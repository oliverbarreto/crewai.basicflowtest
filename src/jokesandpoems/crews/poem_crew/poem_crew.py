from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from langchain_openai import ChatOpenAI


@CrewBase
class PoemCrew:
    """Poem Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # Configuración del modelo
    llm = ChatOpenAI(
        model="ollama/llama3.2",
        temperature=1,
        base_url="http://localhost:11434",  # OLLAMA
        # base_url="http://localhost:52415/v1", #EXO
        api_key="dummy_key",  # Clave ficticia, necesaria para pasar la validación
    )

    @agent
    def poem_writer(self) -> Agent:
        return Agent(config=self.agents_config["poem_writer"], llm=self.llm)

    @task
    def write_poem(self) -> Task:
        return Task(config=self.tasks_config["write_poem"], llm=self.llm)

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
