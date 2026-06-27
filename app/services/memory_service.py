from app.repositories.memory_repository import *

def create_memory():

    print()

    print("ثبت حافظه")

    print()

    title=input("عنوان : ")

    print()

    print("نوع")

    print("1-شخص")

    print("2-شرکت")

    print("3-ایده")

    print("4-رویداد")

    print("5-هزینه")

    print("6-درآمد")

    print()

    t=input("انتخاب : ")

    mapping={

        "1":"شخص",

        "2":"شرکت",

        "3":"ایده",

        "4":"رویداد",

        "5":"هزینه",

        "6":"درآمد"

    }

    memory_type=mapping.get(t,"سایر")

    content=input("توضیحات : ")

    importance=int(input("اهمیت (1-5): "))

    add_memory(

        title,

        memory_type,

        content,

        importance

    )

    print()

    print("ثبت شد.")

    input()



def show_memories():

    memories=get_memories()

    print()

    print("="*70)

    print("حافظه اطلس")

    print("="*70)

    for m in memories:

        print()

        print("شناسه :",m[0])

        print("عنوان :",m[1])

        print("نوع :",m[2])

        print("اهمیت :",m[4])

        print("زمان :",m[6])

        print("توضیح :",m[3])

        print("-"*70)

    input()