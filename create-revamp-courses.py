import requests
import json

access_jwt = requests.post(
    "https://backend.rev-amp.tech/api/v1/login/access-token",
    data={"username": "test@rev-amp.tech", "password": "INSERT-PASSWORD-HERE"},
).json()["access_token"]

terms = requests.get(
    "https://backend.rev-amp.tech/api/v1/terms/",
    headers={"Authorization": f"Bearer {access_jwt}"},
).json()

courses = (
    ("Cloud Computing", "CSP42B"),
    ("High Performance Computing", "CS324"),
    ("Web Technology", "CS325"),
    ("Database Management System", "CS312"),
    ("Indian Tradition, Culture and Heritage", "WPC5"),
)
for term in terms:
    if term["year"]["school"]["id"] != "38b357f2-71ef-49de-986e-6f2d2c1f1d02":
        continue
    for name, code in courses:
        response = requests.post(
            "https://backend.rev-amp.tech/api/v1/courses/",
            json={
                "name": name,
                "course_code": code,
                "term_id": term["id"],
            },
            headers={"Authorization": f"Bearer {access_jwt}"},
        )
        print(response.json(), response.status_code)
