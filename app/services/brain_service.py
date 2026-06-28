from app.ai.parser import AtlasParser
from app.repositories.memory_repository import MemoryRepository


class BrainService:

    def __init__(self):

        self.parser = AtlasParser()

        self.repository = MemoryRepository()

    def observe(self):

        print()

        text = input("چه اتفاقی افتاده؟\n\n> ")

        memory = self.parser.parse(text)

        self.repository.save(memory)

        print("\nثبت شد\n")

        print(memory.text)

        input("\nEnter...")

    def show_memories(self):

        print()

        rows = self.repository.all()

        print("=" * 70)

        print("حافظه های Atlas")

        print("=" * 70)

        for row in rows:

            print()

            print("ID :", row[0])

            print("متن :", row[1])

            print("دسته :", row[3])

            print("عمل :", row[4])

            print("اهمیت :", row[5])

            print("پیگیری :", bool(row[6]))

            print("اشخاص :", row[7])

            print("برچسب :", row[8])

            print("-" * 70)

        input("\nEnter...")