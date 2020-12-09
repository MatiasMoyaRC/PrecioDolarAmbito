import scraper
import saver
import crawler

HOME_URL = "https://www.ambito.com/contenidos/dolar.html"


def run():
    headless = True
    crawler_obj = crawler.Crawler("chrome", headless)
    driver = crawler_obj.create_driver()
    crawler_obj.crawl(driver, HOME_URL)
    scrap = scraper.Scraper()
    precios_dic = scrap.crear_dic(driver)
    save_in = saver.DataB("Dolar_Historico.csv")
    save_in.save_csv(precios_dic)
    driver.quit()


if __name__ == '__main__':
    run()
