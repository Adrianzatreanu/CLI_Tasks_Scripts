import argparse

from dbhandler import DbHandler
from utils import clear_screen, check_db_exists

def greet():
	clear_screen()
	print("Hello. This script will help you remove a task from the database. " + \
		  "If you want the files removed from the repo as well, please do it manually.")

def get_task_name(path_to_db):
    print("\nPlease insert the task name, case insensitive. It must not exist.")
    all_tasks = DbHandler.get_all_tasks(path_to_db)

    while True:
        task_name = input("Task name: ")
        for task in all_tasks:
        	if task.lower() == task_name.lower():
        		return task
        print("This task does not exist.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d','--db', help='Sqlite database location',
        type=str, required=True)
    args = parser.parse_args()

    if not check_db_exists(args.db):
        print("The database file does not exist. Perhaps you got the path wrong?" + \
            " If it's a new database, please create it manually.")
        return

    greet()

    task_name = get_task_name(args.db)

    DbHandler.remove_task_from_db(args.db, task_name)

    print("Done")

if __name__ == "__main__":
    main()
