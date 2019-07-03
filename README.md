# Web-Scrapper

## Srapping Quotes from Website
Basic web scrapper using scappy python which scrapped quotes from multiple pages of 'http://quotes.toscrape.com'



## Amazon Scrapper 
Scrapped following Mobile details 
1. Name
2. Price
3. Image
4. No of Reviews 
After Extraction These details were stored in Product.json file


### Technology Stack
Pycharm 
Scrapy = 1.6.0
pypiwin32 = 224
scrapy-user-agents = 0.1.1


### Build Instructions
#### In terminal Window write scrapy crawl amazon_spider -o Product.json. 



To prevent Amazon from blocking you, you could use the following tricks to bypass their security measures.

GoogleBot - Confuse the site by faking your user-agent to be google's bot agent. Amazon allows access to google to crawl it's website. Add the code to your settings.py -> USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'

Rotating User-Agents and Spoofing - Spoof the User Agent by creating a list of user agents and picking a random one for each request. Websites do not want to block genuine users so you should try to look like one. Add the code to your settings.py -> DOWNLOADER_MIDDLEWARES = { 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None, 'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400, }

Rotating IPs and Proxy Services - Use different IP addresses for making requests to a server, so that the detection becomes harder. Create a pool of IPs that you can use and use random ones for each request. We can use VPNs, shared proxies for the same.




