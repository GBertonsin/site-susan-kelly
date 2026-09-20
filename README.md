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

## Pendências conhecidas (marcadas como `TODO` no código)

- Substituir os placeholders de imagem (portfólio da Susan, galeria dos
  alunos, foto de perfil) por fotos reais, mediante autorização de uso
  de imagem.
- Confirmar textos institucionais e nomes/descrições reais dos cursos
  junto à proprietária.
- Substituir o bloco `.agenda-embed` pelo `<iframe>` real da Agenda de
  Compromissos do Google Calendar, assim que os horários forem
  configurados (Sprint 03).
- Substituir `55SEUNUMEROAQUI` no botão do WhatsApp pelo número real da
  instituição, no formato `55DDDNUMERO`.

## Publicação (deploy)

O deploy é feito pela integração Git nativa do hPanel da Hostinger
(Avançado → Git), apontando para este repositório e branch `main`, com
deploy automático a cada push.

## Licença

Projeto acadêmico/extensionista. Conteúdo e imagens da Escola de Artes
Susan Kelly pertencem à instituição.
