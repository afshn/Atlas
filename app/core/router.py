from app.agents.memory_agent import MemoryAgent
from app.agents.financial_agent import FinancialAgent


class AtlasRouter:

    def __init__(self):

        self.memory = MemoryAgent()
        self.financial = FinancialAgent()

    def memory_route(self, text):

        return self.memory.analyze(text)

    def financial_route(self, text):

        return self.financial.analyze(text)