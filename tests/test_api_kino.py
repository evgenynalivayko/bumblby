#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def test_check_film():
    url = "https://kinopoiskapiunofficial.tech/api/v2.2/films/premieres?year=2021&month=JANUARY"
    payload = {}
    headers = {'X-API-KEY': '29cf32dd-c7ca-4298-ae1b-ed6f5d47a191'}
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["total"] == 39
    assert response_json["items"][0]["kinopoiskId"] == 1249172

