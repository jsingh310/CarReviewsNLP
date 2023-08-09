import os,nltk,csv
import pandas as pd
from bs4 import BeautifulSoup
#import bs4
nltk.download('vader_lexicon')

data_path = 'cars/data/'

df_07 = pd.read_csv(data_path + '2007.csv')
df_08 = pd.read_csv(data_path + '2008.csv')
df_09 = pd.read_csv(data_path + '2009.csv')

#save name of each doc file into a list to pass into function below
doc_files_2007 = [os.path.join(data_path + '2007/', file)[15:]  for file in os.listdir(data_path + '2007/')]
doc_files_2008 = [os.path.join(data_path + '2008/', file)[15:]  for file in os.listdir(data_path + '2008/')]
doc_files_2009 = [os.path.join(data_path + '2009/', file)[15:]  for file in os.listdir(data_path + '2009/')]

def doc_to_csv(year,file_name):
    data_file_path = data_path + str(year) + '/' + file_name
    
    #loading data from the data file in text format
    with open(data_file_path, encoding='latin-1') as txt_file:
        data = txt_file.read()
    #using Beautiful soup to get the data into html format
    soup = BeautifulSoup(data, 'lxml')
    #taking list to load the data into csv format
    csv_data = []
    #headers for the csv format
    csv_data.append(["date","author","text","favorite"])
    #finding and printing the data of "doc" format
    for doc_tag in soup.find_all("doc"):
        #loading data in list to append the cummulated data to upper list
        raw_data = []
        #getting each values for a respective doc tag
        raw_data.append(doc_tag.find("date").text)
        raw_data.append(doc_tag.find("author").text)
        raw_data.append(doc_tag.find("text").text)
        raw_data.append(doc_tag.find("favorite").text)
        csv_data.append(raw_data)
    
    review_data = pd.DataFrame(csv_data[1:],columns=csv_data[0])
    review_data.insert(1,'doc_id',file_name)
    review_data.to_csv(data_path + str(year) + '/' + file_name + '.csv',index=False)
    
if __name__ == '__main__':

    for file in doc_files_2007:
        doc_to_csv(2007,str(file))
        
    test = pd.read_csv(data_path + '2007/2007_mercedes-benz_e-class.csv')
        
    for file in doc_files_2008:
        doc_to_csv(2008,str(file))
    
    for file in doc_files_2009:
        doc_to_csv(2008,str(file))

