from bs4 import BeautifulSoup
import requests
from csv import writer

url="https://housing.com/in/buy/searches/Pskwz0ocdh7q42r5S1"
page = requests.get(url)


soup = BeautifulSoup(page.content,'html.parser')
lists = soup.find_all('article',class_="css-1nr7r9e")

with open('housing.csv','w',encoding='utf8',newline='')as f: 
    thewriter = writer(f)
    header = ['Title','Location','Price','Area']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('a',class_="css-1lj7uy5").text.replace('\n','')
        location = list.find('a',class_="css-16drx2b").text.replace('\n','')
        price = list.find('div',class_="css-18rodr0").text.replace('\n','')
        area = list.find('div',class_="css-1ty8tu4").text.replace('\n','')
        
        info=[title,location,price,area]
        thewriter.writerow(info)

        




    
