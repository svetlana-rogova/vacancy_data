import psycopg2


def create_database(database_name: str, params: dict) -> None:
    """Создание базы данных и таблиц для сохранения данных"""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
    cur.execute(f"CREATE DATABASE {database_name}")

    cur.close()
    conn.close()

    with psycopg2.connect(dbname=database_name, **params) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE employers (
                    employers_id INTEGER PRIMARY KEY,
                    employer_name VARCHAR(255) NOT NULL,
                    site_url TEXT,
                    city TEXT
                )
            """)

        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE vacancies(
                    vacancies_id INTEGER PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    employer TEXT,
                    city TEXT,
                    salary_from INTEGER,
                    salary_to INTEGER,
                    currency TEXT,
                    employers_id INT REFERENCES employers(employers_id),
                    vacancies_url TEXT,
                    published_at DATE
                )
            """)

    conn.close()
