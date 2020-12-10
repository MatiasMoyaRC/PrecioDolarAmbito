# -*- coding: utf-8 -*-
import scraper
import saver
import crawler
from datetime import datetime

HOME_URL = "https://www.ambito.com/contenidos/dolar.html"


def run():
    timestamp = datetime.now().strftime("%H:%M:%S")
    print("{} - Start crawling".format(timestamp))
    headless = True
    crawler_obj = crawler.Crawler(headless)
    driver = crawler_obj.create_driver()
    crawler_obj.crawl(driver, HOME_URL)
    scrap = scraper.Scraper()
    timestamp = datetime.now().strftime("%H:%M:%S")
    print("{} - Start Scraping".format(timestamp))
    precios_dic = scrap.crear_dic(driver)
    save_in = saver.DataB("Dolar_Historico.csv")
    save_in.save_csv(precios_dic)
    driver.quit()
    timestamp = datetime.now().strftime("%H:%M:%S")
    print("{} - Saved".format(timestamp))


if __name__ == '__main__':
    run()
