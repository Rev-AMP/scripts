#!/usr/bin/env python3

from names import get_full_name
from random import randint
import requests


def create_admin(give_full_perms: bool):
    name = get_full_name()
    user_details = {
        "full_name": name,
        "password": "INSERT-PASSWORD-HERE",
        "type": "admin",
        "email": f"test+{name.replace(' ', '')}@rev-amp.tech",
        "school_id": school_id,
    }
    response = requests.post(
        "https://backend.rev-amp.tech/api/v1/users/",
        json=user_details,
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())

    permission_details = {
        "user_id": response.json().get("id"),
        "permissions": 255 if give_full_perms else randint(0, 256),
    }
    response = requests.put(
        "https://backend.rev-amp.tech/api/v1/admins/",
        json=permission_details,
        headers={"Authorization": f"Bearer {access_jwt}"},
    )
    print(response.status_code, response.json())


access_jwt = requests.post(
    "https://backend.rev-amp.tech/api/v1/login/access-token",
    data={"username": "test@rev-amp.tech", "password": "INSERT-PASSWORD-HERE"},
).json()["access_token"]

school_ids = [
    "4786c637-78a6-4c4f-a1a0-c1824bfeb710",
    "38b357f2-71ef-49de-986e-6f2d2c1f1d02",
    "06f40d54-de9b-4d2e-b599-8c6c4fe87cf0",
    "6b7cf0c7-3a69-4b9b-9321-9b1468742034",
    "065680be-ad4e-4d38-bac1-44641ea3875a",
    "f7e62a4d-55d5-4f3c-902a-c556dcae65bd",
    "250d0043-8be5-4db6-8e6a-9efabe5fb3d1",
    "401dcf8f-d6cc-4a4d-bd3c-33a9f90a5f43",
    "ad35aa3d-12db-41e0-8cd0-98dd9741be56",
]
for school_id in school_ids:
    for i in range(2):
        print(f"Creating admin {i+1} for {school_id}")
        create_admin(False)
    create_admin(True)
