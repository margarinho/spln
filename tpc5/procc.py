#!/usr/bin/python3

import shelve
import requests
from bs4 import BeautifulSoup as bs
import time

db = shelve.open("pages_db")

def get_page(url):
    if url not in db:
        response = requests.get(url)
        db[url] = response.text
    return db[url]

    
def get_article(url):
        response = get_page(url)
        
        if not response:
            return

        soup = bs(response, 'lxml')

        title = soup.find('title').text if soup.find('title') else "No Title"

        meta_desc = soup.find('meta', {'property': 'og:description'})
        description = meta_desc['content'].strip() if meta_desc else "No Description"

        article = soup.find('article')
        article_content = article.get_text("\n").strip() if article else "No Article Found"

        name = title.replace(" ", "_") + ".txt"

        with open(name, 'w') as file:
            file.write(f"URL: {url}\n")
            file.write(f"Title: {title}\n")
            file.write(f"Description: {description}\n")
            file.write(f"Article Content: {article_content}\n")
        
        print(f"Dados salvos em '{name}'!")

 
def main():
    
    url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/"
    txt = get_page(url)
    soup = bs(txt, 'lxml')

    dirs = []
    for table in soup.find_all("table"):
        for tr in table.find_all("tr")[3:]:
            if tr.find("img", alt="[DIR]"):
                a_tag = tr.find("a") 
                if a_tag and 'href' in a_tag.attrs:
                    print(a_tag['href'])
                    dirs.append(a_tag['href'])
    
    for page in dirs:
        get_article(page)
        time.sleep(2)

main()
db.close()