# Sku-Aggregator
Aggregator app that scrapes products from different sites regularly, store these products in database and show them to users with different filters.

# Technology Used:
<li>Python3</li>
<li>Django Rest Framework</li>
<li>Celery</li>
<li>Postgresql</li>
<li>RabbitMQ</li>
<li>Scrapy</li>
<li>Javascript</li>
<li>React</li>
<li>Redux</li>
<li>Docker</li>

# How does it work
Sku-aggregator app is created using django, scrapy and react . While django and drf are used to create apis for crud operations and filtering of product items. Using Celerybeat to schedule scrapping jobs which put them into RabbitMQ queues, from where celery worker picks up and executes the job. As soon as the celery worker runs scrapper, the sites are scrapped by the spider and data is processed and added to database by the scrapy pipelines using the APIs. The frontend App is create using React Js and redux (for state management). The react app provides listing, filtering, searching and detailview options. Finally, the app is containerized using docker-compose, and hosted on heroku.

# How do i get setup:
Just clone the repository and run docker-compose up. And you are good to go.

# App Links:
Link to frontend app: https://young-spire-23991.herokuapp.com/

Link to django admin: https://sku-aggregator.herokuapp.com/admin
