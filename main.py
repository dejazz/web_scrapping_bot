from playwright.async_api import async_playwright
from utils.create_dict import create_dict
import asyncio

async def main(deep=False):
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto(
            "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
        )
        all_notebooks = await page.locator(
            ".col-sm-4.col-lg-4.col-md-4"
        ).element_handles()

        lenovo_notebooks = []
        for notebook in all_notebooks:
            lenovo_notebook = {}
            filter_item = 'lenovo'
            comparison_item = await notebook.query_selector('.title')
            validate_item = await comparison_item.inner_text()


            if validate_item.lower().split(" ")[0] == filter_item:
                
                product_id = await notebook.query_selector('.title')

                lenovo_notebook['product_id'] = int(str(await product_id.get_attribute('href'))[-3:]
                title = await notebook.query_selector('.title')
                lenovo_notebook['title'] = await title.get_attribute('title')

                description = await notebook.query_selector(".description")
                lenovo_notebook['description'] = await description.inner_text()
                
                price = await notebook.query_selector(".pull-right.price")
                lenovo_notebook['price'] = await  price.inner_text()

                reviews = await notebook.query_selector("p.pull-right")
                lenovo_notebook['reviews'] = await  reviews.inner_text()
                
                starts = await notebook.query_selector_all("span")
                lenovo_notebook['reviews'] =  int(len(starts)) 

                product_infos = await notebook.query_selector('.title')
                lenovo_notebook['product_url'] =  f"https://webscraper.io/{await product_infos.get_attribute('href')}"
                
                if deep :
                    page_notebook = await browser.new_page()
        
                    await page_notebook.goto(
                        f"https://webscraper.io/{await product_infos.get_attribute('href')}"
                    )

                    storages = await page_notebook.locator(".btn.swatch").element_handles()
                    storages_unavailable = await page_notebook.locator(".btn.swatch.disabled").element_handles()

                    lenovo_notebook["hdd"] = [f"{await hdd.inner_text()}GB" for hdd in storages]
                    lenovo_notebook["hdd_unavailable"] = [
                        f"{await hdd_unavailable.inner_text()}GB" for hdd_unavailable in storages_unavailable
                    ]
                    lenovo_notebooks.append(dict(sorted(lenovo_notebook.items())))


                lenovo_notebooks.append(dict(sorted(lenovo_notebook.items())))

        print(lenovo_notebooks[0])
        print(len(lenovo_notebooks))
        return lenovo_notebooks

if __name__ == '__main__':
    asyncio.run(main())
  