import csv
import os

FILE_NAME = "Dolar_Historico.csv"


class DataB:

    def __init__(self, file_name):
        self.__file_name = file_name

    def save_csv(self, precios_dic):
        with open('{}'.format(self.__file_name), 'a+', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=precios_dic.keys())

            if os.stat(FILE_NAME).st_size == 0:
                writer.writeheader()

            writer.writerow(precios_dic)
