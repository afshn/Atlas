from app.database.schema import create_database
from app.database.financial_schema import create_financial_tables

from app.core.atlas_core import AtlasCore

create_database()
create_financial_tables()

core = AtlasCore()

while True:

    print("\n" + "=" * 40)
    print("ATLAS")
    print("=" * 40)
    print("1. ثبت اطلاعات")
    print("2. مشاهده حافظه ها")
    print("3. خروج")

    choice = input("\nانتخاب: ")

    if choice == "1":

        print()

        text = input("> ")

        event = core.process(text)

        if "memory" in event.results:

            print("\n✓ حافظه ثبت شد")
            print(event.results["memory"])

        if "financial" in event.results:

            print("\n✓ تراکنش مالی ثبت شد")
            print(event.results["financial"])

        input("\nEnter...")

    elif choice == "2":

        memories = core.get_memories()

        print()

        print("=" * 70)
        print("حافظه های Atlas")
        print("=" * 70)

        for row in memories:

            print()

            print("شناسه :", row[0])
            print("متن :", row[1])
            print("تاریخ :", row[2])
            print("دسته :", row[3])
            print("عمل :", row[4])
            print("اهمیت :", row[5])
            print("نیاز به پیگیری :", "بله" if row[6] else "خیر")
            print("اشخاص :", row[7])
            print("برچسب :", row[8])

            print("-" * 70)

        input("\nEnter...")

    elif choice == "3":

        break