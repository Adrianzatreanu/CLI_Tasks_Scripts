# CLI_Tasks_Scripts

Repository containing checker scripts for CLI Tasks.

Structure for checker scripts is `scripts/topic_name/task_name`.
Both topic name and task name are lowercase and have their spaces replaced by
underscores by default.

This repo also contains scripts to add or remove tasks.

Currently supported languages for checker scripts:
 - shell

# Usage

In order to add a new task, you will need to write a script in a supported language
that returns 0 on success, non zero otherwise. Then simply run:
```
$ python3 add_task.py --db <db_location>
```
where db_location is the sqlite database file (usually in the CLI_Tasks repo, under CLI_Tasks/db/cli_tasks.db).
Once your local database and this repository are modified, you will need to do a Pull Request
and merge both of them on master so that the changes become visible.

To delete a task:
```
$ python3 remove_task.py --db <db_location>
```

Note that db_location is the sqlite file path, usually in
CLI_Tasks/db/cli_tasks.db, where CLI_Tasks is a different repository.
