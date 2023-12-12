from bs4 import BeautifulSoup
import time
from selenium import webdriver
import pandas as pd

#link do site
url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars'

#coloque o endereço do chromedriver do seu computador
servico = webdriver.ChromeService(executable_path='C:\chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=servico)
driver.get(url)

#tempo que o navegador mostrará o site
time.sleep(2)

#cria a lista das estrelas mais brilhantes


def scrape():
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    #localize a tabela <table> com a classe jquery-tablesorter
    
    #nessa tabela, encontre o tbody
    
    #nesse tbody, encontre todas as linhas <tr> e adicione na variavel
    

    #para cada uma das linhas, encontre as colunas
    
        #add as colunas <td> 
        
        #crie a lista de dados
        

        #repita para cada coluna existente
        
            #o método text() -> acessa os textos
            #o método strip() -> retira espaços brancos extras
            
            #add o dado na lista
            
        
        #add a lista no dataframe
        

#chame a função que coleta os dados do site


#defina os títulos das colunas
headers = [
    'Rank', 'Visual magnitude', 'Proper Name', 
    'Bayer Designation','Distance', "Spectral type"
    ]

#converta em um dataframe

#converta o dataframe em um arquivo csv
