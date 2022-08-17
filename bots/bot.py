from playwright.sync_api import sync_playwright
from utils.create_dict import create

class BotScraping():

    def scraping():
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(
                "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
            )
            all_notebooks = page.locator(".col-sm-4.col-lg-4.col-md-4").element_handles()

            all_lenovo_notebooks = []

            response = create(all_notebooks)
            all_lenovo_notebooks.append(response)
            return all_lenovo_notebooks

