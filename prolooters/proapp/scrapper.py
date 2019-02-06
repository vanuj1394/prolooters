from lxml import html  
import csv,os,json
import requests
from exceptions import ValueError
from time import sleep
from .models import product_iteam
class parsor():
    def AmzonParser(request):
        url = "https://www.mytokri.com"
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
        page = requests.get(url,headers=headers)
        while True:
            try:
            	extracted_data = []
                for i in range(1,30):
                            doc = html.fromstring(page.content)
                            xpath_title = "//*[@id=\"mt-only-grid\"]/div[%d]/div/div[2]/a/p/text()" %i
                            xpath_link="//*[@id=\"mt-only-grid\"]/div[%d]/div/div[2]/a/@href" %i
                            xpath_price = "//*[@id=\"mt-only-grid\"]/div[%d]/div/div[2]/h4/span[1]/text()" %i
                            xpath_src = "//*[@id=\"mt-only-grid\"]/div[%d]/div/div[1]/a/img/@src" %i
                            title = doc.xpath(xpath_title)
                            link = doc.xpath(xpath_link)
                            deal_price = doc.xpath(xpath_price)
                            img_src = doc.xpath(xpath_src)
                            link = url + link[0]
                            next_page = requests.get(link,headers= headers)
                            next_doc = html.fromstring(next_page.content)
                            next_xpath = "//*[@id=\"main-content\"]/div/div[2]/div[2]/div[2]/a/@href"
                            buy_link = next_doc.xpath(next_xpath)
                            buy_link = buy_link[0]
                            splitted_url = buy_link.split("url=")
                            s=","
                            print(s.join(title))
                            print('\n')
                            print(deal_price)
                            print(splitted_url[1])
                            p = product_iteam(title = s.join(title) , buy_link = splitted_url[1],deal_price = s.join(deal_price), img_src = s.join(img_src))
                            p.save()

            	return 
            except Exception as e:
                print e
                return True

    # def ReadAsin():
        # AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"Asinfeed.csv")))
        # extracted_data = []
        # url = "https://www.mytokri.com"
        # print "Processing: "+url
        # AmzonParser(url)
        # print("Element scapped",len(extracted_data))
        # f=open('data.json','w')
        # json.dump(extracted_data,f,indent=4)
     
     
    # if __name__ == "__main__":
    #     AmzonParser()