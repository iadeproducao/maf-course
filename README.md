# Microsoft Agent Framework in Practice

> **Aprenda a construir agentes de IA para aplicações reais utilizando o Microsoft Agent Framework (MAF).**

Este repositório acompanha uma série de artigos e vídeos sobre o **Microsoft Agent Framework**, abordando desde os conceitos fundamentais até a construção de arquiteturas completas para sistemas de IA em produção.

O objetivo não é apenas ensinar a API do framework, mas mostrar **como projetar, implementar e evoluir aplicações reais baseadas em agentes**, utilizando boas práticas de engenharia de software.

---

# Objetivos

Ao longo deste curso você aprenderá a:

* Criar agentes utilizando o Microsoft Agent Framework.
* Integrar diferentes modelos de linguagem (OpenAI, Azure OpenAI, OpenRouter e outros provedores compatíveis).
* Construir aplicações baseadas em múltiplos agentes.
* Utilizar ferramentas (Tools) e chamadas de funções.
* Implementar memória e gerenciamento de contexto.
* Trabalhar com MCP (Model Context Protocol).
* Integrar agentes com bancos de dados, APIs REST e serviços externos.
* Construir sistemas RAG (Retrieval-Augmented Generation).
* Implementar Human-in-the-Loop (HITL).
* Organizar projetos utilizando boas práticas de arquitetura.
* Preparar aplicações para ambientes de produção.

---

# Público-alvo

Este material é destinado a:

* Desenvolvedores de Software
* Engenheiros de IA
* Arquitetos de Software
* Desenvolvedores .NET e Python
* Pessoas que já utilizam LangChain, LangGraph, CrewAI, Semantic Kernel ou AutoGen e desejam conhecer o Microsoft Agent Framework.

---

# Filosofia do Curso

Grande parte do conteúdo disponível atualmente apresenta apenas exemplos simples, como chatbots ou pequenos agentes de demonstração.

Neste curso, o foco será diferente.

A proposta é responder perguntas como:

* Como estruturar um projeto real utilizando o MAF?
* Como integrar agentes com APIs corporativas?
* Como construir um sistema RAG utilizando o framework?
* Como utilizar múltiplos agentes trabalhando em conjunto?
* Como preparar uma aplicação para produção?
* Quais são as boas práticas de arquitetura?
* Em quais situações o Microsoft Agent Framework é mais adequado do que outras soluções?

Mais do que aprender a utilizar uma biblioteca, o objetivo é compreender como construir aplicações robustas, escaláveis e fáceis de manter.

---

# Estrutura do Curso

## Parte 1 — Fundamentos

* Introdução ao Microsoft Agent Framework
* Arquitetura do Framework
* Instalação
* Primeiro Agente
* Clientes de Modelos (OpenAI, Azure OpenAI e OpenRouter)

---

## Parte 2 — Construindo Agentes

* Prompts e Instructions
* Estado e Contexto
* Ferramentas (Tools)
* Function Calling
* Memória
* Tratamento de Erros

---

## Parte 3 — Aplicações Reais

* Integração com APIs REST
* Integração com Bancos de Dados
* Agentes consumindo documentos
* RAG
* Human-in-the-Loop
* Observabilidade
* Logging

---

## Parte 4 — Arquiteturas

* Multi-Agent Systems
* Orquestração
* MCP (Model Context Protocol)
* Arquiteturas Empresariais
* Escalabilidade
* Deploy

---

# Estrutura do Repositório

```text
maf-course/
│
├── docs/
│   ├── 01-introducao.md
│   ├── 02-instalacao.md
│   ├── 03-primeiro-agente.md
│   └── ...
│
├── examples/
│   ├── 01-primeiro-agente.py
│   ├── 02-openrouter.py
│   ├── 03-tools.py
│   └── ...
│
└── README.md
```

Cada capítulo da documentação possui exemplos completos dentro da pasta `examples`.

---

# Tecnologias Utilizadas

* Python
* Microsoft Agent Framework
* OpenAI
* Azure OpenAI
* OpenRouter
* MCP (Model Context Protocol)
* FastAPI
* Docker
* GitHub

Ao longo do curso também serão apresentados exemplos de integração com bancos vetoriais, APIs REST e aplicações corporativas.

---

# Pré-requisitos

Conhecimentos básicos de:

* Python
* APIs REST
* Git
* Conceitos básicos de IA Generativa (LLMs)

Não é necessário conhecimento prévio do Microsoft Agent Framework.

---

# Como Executar os Exemplos

Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/maf-course.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` baseado no `.env.example`:

```text
OPENROUTER_API_KEY=...
```

Execute qualquer exemplo:

```bash
python examples/01-primeiro-agente.py
```

---

# Roadmap

* [x] Introdução
* [ ] Instalação
* [ ] Primeiro Agente
* [ ] OpenRouter
* [ ] Azure OpenAI
* [ ] Tools
* [ ] Function Calling
* [ ] Memória
* [ ] MCP
* [ ] Multi Agents
* [ ] RAG
* [ ] Human-in-the-Loop
* [ ] Observabilidade
* [ ] Deploy

Este roadmap será atualizado continuamente conforme novos capítulos forem publicados.

---

# Contribuições

Sugestões, correções e melhorias são sempre bem-vindas.

Caso encontre algum problema ou tenha alguma sugestão de conteúdo, abra uma *Issue* ou envie um *Pull Request*.

---

# Licença

Código dos exemplos: Licença MIT.
Textos do curso (README, capítulos, imagens e materiais didáticos): Copyright © Fabio Navarro. Todos os direitos reservados.

---

## Sobre este projeto

O Microsoft Agent Framework representa uma nova geração de ferramentas para o desenvolvimento de aplicações baseadas em agentes de IA.

Este repositório foi criado para compartilhar conhecimento de forma prática, sempre com foco em cenários encontrados no desenvolvimento de software profissional.

Se este material ajudar você de alguma forma, deixe uma ⭐ no repositório. Isso incentiva a continuidade da série e ajuda outras pessoas a encontrarem este conteúdo.
