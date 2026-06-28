from app.core.router import AtlasRouter
from app.core.event import Event
from app.repositories.memory_repository import MemoryRepository


class AtlasCore:

    def __init__(self):

        self.router = AtlasRouter()

        self.memory_repository = MemoryRepository()

    def detect_agents(self, text):

        event = Event(text=text)

        event.agents.append("memory")

        financial_words = [
            "پرداخت",
            "خرید",
            "فروش",
            "هزینه",
            "درآمد"
        ]

        if any(word in text for word in financial_words):

            event.agents.append("financial")

        return event

    def process(self, text):

        event = self.detect_agents(text)

        for agent in event.agents:

            if agent == "memory":

                memory = self.router.memory_route(text)

                self.memory_repository.save(memory)

                event.results["memory"] = memory

            elif agent == "financial":

                transaction = self.router.financial_route(text)

                event.results["financial"] = transaction

        return event

    def get_memories(self):

        return self.memory_repository.all()