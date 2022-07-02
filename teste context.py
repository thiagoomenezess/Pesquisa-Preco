from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    context2 = browser.new_context()
    page_two = context2.new_page()

    page_two.goto("https://www.terabyteshop.com.br/")
    page_two.fill('//input[@id="isearch"]', "Rtx 3080")




    context1 = browser.new_context()
    page_one = context1.new_page()

    page_one.goto("https://www.kabum.com.br/")
    page_one.fill('//form[@action="/busca"]/input', "Rtx 3070")

    time.sleep(999)







