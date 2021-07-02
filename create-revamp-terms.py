import requests
import json

access_jwt = requests.post(
    "https://backend.rev-amp.tech/api/v1/login/access-token",
    data={"username": "test@rev-amp.tech", "password": "INSERT-PASSWORD-HERE"},
).json()["access_token"]

years = requests.get(
    "https://backend.rev-amp.tech/api/v1/years/",
    headers={"Authorization": f"Bearer {access_jwt}"},
).json()

for year in years:
    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/terms/",
        json={
            "year_id": year["id"],
            "current_year_term": 1,
            "school_id": year["school_id"],
            "has_electives": False,
            "start_date": f"{year['start_year']}-07-10",
            "end_date": f"{year['start_year']}-10-20",
            "name": f"Term 1, {year['start_year']} - {year['end_year']}",
        },
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())

    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/terms/",
        json={
            "year_id": year["id"],
            "current_year_term": 2,
            "school_id": year["school_id"],
            "has_electives": False,
            "start_date": f"{year['start_year']}-11-10",
            "end_date": f"{year['end_year']}-02-10",
            "name": f"Term 2, {year['start_year']} - {year['end_year']}",
        },
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())

    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/terms/",
        json={
            "year_id": year["id"],
            "current_year_term": 3,
            "school_id": year["school_id"],
            "has_electives": False,
            "start_date": f"{year['end_year']}-03-10",
            "end_date": f"{year['end_year']}-6-05",
            "name": f"Term 3, {year['start_year']} - {year['end_year']}",
        },
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())
