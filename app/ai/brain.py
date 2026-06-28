from app.ai.parser import AtlasParser


class AtlasBrain:

    def __init__(self):

        self.parser = AtlasParser()

    def think(self, text):

        memory = self.parser.parse(text)

        return memory