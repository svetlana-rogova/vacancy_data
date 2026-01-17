from unittest.mock import MagicMock


def test_get_companies_and_vacancies_count(db_manager_with_cursor):
    manager, cursor = db_manager_with_cursor
    cursor.description = [
        ("employer_name",),
        ("vacancies_count",),
    ]
    cursor.fetchall.return_value = [
        ("Company A", 5),
        ("Company B", 2),
    ]
    result = manager.get_companies_and_vacancies_count()
    assert result == [
        {"employer_name": "Company A", "vacancies_count": 5},
        {"employer_name": "Company B", "vacancies_count": 2},
    ]


def test_get_all_vacancies(db_manager_with_cursor):
    manager, cursor = db_manager_with_cursor
    cursor.description = [
        ("employer_name",),
        ("name",),
        ("salary_from",),
        ("salary_to",),
        ("vacancies_url",),
    ]
    cursor.fetchall.return_value = [
        ("Company A", "Python dev", 100000, 150000, "http://test"),
    ]
    result = manager.get_all_vacancies()
    assert result == [
        {
            "employer_name": "Company A",
            "name": "Python dev",
            "salary_from": 100000,
            "salary_to": 150000,
            "vacancies_url": "http://test",
        }
    ]


def test_get_avg_salary(db_manager_with_cursor):
    manager, cursor = db_manager_with_cursor
    cursor.fetchall.return_value = [(120000,)]
    result = manager.get_avg_salary()
    assert result == 120000


def test_get_vacancies_with_higher_salary(db_manager_with_cursor):
    manager, cursor = db_manager_with_cursor
    manager.get_avg_salary = MagicMock(return_value=100000)
    cursor.description = [
        ("vacancies_id",),
        ("name",),
        ("salary_from",),
    ]
    cursor.fetchall.return_value = [
        (1, "Senior Python", 150000),
    ]
    result = manager.get_vacancies_with_higher_salary()
    assert result == [
        {
            "vacancies_id": 1,
            "name": "Senior Python",
            "salary_from": 150000,
        }
    ]


def test_get_vacancies_with_keyword(db_manager_with_cursor):
    manager, cursor = db_manager_with_cursor
    cursor.description = [("name",)]
    cursor.fetchall.return_value = [("Python developer",)]
    result = manager.get_vacancies_with_keyword("python")
    assert result == [{"name": "Python developer"}]
