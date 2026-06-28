from app.database.schema import create_database
from app.database.financial_schema import create_financial_tables

from app.repositories.memory_repository import MemoryRepository
from app.core.router import AtlasRouter

create_database()
create_financial_tables()

router = AtlasRouter()

memory_repository = MemoryRepository()

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

        route, result = router.process(text)

        if route == "memory":

            memory_repository.save(result)

            print("\n✓ حافظه ثبت شد")

        elif route == "financial":

            print("\n✓ تراکنش مالی ثبت شد")

        print()

        input("Enter...")

    elif choice == "2":

        memories = memory_repository.all()

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