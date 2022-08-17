def create(all_items: list,browser):
    lenovo_notebooks = []
    for notebook in all_items:

        filter_notebook = "lenovo"

        if (
            notebook.query_selector(".title").inner_text().lower().split(" ")[0]
            == filter_notebook
        ):

            notebook_item = {
                "title": notebook.query_selector(".title").get_attribute("title"),
                "description": notebook.query_selector(".description").inner_text(),
                "price": notebook.query_selector(".pull-right.price").inner_text(),
                "reviews": notebook.query_selector("p.pull-right").inner_text(),
                "starts": int(len(notebook.query_selector_all("span"))),
                "product_infos": f"https://webscraper.io/{notebook.query_selector('.title').get_attribute('href')}",
            }

            page_notebook = browser.new_page()
            page_notebook.goto(
                f"https://webscraper.io/{notebook.query_selector('.title').get_attribute('href')}"
            )

            notebooks = page_notebook.locator(".btn.swatch").element_handles()

            notebook_item["hdd"] = [f"{hdd.inner_text()}GB" for hdd in notebooks]
            notebook_item["hdd_unavailable"] = [
                f"{hdd_unavailable.inner_text()}GB" for hdd_unavailable in notebooks
            ]
            lenovo_notebooks.append(dict(sorted(notebook_item.items())))
    return lenovo_notebooks