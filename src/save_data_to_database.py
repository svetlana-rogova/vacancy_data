from typing import Any

import psycopg2


def save_data_to_database(data: list[dict[str, Any]], database_name: str, params: dict) -> None:
    """Сохранение данных о компаниях и вакансиях в базу данных"""
    conn = psycopg2.connect(dbname=database_name, **params)
    with conn.cursor() as cur:
        for dict_data in data:
            employer_data = dict_data["employers"]
            cur.execute(
                """
                INSERT INTO employers (employers_id, name, site_url, city, open_vacancies)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    employer_data["id"],
                    employer_data["name"],
                    employer_data["site_url"],
                    employer_data["city"],
                    employer_data["open_vacancies"],
                ),
            )
            vacancies_data = dict_data["vacancies"]
            for vac in vacancies_data:
                salary_from = None
                salary_to = None
                currency = None

                if vac["salary"] is not None:
                    salary_from = vac["salary"]["from"]
                    salary_to = vac["salary"]["to"]
                    currency = vac["salary"]["currency"]
                cur.execute(
                    """
                    INSERT INTO vacancies (vacancies_id, name, employer, city, salary_from, salary_to, currency,
                    employers_id, vacancies_url, published_at)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    """,
                    (
                        vac["id"],
                        vac["name"],
                        vac["employer"]["name"],
                        vac["area"]["name"],
                        salary_from,
                        salary_to,
                        currency,
                        vac["employer"]["id"],
                        vac["employer"]["vacancies_url"],
                        vac["published_at"],
                    ),
                )
    conn.commit()
    conn.close()
