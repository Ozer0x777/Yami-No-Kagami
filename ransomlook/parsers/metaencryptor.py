import os
from bs4 import BeautifulSoup

def main():
    list_div=[]

    for filename in os.listdir('source'):
        try:
            if filename.startswith(__name__.split('.')[-1]+'-'):
                html_doc='source/'+filename
                file=open(html_doc,'r')
                soup=BeautifulSoup(file,'html.parser')
                divs_name=soup.find_all('div', {"class": "card shadow-sm border-info shadow-lg"})
                for div in divs_name:
                    print(div)
                    title = div.find('div',{"class","card-header"}).text.strip()
                    description = div.find("p", {"class": "card-text"}).text.strip()
                    list_div.append({"title" : title, "description" : description})
                file.close()
        except:
            print("Failed during : " + filename)
            pass
    print(list_div)
    return list_div