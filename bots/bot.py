from playwright.sync_api import sync_playwright
from utils.create_dict import create_dict

class BotScraping():

    def scraping(self):
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto(
                "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
            )
            all_notebooks = page.locator(".col-sm-4.col-lg-4.col-md-4").element_handles()

            response = create_dict(all_notebooks,browser=browser)

            return response

