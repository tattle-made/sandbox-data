from factchecking_news_sites import get_db, get_live_links, scraping_site_links, setup_driver
from factchecking_news_sites import get_post_vishvasnews, get_historical_links_vishvasnews, get_post_quint, get_historical_links_quint


url = "https://www.vishvasnews.com"
langs = ["hindi"]
domain = "vishvasnews.com/hindi"

get_historical_links_vishvasnews(url=url,domain=domain)
