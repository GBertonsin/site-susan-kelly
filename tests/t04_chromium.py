"""T04 (parcial) – Navegação, imagens e contraste no Chromium.

Cobre apenas o Chromium (desktop e mobile emulado). Safari, Edge e aparelhos
reais ficam para o checklist manual da Sprint 04.
Verifica:
  - os links de navegação e o botão "Ver horários e agendar" levam à seção certa;
  - toda imagem tem texto alternativo e carrega (as decorativas usam alt vazio);
  - contraste do texto contra o fundo (mínimo 4,5:1; 3:1 para texto grande);
  - ausência de erros no console (ignora as fontes do Google, que dependem de rede).
Uso: python3 tests/t04_chromium.py
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = (Path(__file__).resolve().parent.parent / "index.html").as_uri()

JS_CONTRASTE = """
() => {
  const parse = c => { const m = c.match(/rgba?\\(([^)]+)\\)/); if (!m) return null;
    const p = m[1].split(',').map(x => parseFloat(x)); return {r:p[0], g:p[1], b:p[2], a: p.length > 3 ? p[3] : 1}; };
  const over = (f, b) => ({r: f.r*f.a + b.r*(1-f.a), g: f.g*f.a + b.g*(1-f.a), b: f.b*f.a + b.b*(1-f.a), a: 1});
  const lum = c => { const f = v => { v/=255; return v <= 0.03928 ? v/12.92 : Math.pow((v+0.055)/1.055, 2.4); };
    return 0.2126*f(c.r) + 0.7152*f(c.g) + 0.0722*f(c.b); };
  const fundo = el => { const pilha = [];
    for (let e = el; e; e = e.parentElement) { const c = parse(getComputedStyle(e).backgroundColor);
      if (c && c.a > 0) { pilha.push(c); if (c.a === 1) break; } }
    let b = {r:255, g:255, b:255, a:1};
    for (let i = pilha.length - 1; i >= 0; i--) b = over(pilha[i], b);
    return b; };
  const falhas = [], vistos = new Set(); let total = 0;
  const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  while (w.nextNode()) {
    const n = w.currentNode; if (!n.textContent.trim()) continue;
    const el = n.parentElement; if (!el || vistos.has(el)) continue;
    const r = el.getBoundingClientRect(); if (!r.width || !r.height) continue;
    vistos.add(el); total++;
    const cs = getComputedStyle(el); const b = fundo(el);
    let f = parse(cs.color); f = over(f, b);
    const l1 = lum(f), l2 = lum(b); const ratio = (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);
    const px = parseFloat(cs.fontSize), peso = parseInt(cs.fontWeight);
    const grande = px >= 24 || (px >= 18.66 && peso >= 700);
    const minimo = grande ? 3 : 4.5;
    if (ratio < minimo) falhas.push(`${el.tagName.toLowerCase()}.${el.className} "${n.textContent.trim().slice(0,28)}" ${ratio.toFixed(1)}:1 (mín. ${minimo})`);
  }
  return {total, falhas};
}
"""

falhas = []
with sync_playwright() as p:
    br = p.chromium.launch()
    for largura, rotulo in ((1280, "desktop"), (390, "mobile")):
        pg = br.new_page(viewport={"width": largura, "height": 900})
        erros = []
        pg.on("console", lambda m: erros.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: erros.append(str(e)))
        pg.goto(URL); pg.wait_for_timeout(400)

        # navegação por âncoras
        links = pg.eval_on_selector_all('a[href^="#"]', 'els => els.filter(e => e.offsetParent).map(e => [e.getAttribute("href"), e.textContent.trim()])')
        for href, texto in links:
            if href == "#conteudo": continue
            pg.evaluate("window.scrollTo(0, 0)")
            pg.click(f'a[href="{href}"]:visible >> nth=0'); pg.wait_for_timeout(700)
            topo = pg.evaluate(f'document.querySelector("{href}").getBoundingClientRect().top')
            if not -5 <= topo <= 220:
                falhas.append(f"{rotulo}: '{texto}' ({href}) não leva à seção (topo em {topo:.0f}px)")
        print(f"{rotulo}: {len(links)} link(s) de âncora verificados")

        # imagens
        imgs = pg.eval_on_selector_all("img", 'els => els.map(e => [e.getAttribute("src"), e.hasAttribute("alt"), e.complete && e.naturalWidth > 0])')
        for src, tem_alt, ok in imgs:
            if not tem_alt: falhas.append(f"{rotulo}: imagem sem alt: {src}")
            if not ok: falhas.append(f"{rotulo}: imagem não carregou: {src}")
        print(f"{rotulo}: {len(imgs)} imagem(ns) verificadas")

        # contraste
        pg.evaluate("window.scrollTo(0, 0)")
        r = pg.evaluate(JS_CONTRASTE)
        print(f"{rotulo}: {r['total']} trechos de texto avaliados quanto ao contraste")
        falhas += [f"{rotulo}: contraste {x}" for x in r["falhas"]]

        # console
        reais = [e for e in erros if "fonts.g" not in e and "ERR_" not in e and "Failed to load resource" not in e]
        falhas += [f"{rotulo}: erro de console: {e}" for e in reais]
        pg.close()
    br.close()

print()
for f in falhas: print("FALHA:", f)
print("Resultado:", "sem falhas" if not falhas else f"{len(falhas)} falha(s)")
sys.exit(1 if falhas else 0)
