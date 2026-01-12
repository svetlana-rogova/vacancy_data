from typing import Any

import requests


def getting_data(employers_ids: list) -> list[dict[str, Any]]:
    data = []
    for employer_id in employers_ids:
        employer_url = f"https://api.hh.ru/employers/{employer_id}"
        response = requests.get(employer_url)
        if response.status_code != 200:
            print(f"Произошла ошибка. Статус-код: {response.status_code}")
            continue
        employers = response.json()

        vacancies = []
        page = 0
        while True:
            vacancies_url = "https://api.hh.ru/vacancies"
            params = {"employer_id": employer_id, "per_page": 100, "page": page}
            response_vac = requests.get(vacancies_url, params=params)
            if response_vac.status_code != 200:
                print(f"Произошла ошибка. Статус-код: {response_vac.status_code}")
                continue

            vac = response_vac.json()
            vacancies.extend(vac["items"])

            if page >= vac["pages"] - 1:
                break
            page += 1

        data.append(
            {
                "employers": {
                    "id": employers["id"],
                    "name": employers["name"],
                    "site_url": employers["site_url"],
                    "city": employers["area"]["name"],
                    "open_vacancies": employers["open_vacancies"],
                },
                "vacancies": vacancies,
            }
        )
    return data
