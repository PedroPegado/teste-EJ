from playwright.sync_api import sync_playwright
import requests


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.uol.com.br/")
    page.click('#l1pj0alt')    
    link = page.url
    page.wait_for_timeout(3000)
    print(page.title())    
    #browser.close()
   
response = requests.get(link)
print(response.json())
