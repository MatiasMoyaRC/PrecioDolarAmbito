from datetime import datetime


class Scraper:

    def __init__(self):
        self.XPATH_DOLAR_OFICIAL_COMPRA = '//div[@data-indice="/dolar/oficial"]//span[@class="value data-compra"]'
        self.XPATH_DOLAR_OFICIAL_VENTA = '//div[@data-indice="/dolar/oficial"]//span[@class="value data-venta"]'
        self.XPATH_DOLAR_TURISTA = '//div[@data-indice="/dolarturista"]//span[@class="value data-valor"]'
        self.XPATH_DOLAR_INFORMAL_COMPRA = '//div[@data-indice="/dolar/informal"]//span[@class="value data-compra"]'
        self.XPATH_DOLAR_INFORMAL_VENTA = '//div[@data-indice="/dolar/informal"]//span[@class="value data-venta"]'

    def crear_dic(self, driver):
        try:
            dolar_turista = driver.find_element_by_xpath(self.XPATH_DOLAR_TURISTA)
            dolar_oficial_c = driver.find_element_by_xpath(self.XPATH_DOLAR_OFICIAL_COMPRA)
            dolar_oficial_v = driver.find_element_by_xpath(self.XPATH_DOLAR_OFICIAL_VENTA)
            dolar_blue_c = driver.find_element_by_xpath(self.XPATH_DOLAR_INFORMAL_COMPRA)
            dolar_blue_v = driver.find_element_by_xpath(self.XPATH_DOLAR_INFORMAL_VENTA)
            today = datetime.today().strftime("%d/%m/%Y, %H:%M:%S")

            precios_dic = {
                "TimeStamp": today,
                "OficialCompra": dolar_oficial_c.text,
                "OficialVenta": dolar_oficial_v.text,
                "Turista": dolar_turista.text,
                "BlueCompra": dolar_blue_c.text,
                "BlueVenta": dolar_blue_v.text
            }
            driver.quit()
            return precios_dic
        except ValueError as ve:
            print(ve)
