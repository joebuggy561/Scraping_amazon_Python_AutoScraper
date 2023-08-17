from autoscraper import AutoScraper

search = "Computer+Tablets"
amazon_url = 'https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A13896617011&ref=nav_em__nav_desktop_sa_intl_computers_tablets_0_2_6_4'

wanted_list = ["$783.63", "Acer Nitro 5 AN515-58-57Y8 Gaming Laptop | Intel Core i5-12500H | NVIDIA GeForce RTX 3050 Ti Laptop GPU | 15.6", "89"]

scraper = AutoScraper()

result = scraper.build(amazon_url, wanted_list)

print(scraper.get_result_similar(amazon_url, grouped=True))


