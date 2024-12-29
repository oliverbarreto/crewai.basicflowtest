#!/usr/bin/env python
from datetime import datetime
from random import randint, choice
import os

from dotenv import load_dotenv

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start, and_

from crews.poem_crew.poem_crew import PoemCrew
from crews.joke_creation_crew.joke_creation_crew import JokeCrew

from langtrace_python_sdk import langtrace


class PoemState(BaseModel):
    sentence_count: int = 1
    topic: str = ""
    poem: str = ""
    joke: str = ""


class PoemFlow(Flow[PoemState]):

    load_dotenv()

    # Must precede any llm module imports
    load_dotenv()
    LANGTRACE_API_KEY = os.getenv("LANGTRACE_API_KEY")
    langtrace.init(api_key=LANGTRACE_API_KEY)

    @start()
    def generate_sentence_count(self):
        print("Generating sentence count")
        topics = ["Donald Trump", "Biology", "Math", "The Canary Islands"]
        self.state.topic = choice(topics)
        self.state.sentence_count = randint(1, 5)

    @listen(generate_sentence_count)
    def generate_poem(self):
        print("Generating poem")
        result = (
            PoemCrew()
            .crew()
            .kickoff(
                inputs={
                    "sentence_count": self.state.sentence_count,
                    "topic": self.state.topic,
                }
            )
        )

        print("Poem generated", result.raw)
        self.state.poem = result.raw

    @listen(generate_sentence_count)
    def generate_joke(self):
        print("Generating Dad Joke")
        result = (
            JokeCrew()
            .crew()
            .kickoff(
                inputs={
                    "sentence_count": self.state.sentence_count,
                    "topic": self.state.topic,
                }
            )
        )

        print("Dad Joke generated", result.raw)
        self.state.joke = result.raw

    @listen(and_(generate_poem, generate_joke))
    def save_poem(self):
        print("Saving")
        output_dir = "output"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        date_str = datetime.now().strftime("%Y%m%d_%H%M")
        output_file = f"poem_{self.state.topic}_{date_str}.txt"
        with open(os.path.join(output_dir, output_file), "w") as f:
            print("Saving poem")
            f.write("Poem:\n")
            f.write(self.state.poem)
            f.write("\n\n---\n\n")

            print("Saving joke")
            f.write("Joke:\n")
            f.write(self.state.joke)

            print("Done !!!")


def kickoff():
    poem_flow = PoemFlow()
    poem_flow.kickoff()


def plot():
    poem_flow = PoemFlow()
    poem_flow.plot()


if __name__ == "__main__":
    kickoff()
