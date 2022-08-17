# web_scraping_bot

## Informações

    Essa api foi criada com o intuito de obter todos os notebooks Lenovo do site: https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops.  Essa api conta com dois end-points de retorno do que o bot encontrou. Sendo o primeiro a ocorrência de todas as informações de cada notebook Lenovo na página geral dos produtos. E o segundo end-point o bot trás também as informação da página individual de cada notebook.
## Base_URL

    A base url da api:
    - ......


## END-POINTS

###  -  __End-point para busca na página inicial do site__

__GET base_url/api/scraping/__<br>
   

RETORNO: __STATUS 200 OK__


    [
        {
            "description": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",<br>
            "price": "$321.94",
            "product_id": 548,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/548",
            "reviews": "5 reviews",
            "starts": 3,
            "title": "Lenovo V110-15IAP"
        },
        {
            "description": "Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home",
            "price": "$404.23",
            "product_id": 557,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/557",
            "reviews": "12 reviews",
            "starts": 1,
            "title": "Lenovo ThinkPad E31-80"
        },
        {
            "description": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 8GB, 128GB SSD, Windows 10 Home",
            "price": "$409.63",
            "product_id": 559,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/559",
            "reviews": "9 reviews",
            "starts": 3,
            "title": "Lenovo V110-15ISK"
        },
        {
            "description": "Lenovo V110-15ISK, 15.6\" HD, Core i3-6006U, 4GB, 128GB SSD, Windows 10 Pro",
            "price": "$454.73",
            "product_id": 567,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/567",
            "reviews": "2 reviews",
            "starts": 2,
            "title": "Lenovo V110-15ISK"
        },

        ...

        ]

RETORNO 404 NOT FOUND:

    {
        "Detail": "site not found"
    }

###  -  __End-point para busca individual de cada produto__


__GET base_url/api/scraping/deep__<br>
   

RETORNO: __STATUS 200 OK__


    [
        {
            "description": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
            "hdd": [
                "128GB",
                "256GB",
                "512GB"
            ],
            "hdd_unavailable": [
                "1024GB"
            ],
            "price": "$321.94",
            "product_id": 548,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/548",
            "reviews": "5 reviews",
            "starts": 3,
            "title": "Lenovo V110-15IAP"
        },
        {
            "description": "Lenovo ThinkPad E31-80, 13.3\" HD, Celeron 3855U 1.6GHz, 4GB, 128GB SSD, Windows 10 Home",
            "hdd": [
                "128GB",
                "256GB",
                "512GB"
            ],
            "hdd_unavailable": [
                "1024GB"
            ],
            "price": "$404.23",
            "product_id": 557,
            "product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/557",
            "reviews": "12 reviews",
            "starts": 1,
            "title": "Lenovo ThinkPad E31-80"
        },

        ...

        ]
        
RETORNO 404 NOT FOUND:

    {
        "Detail": "site not found"
    }

