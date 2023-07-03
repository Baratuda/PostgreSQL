from csv import writer
from Clients.data_client import DataClient
import pandas as pd


class CSVClient(DataClient):
    def get_connection(self):
        pass

    def create_mebel_table(self, mebel_items=None):
       pd.DataFrame(columns=['link','price','description']).to_csv('pandadata.csv', index = False)  

    def get_items(self, conn=None, price_from=0, price_to=100000):
         data = pd.read_csv('pandadata.csv')
         print(data[(data.price >= price_from) & (data.price<=price_to)].to_markdown())

    def insert(self, link, price, description,conn=None):
        with open('pandadata.csv', 'a',encoding='utf-8',newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow([link,price,description])

