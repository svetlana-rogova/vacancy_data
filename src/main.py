from config import config
from src.create_database import create_database
from src.DBManager import DBManager
from src.formatter import Formatter
from src.getting_data_API import getting_data
from src.save_data_to_database import save_data_to_database


def main() -> str:
    params = config()
    create_database("hh_vacancies", params)
    employers_ids = [
        "1440683",  # Rutube
        "841097",  # АО НИИ МАСШТАБ
        "913476",  # Aston
        "11545313",  # ООО СП Солюшен
        "3513136",  # ООО ТЕХНОЛОГИИ ОТРАСЛЕВОЙ ТРАНСФОРМАЦИИ
        "9904744",  # АО Консалт Плюс
        "4596113",  # ООО Фабрика Решений
        "3125",  # QIWI
        "1567355",  # ООО Айкомплекс
        "9311920",  # DNS Технологии
    ]
    data = getting_data(employers_ids)

    save_data_to_database(data, "hh_vacancies", params)

    bd = DBManager(params, "hh_vacancies")
    form = Formatter()
    while True:
        answer = input(
                "Была создана база данных с вакансиями по 10 компаниям.\n"
                "Вы можете выбрать несколько вариантов вывода информации из данной БД:\n"
                "Чтобы получить список всех компаний и количество вакансий у каждой компании введите 1,\n"
                "Чтобы получить список всех вакансий с указанием названия компании, названия вакансии, зарплаты и "
                "ссылки на вакансию введите 2,\n"
                "Чтобы получить среднюю зарплату по всем вакансиям из БД введите 3,\n"
                "Чтобы получить список всех вакансий, у которых зарплата выше средней по всем вакансиям введите 4,\n"
                "Чтобы получить список вакансий по выбранному Вами слову введите 5\n"
         )
        if answer == "1":
            return form.companies(bd.get_companies_and_vacancies_count())
        elif answer == "2":
            return form.vacancies(bd.get_all_vacancies())
        elif answer == "3":
            return form.form_avg(bd.get_avg_salary())
        elif answer == "4":
            return form.vac_avg_salary(bd.get_vacancies_with_higher_salary())
        elif answer == "5":
            word = input("Введите слово для поиска по списку вакансий")
            return form.form_vacancies_with_keyword(bd.get_vacancies_with_keyword(word))
        else:
            print("Некорректный ввод, пожалуйста, выберите цифру от 1 до 5")


if __name__ == "__main__":
    print(main())
