#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports' function so that it returns a list of airport
codes, excluding any combinations like "All".
"""

from bs4 import BeautifulSoup
html_page = "options.html"


def extract_airports(page):
    data = []
    skip=['All','AllUS','AllForeign','AllMajors','AllOthers']
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        tags=soup.find('select',{'id':'AirportList'}).children
        count=0
#        print len(tags)
        for tag in tags:

            try:
    #            print tag['value']
                if tag['value'] in skip:
    #                print '1'
                    continue
                else:
                    data.append(tag['value'])

            except:
#                print '2'
                continue

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

test()
