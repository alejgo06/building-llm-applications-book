# Building LLM Applications

This repository contains examples and experiments for building LLM applications with Python, LangChain, and different LLM providers.

The project is based on the original repository and the accompanying O'Reilly course/book.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/alejgo06/building-llm-applications-book.git
cd building-llm-applications-book.git
```

### 2. Install dependencies

The project uses [uv](https://docs.astral.sh/uv/) for Python package and environment management.

After cloning the repository, run:

```bash
uv sync
```

This will create the virtual environment and install the project dependencies.

### 3. Activate the virtual environment

When you want to work interactively with the project, activate the virtual environment:

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

> You don't necessarily need to activate the environment when using `uv run`.

## Running a Script

You can run any Python script using `uv run`.

For example:

```powershell
uv run .\chain_try_5_1.py
```


## Environment Variables

Some examples require API keys or configuration through environment variables.

Create a `.env` file in the project root if you want to use cloud-based LLM providers:

```env
LLM_PROVIDER=zai OR gpt

ZAI_API_KEY=your_api_key
OPENAI_API_KEY=your_api_key
```

If `LLM_PROVIDER` is not defined, the application uses the local Ollama model by default.

For example:

```env
LLM_PROVIDER=local
```

or:

```env
LLM_PROVIDER=zai
```

Make sure that `.env` is included in `.gitignore` and never commit your API keys to the repository.

## Original Repository

This project is based on:

https://github.com/roberto-inf/building-llm-applications

## Learning Resources

### O'Reilly — AI Agents and Applications

**Audio / Video:**

https://learning.oreilly.com/videos/ai-agents-and/9781633436541AU/9781633436541AU-agents_ch4/

**Text:**

https://learning.oreilly.com/library/view/ai-agents-and/9781633436541/Text/chapter-4.html
