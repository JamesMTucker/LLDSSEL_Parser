# -*- encoding: utf-8 -*-

import time
import os
import csv
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup


def get_source(siglum):
    """
    Get HTML source for siglum
    """

    # The LLDSSEL adds "-1" to a siglum
    siglum = siglum + "-1"

    browser = webdriver.Chrome()
    browser.get("https://www.deadseascrolls.org.il/explore-the-archive/manuscript/" + siglum)

    print("Opening Google Chrome at " + siglum + " to dowload …")
    time.sleep(5)

    # Get HTML Source
    html = browser.page_source

    # Pass HTML to soup
    soup = BeautifulSoup(html, "lxml")

    # JavaScript unloads the images for a given siglum. PAMs are last images.
    refresh_times = soup.find("div", class_="c-search-page__status")



