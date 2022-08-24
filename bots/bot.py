from playwright.async_api import async_playwright

URL_SCRAPING = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

NOTEBOOKS_LOCATOR = ".col-sm-4.col-lg-4.col-md-4"


class BotScraping:

    lenovo_notebooks = []
    lenovo_deep_notebooks = []
    filter_item = "lenovo"
    all_notebooks = []

    async def scraping(self, deep: bool = False):

        async with async_playwright() as pw:
            browser = await pw.chromium.launch(headless=False)
            page = await browser.new_page()
            await page.goto(URL_SCRAPING)
            self.all_notebooks = await page.locator(NOTEBOOKS_LOCATOR).element_handles()
            self.lenovo_notebooks = []
            for notebook in self.all_notebooks:

                comparison_item = await notebook.query_selector(".title")
                validate_item = await comparison_item.inner_text()

                description = await notebook.query_selector(".description")
                description_item = await description.inner_text()

                if (
                    validate_item.lower().split(" ")[0] == self.filter_item
                    and description_item.lower().split(" ")[0] == self.filter_item
                ):
                    product_id = await notebook.query_selector(".title")
                    title = await notebook.query_selector(".title")
                    description = await notebook.query_selector(".description")
                    price = await notebook.query_selector(".pull-right.price")
                    reviews = await notebook.query_selector("p.pull-right")
                    starts = await notebook.query_selector_all("span")
                    product_infos = await notebook.query_selector(".title")

                    lenovo_notebook = {
                        "product_id": int(
                            str(await product_id.get_attribute("href"))[-3:]
                        ),
                        "title": await title.get_attribute("title"),
                        "description": await description.inner_text(),
                        "price": await price.inner_text(),
                        "reviews": await reviews.inner_text(),
                        "starts": int(len(starts)),
                        "product_url": f"https://webscraper.io/{await product_infos.get_attribute('href')}",
                    }

                    self.storage_elements_scraping(lenovo_notebook)

        return self.lenovo_notebooks

    def storage_elements_scraping(self, data: dict):

        self.lenovo_notebooks.append(dict(sorted(data.items())))

    async def scraping_deep(self):

        async with async_playwright() as pw:
            browser = await pw.chromium.launch()
            page = await browser.new_page()
            await page.goto(URL_SCRAPING)
            self.all_notebooks = await page.locator(NOTEBOOKS_LOCATOR).element_handles()

            for notebook in self.all_notebooks:
                price_hdd = []
                comparison_item = await notebook.query_selector(".title")
                validate_item = await comparison_item.inner_text()

                description = await notebook.query_selector(".description")
                description_item = await description.inner_text()

                if (
                    validate_item.lower().split(" ")[0] == self.filter_item
                    and description_item.lower().split(" ")[0] == self.filter_item
                ):
                    product_id = await notebook.query_selector(".title")
                    title = await notebook.query_selector(".title")
                    description = await notebook.query_selector(".description")
                    price = await notebook.query_selector(".pull-right.price")
                    reviews = await notebook.query_selector("p.pull-right")
                    starts = await notebook.query_selector_all("span")
                    product_infos = await notebook.query_selector(".title")

                    lenovo_notebook = {
                        "product_id": int(
                            str(await product_id.get_attribute("href"))[-3:]
                        ),
                        "title": await title.get_attribute("title"),
                        "description": await description.inner_text(),
                        "price": await price.inner_text(),
                        "reviews": await reviews.inner_text(),
                        "starts": int(len(starts)),
                        "product_url": f"https://webscraper.io/{await product_infos.get_attribute('href')}",
                    }

                    page_notebook = await browser.new_page()

                    await page_notebook.goto(
                        f"https://webscraper.io/{await product_infos.get_attribute('href')}"
                    )
           
                    click_page = await page_notebook.query_selector_all(".btn.swatch")
                    for hdd_bottom in click_page:
                        elem = await hdd_bottom.click()
                        price = await page_notebook.locator(
                            ".pull-right.price"
                        ).element_handle()
                        hdd = f"{await hdd_bottom.inner_text()}GB"
                        price_hdd.append({hdd:await price.inner_text()})

                    lenovo_notebook["hdd_and_price"] = price_hdd

                    self.lenovo_deep_notebooks.append(dict(sorted(lenovo_notebook.items())))

        return self.lenovo_deep_notebooks
