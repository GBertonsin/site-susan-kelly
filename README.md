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
├── assets/
│   └── img/            # imagens reais (portfólio, galeria, fotos) — a preencher
└── README.md
```

## Identidade visual

- **Cores:** `#F2ECDD` (linho/canvas — fundo), `#23263A` (tinta — texto e
  destaques escuros), `#C48A2E` (ocre — cor de ação/CTA), `#A84B2A`
  (terracota — acento secundário), `#56684F` (verde-sálvia — tags).
- **Tipografia:** [Fraunces](https://fonts.google.com/specimen/Fraunces)
  para títulos, [Work Sans](https://fonts.google.com/specimen/Work+Sans)
  para texto corrido — ambas via Google Fonts.

## Como visualizar localmente

Não há build nem dependências. Basta abrir `index.html` num navegador, ou
servir a pasta com qualquer servidor estático, por exemplo:

```bash
python3 -m http.server 8000
```

e acessar `http://localhost:8000`.

## Critérios de aceite das páginas institucionais

Referência para a revisão da Sprint 02. Cada página (seção) só é considerada
concluída quando atende aos critérios abaixo. *Status: critérios propostos em
11/10/2026, a confirmar com a proprietária.*

| Página / seção | Critério de aceite (verificável) |
| --- | --- |
| Início (`#topo`) | Título principal e botão "Ver horários e agendar" visíveis; o botão leva à seção `#agendamento`; os 5 links da navegação rolam até a seção correta. |
| Sobre (`#sobre`) | Texto institucional confirmado pela Susan; foto real dela no lugar do placeholder; público-alvo confirmado; nenhum texto "(a inserir)" visível. |
| Portfólio (`#portfolio`) | Os 6 quadros substituídos por fotos reais das obras da Susan, cada uma com texto alternativo (`alt`); nenhum placeholder "obra 0X" visível. |
| Cursos (`#cursos`) | Nome, descrição e nível/faixa etária de cada curso confirmados pela Susan; nenhum curso de exemplo restante. |
| Galeria (`#galeria`) | Apenas trabalhos reais de alunos com autorização de uso de imagem confirmada por escrito (mensagem ou termo); nenhum placeholder "trabalho" visível. |
| Todas | Sem sobreposição de elementos nem rolagem horizontal entre 360 px e 1920 px de largura; nenhum link quebrado; nenhum `TODO` no código publicado fora dos registrados nas Pendências. |

## Pendências conhecidas (marcadas como `TODO` no código)

Todos os 10 comentários `TODO` de `index.html` estão registrados abaixo e
vinculados ao card correspondente do quadro Kanban (Trello). Para conferir,
rode `grep -n TODO index.html` e compare com a tabela: o resultado deve ser
exatamente os 10 itens listados.

| # | Onde (seção) | Pendência | Card no Trello |
| --- | --- | --- | --- |
| 1 | Sobre | Substituir o placeholder pela foto real da Susan Kelly. | Validar conteúdo (textos e imagens) com a Susan |
| 2 | Sobre | Confirmar se crianças fazem parte do público prioritário. | Validar conteúdo (textos e imagens) com a Susan |
| 3 | Portfólio | Substituir os 6 quadros por fotos reais das obras da Susan. | Validar conteúdo (textos e imagens) com a Susan |
| 4 | Cursos | Confirmar nomes, descrições e faixas etárias reais dos cursos. | Validar conteúdo (textos e imagens) com a Susan |
| 5 | Galeria | Substituir pelos trabalhos reais dos alunos, com autorização de uso de imagem confirmada. | Validar conteúdo (textos e imagens) com a Susan |
| 6 | Agendamento | Substituir o bloco `.agenda-embed` pelo `<iframe>` da Agenda de Compromissos do Google Calendar (Sprint 03). | Implementar Agenda de Compromissos do Google Calendar |
| 7 | Agendamento | Substituir `55SEUNUMEROAQUI` no botão do WhatsApp pelo número real, no formato `55DDDNUMERO`. | Implementar botão de confirmação via WhatsApp (wa.me) |
| 8 | Rodapé | Inserir o endereço real. | Validar conteúdo (textos e imagens) com a Susan |
| 9 | Rodapé | Inserir o telefone/WhatsApp real. | Validar conteúdo (textos e imagens) com a Susan |
| 10 | Rodapé | Inserir o e-mail real. | Validar conteúdo (textos e imagens) com a Susan |

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
  (`:root`: `--ochre`, `--ink`, `--canvas` etc.). Alterar o valor da variável
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
