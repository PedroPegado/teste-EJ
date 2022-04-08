from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    nav = p.chromium.launch(headless=False)
    page = nav.new_page
    page.goto('http://google.com.br')

