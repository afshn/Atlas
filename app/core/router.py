from app.ai.parser import AtlasParser
from app.agents.financial_agent import FinancialAgent


class AtlasRouter:

    def __init__(self):

        self.memory = AtlasParser()

        self.financial = FinancialAgent()

    def process(self, text):

        financial_words = [

            "پرداخت",

            "خرید",

            "فروش",

            "درآمد",

            "هزینه"

        ]

        for word in financial_words:

            if word in text:

                return "financial", self.financial.analyze(text)

        return "memory", self.memory.parse(text)