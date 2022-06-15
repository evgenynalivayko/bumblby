#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
в) Модифицируйте  авто-тест с помощью языка программирования python  и библиотек selenium, pytest

Для работы теста необходимо установить
python3.8

Библиотеки
pytest
selene==2.0.0b1
selenium==4.1.0
requests

Запуск теста

pytest test_auth.py

В тесте сломан один из локаторов
Нужно починить

Используйте свой логин/пароль вместо XXX
"""


from selene.support.shared import browser
from selene import have


def test_auth_bumbleby():
    browser.open("https://bumbleby.ru")
    browser.element("/html/body/div/div/div/section/div[2]/div/div/div/form/div[1]/div[1]/div/input").type("XXX")
    browser.element('//*[@id="__layout"]/div/section/div[1]/div[2]/div/input').type("XXX")
    browser.element(".btn.fill").click()
    browser.element('//*[@id="__layout"]/div/div[3]/div/section/div[1]/h2').should(have.text("Расписание"))
    browser.element('.scrollmenu').click()
    browser.element('.logout').click()

