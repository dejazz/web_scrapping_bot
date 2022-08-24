from playwright.async_api import async_playwright
import asyncio

URL_SCRAPING = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

NOTEBOOKS_LOCATOR = ".col-sm-4.col-lg-4.col-md-4"


async def main():
    all_notebooks = []
    filter_item = "lenovo"
    lenovo_deep_notebooks = []
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(URL_SCRAPING)
        all_notebooks = await page.locator(NOTEBOOKS_LOCATOR).element_handles()

        for notebook in all_notebooks:

            comparison_item = await notebook.query_selector(".title")
            validate_item = await comparison_item.inner_text()

            description = await notebook.query_selector(".description")
            description_item = await description.inner_text()

            if (
                validate_item.lower().split(" ")[0] == filter_item
                and description_item.lower().split(" ")[0] == filter_item
            ):
                product_id = await notebook.query_selector(".title")
                title = await notebook.query_selector(".title")
                description = await notebook.query_selector(".description")
                price = await notebook.query_selector(".pull-right.price")
                reviews = await notebook.query_selector("p.pull-right")
                starts = await notebook.query_selector_all("span")
                product_infos = await notebook.query_selector(".title")

                lenovo_notebook = {
                    "product_id": int(str(await product_id.get_attribute("href"))[-3:]),
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

                storages = await page_notebook.locator(".btn.swatch").element_handles()

                storages_unavailable = await page_notebook.locator(
                    ".btn.swatch.disabled"
                ).element_handles()

                lenovo_notebook["hdd"] = [
                    f"{await hdd.inner_text()}GB" for hdd in storages
                ][:-1]

                lenovo_notebook["hdd_unavailable"] = [
                    f"{await hdd_unavailable.inner_text()}GB"
                    for hdd_unavailable in storages_unavailable
                ]

                price_hdd = []
                click_page = await page_notebook.query_selector_all(".btn.swatch")
                for hdd_bottom in click_page:
                    elem = await hdd_bottom.click()
                    price = await page_notebook.locator(
                        ".pull-right.price"
                    ).element_handle()

                    price_hdd.append(f'{await price.inner_text()},00')

                lenovo_notebook["price_hdd_availability"] = price_hdd[:-3]
                lenovo_notebook["price_hdd_avaibility"] = price_hdd[-3:]

                lenovo_deep_notebooks.append(dict(sorted(lenovo_notebook.items())))
    return lenovo_deep_notebooks


if __name__ == "__main__":
    result = asyncio.run(main())
    print(result)
