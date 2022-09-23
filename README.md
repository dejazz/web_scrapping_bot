# web_scraping_bot

## Informações
<article>
    <p>Essa api foi criada com o intuito de obter todos os notebooks Lenovo do site: <a href="https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" target="_blank">WebScrap</a>. A api conta com um end-point de retorno  com o resultado da busca. </a>
</article>


<h2>Tecnologias Utilizadas</h2>

  <ul>
    <li>Linguagem utilizada: <strong>Python</strong></li>  
    <li>Para criação do bot foi utilizada a biblioteca <a href="https://playwright.dev/" target="_blank">Playwright</a></li>
    <li>Para criação de REST api foi utilizado o framework de python <a href="https://www.djangoproject.com/" target="_blank">Django</a></li>
    <li>Para conteinerização foi utilizado  <a href="https://www.docker.com/" target="_blank">Docker</a></li>
    <li>Para hospedagem do bot foi utilizado o  <a href="https://aws.amazon.com/pt/?nc2=h_lg" target="_blank">AWS EC2</a></li>
  </ul>

<h2>Base_URL</h2>

    A base url da api:
    - http://ec2-18-205-114-89.compute-1.amazonaws.com:8000
   
<h2>End-points</h2>

###  -  __End-point para busca na página inicial do site__

GET __base_url/api/scraping/__<br>
 <span>Api funcionando apenas localmente</span>
 <p>Para testar será preciso clonar o repositório e clonar as dependência do projeto. Além de necessitar rodar: playwright install</p>
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

GET __base_url/api/scraping/deep__<br>

RETORNO: __STATUS 200 OK__

	[
		{
			"description": "Lenovo V110-15IAP, 15.6\" HD, Celeron N3350 1.1GHz, 4GB, 128GB SSD, Windows 10 Home",
			"hdd_and_price": [
				{
					"128GB": "$321.94"
				},
				{
					"256GB": "$341.94"
				},
				{
					"512GB": "$361.94"
				},
				{
					"1024GB": "$381.94"
				}
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
			"hdd_and_price": [
				{
					"128GB": "$404.23"
				},
				{
					"256GB": "$424.23"
				},
				{
					"512GB": "$444.23"
				},
				{
					"1024GB": "$464.23"
				}
			],
			"price": "$404.23",
			"product_id": 557,
			"product_url": "https://webscraper.io//test-sites/e-commerce/allinone/product/557",
			"reviews": "12 reviews",
			"starts": 1,
			"title": "Lenovo ThinkPad E31-80"
		},
