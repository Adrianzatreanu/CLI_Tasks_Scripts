import sqlite3

class DbHandler:

    @staticmethod
    def list_topics(path_to_db):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()
            instruction = "select name from topics"
            cursor.execute(instruction)
            rows = cursor.fetchall()

            topics = []
            for row in rows:
                topics.append(row[0])

            return topics

    @staticmethod
    def get_all_tasks(path_to_db):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select name from tasks"
            cursor.execute(instruction)
            rows = cursor.fetchall()

            tasks = []

            for row in rows:
                tasks.append(row[0])

            return tasks

    @staticmethod
    def get_checker_names(path_to_db):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select name from tasks"
            cursor.execute(instruction)
            rows = cursor.fetchall()

            names = []

            for row in rows:
                names.append(row[0])

            return names

    @staticmethod
    def get_topic_for_checker(path_to_db, checker_name):
        with sqlite3.connect(PATH_TO_DB) as conn:
            cursor = conn.cursor()
            instruction = "select id from tasks where checker_name='{}'".format(checker_name)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return ""

            task_id = row[0]
            instruction = "select topic_id from topic_tasks where task_id={}".format(task_id)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return ""

            topic_id = row[0]
            instruction = "select name from topics where id={}".format(topic_id)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return ""

            return row[0]

    @staticmethod
    def get_checker_languages(path_to_db):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select name from checker_languages"
            cursor.execute(instruction)
            rows = cursor.fetchall()

            languages = []

            for row in rows:
                languages.append(row[0])

            return languages


    @staticmethod
    def insert_topic(path_to_db, topic):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select id from topics where name='{}'".format(topic)
            cursor.execute(instruction)
            row = cursor.fetchone()

            # it exists
            if row is not None:
                return row[0]

            # else insert it
            instruction = "insert into topics(id, name) values(NULL, '{}')".format(topic)
            cursor.execute(instruction)
            conn.commit()

            instruction = "select id from topics where name='{}'".format(topic)
            cursor.execute(instruction)
            row = cursor.fetchone()

            return row[0]

    @staticmethod
    def insert_task(path_to_db, topic_id, task, checker_name, checker_language, description, added_by):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select id from checker_languages where name='{}'".format(checker_language)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return
            checker_language_id = row[0]

            # add to tasks
            cursor.execute("insert into tasks(id, name, added_by, checker_name, checker_language_id, description) " + \
                "values(NULL, ?, ?, ?, ?, ?)", (task, added_by, checker_name, checker_language_id, description))

            instruction = "select id from tasks where name='{}'".format(task)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return
            task_id = row[0]

            # add task to topic
            instruction = "insert into topic_tasks(topic_id, task_id) values({}, {})".format(topic_id, task_id)
            cursor.execute(instruction)

            conn.commit()

    @staticmethod
    def remove_task_from_db(path_to_db, task_name):
        with sqlite3.connect(path_to_db) as conn:
            cursor = conn.cursor()

            instruction = "select id from tasks where name='{}'".format(task_name)
            cursor.execute(instruction)
            row = cursor.fetchone()

            if row is None:
                return
            task_id = row[0]

            instruction = "delete from topic_tasks where task_id={}".format(task_id)
            cursor.execute(instruction)

            instruction = "delete from tasks where id={}".format(task_id)
            cursor.execute(instruction)

            conn.commit()

