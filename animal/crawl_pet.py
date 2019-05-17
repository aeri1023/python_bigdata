# -*-coding: utf-8 -*-
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def crawl(pet):
    for pageNum in range(50): #50page
        print pet
        p = {"query": pet,"pagingIndex" : pageNum}
        url="https://search.shopping.naver.com/search/all.nhn?"
        r=requests.get(url,params=p)
        pet_ = r.text
        soup=BeautifulSoup(pet_,"lxml")
        product =[name.get_text().strip() for name in soup.select('a.tit')]
    return product
    
def fre_word(list_pet):
    d=dict()
    for name in list_pet:
        for n in name.split():
            if n not in d:
                d[n]=1
            else:
                d[n]=d[n]+1
    d1 = dict()
    for key, value in d.iteritems():
        if value>1:
            d1[key]=value
        print key, value

def make_cloud(list_pet):
    wordcloud_pet = WordCloud(
        font_path='C:/Windows/Fonts/HMFMPYUN.TTF',
        background_color='white'
    ).generate(' '.join(list_pet))
    plt.imshow(wordcloud_pet, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def main():
    product_dog = crawl(u"애견용품")
    #fre_word(product_dog) 
    make_cloud(product_dog)

if __name__=="__main__":
    main()