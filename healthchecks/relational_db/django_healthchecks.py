from django.db import connection


def is_database_healthy() -> bool:
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT 1')
            return tuple(cursor.fetchone()) == (1,)
    except IOError:
        return False
