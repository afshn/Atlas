from app.ai.parser import AtlasParser


class MemoryAgent:

    def __init__(self):

        self.parser = AtlasParser()

    def analyze(self, text):

        return self.parser.parse(text)