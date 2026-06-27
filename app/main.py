from app.database.schema import create_database

from app.core.dashboard import show_dashboard

from app.services.memory_service import *

def main():

    create_database()

    while True:

        show_dashboard()

        choice=input("انتخاب : ")

        if choice=="1":

            create_memory()

        elif choice=="2":

            show_memories()

        elif choice=="3":

            break

if __name__=="__main__":

    main()