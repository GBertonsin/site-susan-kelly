"""T05 – Responsividade (RQ01/RQ03, MQ03).

Abre index.html em larguras de 360 a 1920 px e registra, para cada uma:
  - rolagem horizontal da página (scrollWidth > largura da janela);
  - elementos que ultrapassam a largura da janela;
  - sobreposição entre links do menu principal;
  - alvos de toque (links e botões) com menos de 44 px de altura, no mobile;
  - texto com menos de 14 px.
Uso: python3 tests/t05_responsividade.py [pasta_de_capturas]
Requer: pip install playwright && playwright install chromium
"""
import json, os, sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "tests" / "saida"
OUT.mkdir(parents=True, exist_ok=True)
LARGURAS = [360, 390, 414, 768, 1024, 1280, 1440, 1920]

JS = """
() => {
  const vw = document.documentElement.clientWidth;
  const r = {vw, scrollW: document.documentElement.scrollWidth, overflow: [], navOverlap: [], small: [], font: []};
  document.querySelectorAll('body *').forEach(el => {
    const b = el.getBoundingClientRect();
    if (b.width === 0 || b.height === 0) return;
    if (b.right > vw + 1 && getComputedStyle(el).position !== 'fixed') {
      let p = el.parentElement, clipped = false;
      while (p && p !== document.body) { const o = getComputedStyle(p).overflowX; if (o === 'hidden' || o === 'auto' || o === 'scroll') { clipped = true; break; } p = p.parentElement; }
      if (!clipped) r.overflow.push((el.className || el.tagName) + ' → ' + Math.round(b.right) + 'px');
    }
  });
  const links = [...document.querySelectorAll('.main-nav a')].filter(a => a.offsetParent);
  for (let i = 0; i < links.length; i++) for (let j = i + 1; j < links.length; j++) {
    const a = links[i].getBoundingClientRect(), c = links[j].getBoundingClientRect();
    if (a.left < c.right && c.left < a.right && a.top < c.bottom && c.top < a.bottom) r.navOverlap.push(links[i].textContent + ' × ' + links[j].textContent);
  }
  document.querySelectorAll('a, button').forEach(el => {
    const b = el.getBoundingClientRect();
    if (b.width && b.height && b.height < 44) r.small.push(el.textContent.trim().slice(0, 30) + ' (' + Math.round(b.height) + 'px)');
  });
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const seen = new Set();
  while (walker.nextNode()) {
    const n = walker.currentNode; if (!n.textContent.trim()) continue;
    const el = n.parentElement; if (!el || !el.offsetParent) continue;
    const fs = parseFloat(getComputedStyle(el).fontSize);
    if (fs < 14 && !seen.has(el)) { seen.add(el); r.font.push(el.className + ' ' + fs + 'px'); }
  }
  return r;
}
"""

resultado = []
with sync_playwright() as p:
    br = p.chromium.launch()
    for w in LARGURAS:
        pg = br.new_page(viewport={"width": w, "height": 900})
        pg.goto((ROOT / "index.html").as_uri()); pg.wait_for_timeout(400)
        r = pg.evaluate(JS)
        r["largura"] = w
        r["scroll_horizontal"] = r["scrollW"] > r["vw"]
        pg.screenshot(path=str(OUT / f"t05_{w}.png"), full_page=True)
        resultado.append(r); pg.close()
    br.close()

falhas = 0
for r in resultado:
    problemas = []
    if r["scroll_horizontal"]: problemas.append(f"rolagem horizontal ({r['scrollW']} > {r['vw']})")
    if r["overflow"]: problemas.append(f"{len(r['overflow'])} elemento(s) além da janela: {r['overflow'][:3]}")
    if r["navOverlap"]: problemas.append(f"menu sobreposto: {r['navOverlap']}")
    if r["largura"] <= 414 and r["small"]: problemas.append(f"{len(r['small'])} alvo(s) de toque < 44 px: {r['small'][:4]}")
    if r["font"]: problemas.append(f"texto < 14 px: {r['font'][:4]}")
    falhas += bool(problemas)
    print(f"{r['largura']:>5} px:", "OK" if not problemas else "FALHA")
    for x in problemas: print("        -", x)
(OUT / "t05_resultado.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=1))
print(f"\n{len(LARGURAS) - falhas} de {len(LARGURAS)} larguras sem falha")
sys.exit(1 if falhas else 0)
