import argparse

from dbhandler import DbHandler
from utils import clear_screen, check_db_exists

def get_topic_name(path_to_db):
    print("\nCurrent list of topics:\n")

    topics = DbHandler.list_topics(path_to_db)
    for topic in topics:
        print(topic)

    print("\nPlease insert the topic name, or a new one, case sensitive. It cannot contain spaces.")

    while True:
        topic_name = input("Topic name: ")
        if " " in topic_name:
            print("It cannot contain spaces.")
        else:
            if not os.path.exists("scripts/" + topic_name):
                print("Directory scripts/" + topic_name + " not found.")
            else:
                return topic_name

def get_task_name(path_to_db):
    print("\nPlease insert the task name, case sensitive. It must not exist.")
    all_tasks = DbHandler.get_all_tasks(path_to_db)
    all_tasks = [x.lower() for x in all_tasks]

    while True:
        task_name = input("Task name: ")
        if task_name.lower() in all_tasks:
            print("This task already exists.")
        else:
            return task_name

def get_checker_name(path_to_db, topic_name):
    print("\nPlease provide the checker name (e.g. the name of the file, including extension)")
    all_checker_names = DbHandler.get_checker_names(path_to_db)

    while True:
        checker_name = input("Checker name: ")
        if checker_name in all_checker_names:
            print("Checker name already exists for topic " + DbHandler.get_topic_for_checker(path_to_db, checker_name))
        else:
            if not os.path.exists("scripts/" + topic_name + "/" + checker_name):
                print("File scripts/" + topic_name + "/" + checker_name + " not found.")
            else:
                return checker_name

def get_checker_language(path_to_db):
    print("\nPlease provide the checker language. Currently supported languages:")
    all_checker_languages = DbHandler.get_checker_languages(path_to_db)

    for language in all_checker_languages:
        print(language)

    while True:
        language = input("Checker language: ")
        if language not in all_checker_languages:
            print("Language does not exist. Please select an existing one.")
        else:
            return language

def greet():
    clear_screen()
    print("Hello. Please copy your checker script in the scripts directory, " + \
        "under the topic name folder.\nIf it does not exist, create it. " + \
        "The topic and task names should be all lower case and should contain no " + \
        "spaces.\nPlease use underscores instead of spaces.\n\n"
        "Example: scripts/filesystem/file_maker.py.\n\nNote: your task name may " + \
        "still contain spaces and mixed cases, inside the application.\n\n" + \
        "Please type 'done' when finished: ", end='')

    while True:
        if input() == "done":
            break

def get_task_desc():
    return input("Please provide the task description:\nDescription: ")

def insert_data_in_db(path_to_db, topic, task, checker_name, checker_language, description, added_by):
    topic_id = DbHandler.insert_topic(path_to_db, topic)
    DbHandler.insert_task(path_to_db, topic_id, task, checker_name, checker_language, description, added_by)

def get_added_by():
    return input("Please provide your name (optional, can be left empty):\nName: ")

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

    topic = get_topic_name(args.db)
    task = get_task_name(args.db)
    checker_name = get_checker_name(args.db, topic)
    checker_language = get_checker_language(args.db)
    description = get_task_desc()
    added_by = get_added_by()

    insert_data_in_db(args.db, topic, task, checker_name, checker_language, description, added_by)

    print("Done")

if __name__ == "__main__":
    main()
