# CLI_Tasks_Scripts

Repository containing checker scripts for CLI Tasks.

Structure for checker scripts is `scripts/topic_name/task_name`.
Both topic name and task name are lowercase and have their spaces replaced by
underscores by default.

This repo also contains scripts to add or remove tasks.

# Usage

In order to add a new task, simply run:
```
$ python3 add_task.py --db <db_location>
```

To delete a task:
```
$ python3 remove_task.py --db <db_location>
```

Note that db_location is the sqlite file path, usually in
CLI_Tasks/db/cli_tasks.db, where CLI_Tasks is a different repository.
