#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def test_auth():
    url = "https://api.bumbleby.ru/graphql"
    payload = {
    "operationName": "signIn",
    "variables": {
        "email": "nalivayko.ev@gmail.com",
        "password": "Aa123456"
    },
    "query": "mutation signIn($email: String!, $password: String!) {\n  signIn(email: $email, password: $password) {\n    success\n    errors {\n      message\n      field\n      __typename\n    }\n    student {\n      ...studentData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment studentData on Student {\n  firstName\n  middleName\n  avatar {\n    id\n    name\n    url\n    contentType\n    __typename\n  }\n  secondName\n  token\n  birthday\n  email\n  phone\n  sex\n  userAddress\n  certificationPassed\n  category {\n    id\n    name\n    __typename\n  }\n  groups {\n    id\n    name\n    groupCourse {\n      id\n      schedule\n      startsAt\n      endsAt\n      course {\n        id\n        title\n        description\n        durationHours\n        logoUrl\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n"
    }

    response = requests.request(method="POST", url=url, json=payload)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["data"]["signIn"]["student"]["token"] is not None
    assert type(response_json["data"]["signIn"]["student"]["token"]) is str
