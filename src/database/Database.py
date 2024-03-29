import psycopg2
import os

# Database connection.
database_url = os.environ.get('DATABASE_URL')
connection = psycopg2.connect(database_url)

# Get every to-do item.
def get_todos():
    try:
        with connection, connection.cursor() as cursor:
            query = f'SELECT * FROM todos ORDER BY id;'
            cursor.execute(query)
            return cursor.fetchall()

    except Exception as e:
        print(f'\nERROR: {e}\n')
        connection.rollback()


# Add to-do item.
def add_todo(task):
    try:
        with connection, connection.cursor() as cursor:
            query = f'INSERT INTO todos (task) VALUES (%s);'
            cursor.execute(query, (task,))
            connection.commit()

    except Exception as e:
        print(f'\nERROR: {e}\n')
        connection.rollback()


# Delete to-do item.
def delete_todo(todo_id):
    try:
        with connection, connection.cursor() as cursor:
            query = f'DELETE FROM todos WHERE id = %s;'
            cursor.execute(query, (todo_id,))
            connection.commit()

    except Exception as e:
        print(f'\nERROR: {e}\n')
        connection.rollback()
