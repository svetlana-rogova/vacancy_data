from typing import Any
from typing import Optional


class Formatter:
    """Форматирует данные из DBManager в человекочитаемый вид"""

    @staticmethod
    def companies(data: list[dict[str, int]]) -> str:
        """Выводит названия компаний и количество вакансий"""
        answer = []
        for info in data:
            answer.append(f"В компании '{info['employer_name']}': {info['vacancies_count']} вакансий.")
        return "\n".join(answer)

    @staticmethod
    def format_salary(salary_from: Optional[int], salary_to: Optional[int]) -> str:
        if salary_from is not None and salary_to is not None:
            return f"с зарплатой от {salary_from} до {salary_to}"
        elif salary_from is not None:
            return f"с зарплатой {salary_from}"
        elif salary_to is not None:
            return f"с зарплатой {salary_to}"
        else:
            return "зарплата не была указана"

    @staticmethod
    def vacancies(data: list[dict[str, int]]) -> str:
        """Выводит основную информацию по вакансиям"""
        answer = []
        for info in data:
            salary_from = info['salary_from']
            salary_to = info['salary_to']
            salary = Formatter.format_salary(salary_from, salary_to)
            answer.append(f"В компании '{info['employer_name']}' есть следующая вакансия: {info['name']},  {salary}, "
                          f"ссылка: {info['vacancies_url']}")
        return "\n".join(answer)

    @staticmethod
    def form_avg(data: Any) -> str:
        """Выводит среднюю зарплату по вакансиям"""
        n = round(data, 2)
        return f"Средняя зарплата по вакансиям в базе данных: {n}"

    @staticmethod
    def vac_avg_salary(data: list[dict[str, int]]) -> str:
        """Выводит список вакансий с зарплатой выше средней"""
        answer = ["У следующих вакансий зарплата выше, чем средняя по всей базе данных: "]
        for info in data:
            salary_from = info['salary_from']
            salary_to = info['salary_to']
            salary = Formatter.format_salary(salary_from, salary_to)
            answer.append(f"Название: {info['name']}, компания: {info['employer']}, город: {info['city']}, {salary}, "
                          f"ссылка: {info['vacancies_url']}, дата публикации: {info['published_at']}")
        return "\n".join(answer)

    @staticmethod
    def form_vacancies_with_keyword(data: list[dict[str, int]]) -> str:
        """Выводит список вакансий по заданному слову"""
        answer = ["Следующие вакансии подходят под введенный запрос: "]
        for info in data:
            salary_from = info['salary_from']
            salary_to = info['salary_to']
            salary = Formatter.format_salary(salary_from, salary_to)
            answer.append(f"Название: {info['name']}, компания: {info['employer']}, город: {info['city']}, {salary}, "
                          f"ссылка: {info['vacancies_url']}, дата публикации: {info['published_at']}")
        return "\n".join(answer)
