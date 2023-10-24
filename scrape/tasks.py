
import requests
from bs4 import BeautifulSoup
from scrape.models import Page, Detail

def scrape_page(link):
    raw_code = requests.get(link)
    if raw_code.status_code == 200:
        soup = BeautifulSoup(raw_code.content, 'lxml')
        name = soup.find('title').text
        page = Page(title= name, link = link)
        page.save()
        links = soup.find_all('a', href=True)
        scrape_link(links, page)
        return name
    else:
        raise Exception("Cant scarpe that page")
    
def scrape_link(links, page):
    for link in links:
        url = link['href']
        detail_list = []
        if url.startswith("http"):
            detail_list.append(Detail(page=page,name=link.text[:50], link=url ))
        Detail.objects.bulk_create(detail_list)


