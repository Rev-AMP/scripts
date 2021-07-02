import requests
import json
from names import get_full_name

access_jwt = requests.post(
    "https://backend.rev-amp.tech/api/v1/login/access-token",
    data={"username": "test@rev-amp.tech", "password": "INSERT-PASSWORD-HERE"},
).json()["access_token"]

courses = requests.get(
    "https://backend.rev-amp.tech/api/v1/courses/",
    headers={"Authorization": f"Bearer {access_jwt}"},
).json()

for course in courses:
    if course["term"]["year"]["start_year"] != 2020:
        continue
    name = get_full_name()
    user_details = {
        "full_name": name,
        "password": "INSERT-PASSWORD-HERE",
        "type": "professor",
        "email": f"test+{name.replace(' ', '')}@rev-amp.tech",
        "school_id": "38b357f2-71ef-49de-986e-6f2d2c1f1d02",
        "is_admin": False,
    }
    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/users/",
        json=user_details,
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())
    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/divisions/",
        json={
            "professor_id": response.json()["id"],
            "division_code": 1,
            "course_id": course["id"],
        },
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.json(), response.status_code)
