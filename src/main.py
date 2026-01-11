from src.getting_data_API import getting_data
from src.save_data_to_database import save_data_to_database
from config import config
from src.create_database import create_database


def main() -> None:
    params = config()
    create_database('hh_vacancies', params)
    employers_ids = [
        "1440683",  # Rutube
        "841097",  # АО НИИ МАСШТАБ
        "6093775",  # Aston
        "11545313",  # ООО СП Солюшен
        "3513136",  # ООО ТЕХНОЛОГИИ ОТРАСЛЕВОЙ ТРАНСФОРМАЦИИ
        "9904744",  # АО Консалт Плюс
        "4596113",  # ООО Фабрика Решений
        "3125",  # QIWI
        "1567355",  # ООО Айкомплекс
        "9311920"  # DNS Технологии
    ]
    data = getting_data(employers_ids)

    save_data_to_database(data, 'hh_vacancies', params)


if __name__ == "__main__":
    main()
