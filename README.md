<div align="center">
  <a href="https://oliverbarreto.com">
    <img src="https://www.oliverbarreto.com/images/site-logo.png" />
  </a>
</div>
</br>
</br>
<div align="center">
  <h1>Testing CrewAI Flows and Crews</h1>
  </br>
  <p>Learning how to ppplying AI Agents to solve real problems... This is just a test with 2 different crews orchestrated with a simple Flow. The result is a file with a poem and a dad joke about a topic.</p>
  <p>It uses local Ollama model "model="ollama/llama3.2".</p>
  </br>
  <p>Resources:</p>
  <a href="https://docs.crewai.com">https://docs.crewai.com</a>
  </br>
  </br>
  <p>Created with ❤️ by Oliver Barreto</p>
</div>

</br>
</br>

---

# Custom Docs

## Install

1. Create a conda environment with: `pip install 'crewai[tools]'` or `pip install crewai crewai-tools`
2. Install LangChain if you are going to use Local Models with e.g. Ollama `pip install langchain-openai`
3. Execute Agentic Flow:

- Inside VS Code: Activate Python Interpreter and run

```shell
~/dev/ai/partidosenlatele main*
❯ python src/partidosenlatele/main.py

- Using CrewAI CLI: `crewai run`
```

## Config

1. Make sure you have a working local Ollama server (http://localhost:11434) and test it with curl

```shell
## Chat with a model
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
```

2. Use Ollama with ChatOpenAI and set llm property of agents and task accordingly

```python
from langchain_openai import ChatOpenAI

# Configuración del modelo
llm = ChatOpenAI(
    model="ollama/llama3.2",
    temperature=1,
    base_url="http://localhost:11434",  # OLLAMA
    # base_url="http://localhost:52415/v1", #EXO
    api_key="dummy_key",  # Clave ficticia, necesaria para pasar la validación
)
```

## IMPORTANT

---

# {{crew_name}} Crew - Official Documentation

Welcome to the {{crew_name}} Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/partidosenlatele/config/agents.yaml` to define your agents
- Modify `src/partidosenlatele/config/tasks.yaml` to define your tasks
- Modify `src/partidosenlatele/crew.py` to add your own logic, tools and specific args
- Modify `src/partidosenlatele/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the partidosenlatele Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The partidosenlatele Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the {{crew_name}} Crew or crewAI.

- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
