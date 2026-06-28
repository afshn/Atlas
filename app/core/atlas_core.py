from app.core.router import AtlasRouter
from app.repositories.memory_repository import MemoryRepository


class AtlasCore:

    def __init__(self):

        self.router = AtlasRouter()
        self.memory_repository = MemoryRepository()

    def is_financial(self, text):

        financial_words = [
            "پرداخت",
            "خرید",
            "فروش",
            "هزینه",
            "درآمد"
        ]

        return any(word in text for word in financial_words)

    def process(self, text):

        if self.is_financial(text):

            result = self.router.financial_route(text)

            return "financial", result

        result = self.router.memory_route(text)

        self.memory_repository.save(result)

        return "memory", result

    def get_memories(self):

        return self.memory_repository.all()