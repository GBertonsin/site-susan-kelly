# Escola de Artes Susan Kelly — Site institucional e agendamento

Projeto de extensão da disciplina **Qualidade de Software Aplicada**
(UniEVANGÉLICA), desenvolvido para a Escola de Artes Susan Kelly: um novo
site institucional, com um sistema de agendamento de aulas mais confiável
do que o processo manual atual (WhatsApp + Google Drive).

## Equipe

- Gabriel Bertonsin Silva Brito

## O que este projeto entrega

- Site institucional estático (HTML/CSS/JS), com as seções Início, Sobre,
  Portfólio da Susan, Cursos, Galeria dos alunos, Agendamento e Contato.
- Agendamento de aulas via **Agenda de Compromissos do Google Calendar**,
  embutida na página (a ser configurada na Sprint 03).
- Botão de confirmação via WhatsApp (`wa.me`) como reforço opcional.
- Publicação automática (deploy) na Hostinger a cada push na branch `main`.

O detalhamento completo de requisitos, escopo do MVP, arquitetura e
planejamento das sprints está no relatório técnico do projeto (entregue
separadamente à disciplina).

## Estrutura do repositório

```
.
├── index.html          # página única do site (todas as seções)
├── css/
│   └── style.css       # estilos do site
├── js/
│   └── main.js         # script do site (por enquanto, mínimo)
├── favicon.svg         # ícone do site (símbolo da marca)
├── tests/
│   ├── t04_chromium.py        # teste T04 parcial: navegação, imagens e contraste
│   └── t05_responsividade.py  # teste T05 (360 a 1920 px)
├── assets/
│   ├── img/            # imagens reais (portfólio, galeria, fotos) — a preencher
│   └── logo/           # logotipos da marca em SVG
└── README.md
```

## Identidade visual

Segue o livro de identidade visual entregue pela proprietária (designer
Rafael Marques). O marfim ocupa cerca de 60% da página; as demais cores são
acentos.

- **Cores:** `#F4EFE6` (tela, marfim — fundo), `#C17B5C` (escultura, terracota),
  `#9B7653` (tradição, ocre), `#6B7C5E` (natureza, verde sálvia), `#3D4F5C`
  (pigmento, azul slate — títulos, botões e seções escuras) e `#3A3A3A`
  (traço, grafite — texto corrido). Terracota, ocre e verde não têm contraste
  suficiente para texto corrido sobre o marfim (de 2,9:1 a 3,9:1), por isso só
  são usados em texto grande e detalhes.
- **Tipografia:** as fontes da marca (Arpona, Redonda e Bickham Script) são do
  Adobe Fonts e exigem assinatura. O site usa equivalentes gratuitas do Google
  Fonts, para manter o custo zero: [Fraunces](https://fonts.google.com/specimen/Fraunces)
  nos títulos, [Figtree](https://fonts.google.com/specimen/Figtree) no texto
  corrido e [Pinyon Script](https://fonts.google.com/specimen/Pinyon+Script)
  nos destaques. Para usar as originais, troque as três variáveis `--font-*`
  em `css/style.css` e o link de fontes no `index.html`.
- **Logo:** arquivos SVG em `assets/logo/` (horizontal e símbolo, em versão
  escura e branca). Não altere as proporções nem as cores do logo.

## Como visualizar localmente

Não há build nem dependências. Basta abrir `index.html` num navegador, ou
servir a pasta com qualquer servidor estático, por exemplo:

```bash
python3 -m http.server 8000
```

e acessar `http://localhost:8000`.

## Como executar o teste de responsividade (T05)

Requer Python 3 e o Playwright (`pip install playwright` e `playwright install chromium`).
Na raiz do repositório, rode:

```bash
python3 tests/t05_responsividade.py
```

O script abre o `index.html` em 8 larguras (360 a 1920 px), verifica rolagem
horizontal, elementos fora da janela, sobreposição do menu, alvos de toque
menores que 44 px e texto menor que 14 px, e salva uma captura de tela de cada
largura em `tests/saida/` (pasta ignorada pelo Git). O código de saída é 0 quando
todas as larguras passam.

## Como executar o teste de navegação e contraste (T04, parte do Chromium)

Mesmos requisitos do T05. Na raiz do repositório, rode:

```bash
python3 tests/t04_chromium.py
```

O script confere se os links de navegação levam à seção certa (desktop e
mobile), se toda imagem tem texto alternativo e carrega, se o contraste do
texto atinge 4,5:1 (3:1 para texto grande) e se não há erros no console.
Cobre apenas o Chromium: Safari, Edge e aparelhos reais são testados à mão na
Sprint 04.

## Critérios de aceite das páginas institucionais

Referência para a revisão da Sprint 02. Cada página (seção) só é considerada
concluída quando atende aos critérios abaixo. *Status: critérios propostos em
11/10/2026, a confirmar com a proprietária.*

| Página / seção | Critério de aceite (verificável) |
| --- | --- |
| Início | Título principal e botão "Ver horários e agendar" visíveis; o botão leva à seção `#agendamento`; os 5 links da navegação rolam até a seção correta. |
| Sobre | Texto institucional confirmado pela Susan; foto real dela no lugar do placeholder; público-alvo confirmado; nenhum texto "(a inserir)" visível. |
| Portfólio | Os 6 quadros substituídos por fotos reais das obras da Susan, cada uma com texto alternativo; nenhum placeholder "obra 0X" visível. |
| Cursos | Nome, descrição e nível/faixa etária de cada curso confirmados pela Susan; nenhum curso de exemplo restante. |
| Galeria | Apenas trabalhos reais de alunos com autorização de uso de imagem confirmada por escrito; nenhum placeholder "trabalho" visível. |
| Todas | Sem sobreposição de elementos nem rolagem horizontal entre 360 px e 1920 px de largura; nenhum link quebrado; nenhum `TODO` no código publicado fora dos registrados nas Pendências. |

## Pendências conhecidas (marcadas como `TODO` no código)

Todos os 9 comentários `TODO` de `index.html` estão registrados abaixo e
vinculados ao card correspondente do quadro Kanban (Trello). Para conferir,
rode `grep -n TODO index.html` e compare com a tabela: o resultado deve ser
exatamente os 9 itens listados.

| # | Onde (seção) | Pendência | Card no Trello |
| --- | --- | --- | --- |
| 1 | Sobre | Substituir o placeholder pela foto real da Susan Kelly e revisar com ela os textos propostos pela equipe. | Validar conteúdo (textos e imagens) com a Susan |
| 2 | Portfólio | Substituir os 6 quadros por fotos reais das obras da Susan. | Validar conteúdo (textos e imagens) com a Susan |
| 3 | Cursos | Confirmar nomes, descrições e faixas etárias reais dos cursos. | Validar conteúdo (textos e imagens) com a Susan |
| 4 | Galeria | Substituir pelos trabalhos reais dos alunos, com autorização de uso de imagem confirmada. | Validar conteúdo (textos e imagens) com a Susan |
| 5 | Agendamento | Substituir o bloco `.agenda-embed` pelo `<iframe>` da Agenda de Compromissos do Google Calendar (Sprint 03). | Implementar Agenda de Compromissos do Google Calendar |
| 6 | Agendamento | Substituir `55SEUNUMEROAQUI` no botão do WhatsApp pelo número real, no formato `55DDDNUMERO`. | Implementar botão de confirmação via WhatsApp (wa.me) |
| 7 | Rodapé | Inserir o endereço real. | Validar conteúdo (textos e imagens) com a Susan |
| 8 | Rodapé | Inserir o telefone/WhatsApp real. | Validar conteúdo (textos e imagens) com a Susan |
| 9 | Rodapé | Inserir o e-mail real. | Validar conteúdo (textos e imagens) com a Susan |

Ao resolver uma pendência, remova o comentário `TODO` correspondente e a linha
da tabela no mesmo commit.

## Como alterar o conteúdo

Todo o conteúdo está em `index.html`; a aparência está em `css/style.css`.

- **Textos:** abra `index.html` e localize a seção pelo `id` (`#sobre`,
  `#portfolio`, `#cursos`, `#galeria`, `#agendamento`, `#contato`). Edite o
  texto entre as tags e salve.
- **Imagens:** coloque o arquivo em `assets/img/` (nomes em minúsculas, com
  hífen, ex.: `obra-01.jpg`). No `index.html`, troque o bloco de placeholder
  (`<span>obra 01</span>`, `<span>trabalho</span>` ou `<span>foto da Susan...</span>`)
  por `<img src="assets/img/obra-01.jpg" alt="descrição da imagem">`. Todo
  `<img>` deve ter o atributo `alt`.
- **Cores e fontes:** estão como variáveis no início de `css/style.css`
  (`:root`: `--tela`, `--pigmento`, `--traco` etc.). Alterar o valor da variável
  muda o site inteiro.
- **Número de WhatsApp:** no botão "Confirmar pelo WhatsApp", troque
  `55SEUNUMEROAQUI` na URL `https://wa.me/...` pelo número no formato
  `55DDDNUMERO` (somente dígitos, sem espaços, `+` ou parênteses). Ex.:
  `5562999999999`.
- **Agenda de agendamento:** na página de agendamento do Google Calendar,
  copie o código de incorporação (`<iframe ...>`) e cole-o dentro de
  `<div class="agenda-embed">`, no lugar do parágrafo
  `agenda-placeholder`. O estilo do iframe já está no CSS; não use `style`
  inline.
- **Publicar:** salve, faça o commit e o push na branch `main`; o deploy é
  automático (ver "Publicação").

## Publicação (deploy)

O deploy é feito pela integração Git nativa do hPanel da Hostinger
(Avançado → Git), apontando para este repositório e branch `main`, com
deploy automático a cada push.

## Licença

Projeto acadêmico/extensionista. Conteúdo e imagens da Escola de Artes
Susan Kelly pertencem à instituição.
