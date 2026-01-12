from typing import Any

import psycopg2


class DBManager:
    """Класс для работы с БД"""

    def __init__(self, params: dict, database_name: str) -> None:
        self.params = params
        self.database_name = database_name

    def connection(self) -> Any:
        return psycopg2.connect(dbname=self.database_name, **self.params)

    def get_companies_and_vacancies_count(self) -> Any:
        """Получает список всех компаний и количество вакансий у каждой компании"""
        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT name, open_vacancies FROM employers")
                return cur.fetchall()

    def get_all_vacancies(self) -> Any:
        """Получает список всех вакансий с указанием названия компании, названия вакансии,
        зарплаты и ссылки на вакансию"""
        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT
                            e.name,
                            v.name,
                            v.salary_from,
                            v.salary_to,
                            v.vacancies_url
                            FROM employers e
                            JOIN vacancies v USING (employers_id)
                """
                )
                return cur.fetchall()

    def get_avg_salary(self) -> Any:
        """Получает среднюю зарплату по вакансиям"""
        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT
                    AVG(
                        COALESCE(
                        (salary_from + salary_to)/2,
                        salary_from,
                        salary_to)) as avg_salary
                        FROM vacancies
                        WHERE salary_from IS NOT NULL OR salary_to IS NOT NULL
                """)
                return cur.fetchall()[0]

    def get_vacancies_with_higher_salary(self) -> Any:
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        avg_salary = self.get_avg_salary()
        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT *
                FROM vacancies
                WHERE COALESCE(
                            (salary_from + salary_to)/2,
                            salary_from,
                            salary_to) > %s
                """,
                    (avg_salary,),
                )
                return cur.fetchall()

    def get_vacancies_with_keyword(self, world: str) -> Any:
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python"""
        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """SELECT *
                FROM vacancies
                WHERE name ILIKE %s""",
                    (f"%{world}%",),
                )
                return cur.fetchall()
