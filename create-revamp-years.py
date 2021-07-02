from random import choice
import requests

access_jwt = requests.post(
    "https://backend.rev-amp.tech/api/v1/login/access-token",
    data={"username": "test@rev-amp.tech", "password": "INSERT-PASSWORD-HERE"},
).json()["access_token"]

school_ids = [
    ("4786c637-78a6-4c4f-a1a0-c1824bfeb710", "School of Mechanical Engineering"),
    (
        "38b357f2-71ef-49de-986e-6f2d2c1f1d02",
        "School of Computer Engineering & Technology",
    ),
    (
        "06f40d54-de9b-4d2e-b599-8c6c4fe87cf0",
        "School of Electronics & Communication Engineering",
    ),
    ("6b7cf0c7-3a69-4b9b-9321-9b1468742034", "School of Civil Engineering"),
    ("065680be-ad4e-4d38-bac1-44641ea3875a", "School of Electrical Engineering"),
    ("f7e62a4d-55d5-4f3c-902a-c556dcae65bd", "School of Chemical Engineering"),
    ("250d0043-8be5-4db6-8e6a-9efabe5fb3d1", "School of Polymer Engineering"),
    ("401dcf8f-d6cc-4a4d-bd3c-33a9f90a5f43", "School of Petroleum Engineering"),
    ("ad35aa3d-12db-41e0-8cd0-98dd9741be56", "School of Peace"),
]

data = ((2017, 2018), (2018, 2019), (2019, 2020), (2020, 2021))

for school_id, school_name in school_ids:
    for start, end in data:
        response = requests.post(
            "https://backend.rev-amp.tech/api/v1/years/",
            json={
                "start_year": start,
                "end_year": end,
                "school_id": school_id,
                "name": f"{start} - {end}, {school_name}",
            },
            headers={"Authorization": f"Bearer {access_jwt}"},
        )
        print(response.status_code, response.json())
