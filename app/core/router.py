from app.ai.parser import AtlasParser
from app.agents.financial_agent import FinancialAgent


class AtlasRouter:

    def __init__(self):

        self.memory = AtlasParser()
        self.financial = FinancialAgent()

    def memory_route(self, text):

        return self.memory.parse(text)

    def financial_route(self, text):

        return self.financial.analyze(text)