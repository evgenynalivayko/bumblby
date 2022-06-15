#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selene.support.shared import browser
from selene import by, be, have


def test_search_google():
    browser.open('https://google.com/ncr')
    browser.element(by.name('q')).should(be.blank).type('selenium').press_enter()
    browser.all('.g').first.should(have.text('Selenium'))
