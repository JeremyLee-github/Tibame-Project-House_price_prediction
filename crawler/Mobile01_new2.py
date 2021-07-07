from bs4 import BeautifulSoup
import requests
import os
import csv
import time
import time, datetime
import random 
import pandas as pd

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'Referer': 'https://www.mobile01.com/'
}

url = 'https://www.mobile01.com/topiclist.php?f=454'



outurl=[]
outtitle=[]
outmain=[]
outrecovery=[]
outcreateTime=[]
for n in range(0,31):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    datas = soup.findAll('div', class_='c-listTableTd__title')  # type:<class 'bs4.element.ResultSet'>, find-> type: <class 'bs4.element.Tag'>
    # print(datas)

    for data in datas:                        #取得每一頁的PO文連結
        title = data.find('a').text
        article_url = 'https://www.mobile01.com/' + data.find('a')['href']
        try:
            res2 = requests.get(url=article_url, headers=headers)         #對每篇PO文做request
            soup2 = BeautifulSoup(res2.text, 'html.parser')
            article_content = soup2.find('article', class_="l-publishArea topic_article").text.replace(' ','').replace('\t','').replace('\n','')

            for i in soup2.findAll('blockquote'):   #去除<blockquote>原貼文的文章
                i.decompose()
            reply_contents = soup2.findAll('article', class_="u-gapBottom--max c-articleLimit")   #每篇PO文的回覆(第一頁)
            time_tag = soup2.find('span', class_="o-fNotes o-fSubMini")                 #每篇PO文的時間(第一頁)
            createTime = time_tag.text + ':00'
            
            reply_all=[]
            count=0
            for reply in reply_contents:                       #把第一頁的回覆內容一則一則寫到 reply_all
                count +=1
                reply = reply.text.replace(' ','').replace('\n\n','').replace('\t','').replace('\n','')
                reply_all.append('Reply'+ str(count)+ ':' + reply)
            try:
                inner_pages_ultag = soup2.find('ul', class_="l-pagination")     #定位在頁數的Tag

                inner_pages_litag = inner_pages_ultag.findAll('li')    
                final_page = inner_pages_litag[-1].text                        #抓出最後一頁
            except:
                final_page = 1               #若tag不到，代表只有一頁 ->PASS
            
            for page in range(2, int(final_page)+1 ):      #抓最後一頁的頁數(因為內文超過5頁，頁數鈕就會縮減)
                url_2 = 'https://www.mobile01.com/' + data.find('a')['href'] + '&p={}'.format(page)

                res3 = requests.get(url=url_2, headers=headers)    #對每篇回覆文章進行request
                soup3 = BeautifulSoup(res3.text, 'html.parser')

                for j in soup3.findAll('blockquote'):   #去除<blockquote>原貼文的文章
                    j.decompose()


                reply_contents_inners_after_p2 = soup3.findAll('article', class_="u-gapBottom--max c-articleLimit")  
                for inner_content in reply_contents_inners_after_p2:        #把第二頁之後的回覆內容 一則一則寫到 reply_all
                    count +=1
                    inner_content = inner_content.text.replace(' ','').replace('\n\n','').replace('\t','').replace('\n','')
                    reply_all.append('Reply' + str(count)+ ':' + inner_content)

            outurl.append(article_url)
            outtitle.append(title)
            outmain.append(article_content)
            outrecovery.append(str(reply_all))
            outcreateTime.append(createTime)
        except:
            print('Error:', article_url)
    
    final_list ={'url':outurl,'title':outtitle,'main':outmain,'recovery':outrecovery,'createTime':outcreateTime}

    output = pd.DataFrame(final_list)
    output.to_csv('mobile01_list_new.csv', index=False , encoding='utf-8')

    print('page:{}'.format(n+1))

    newUrl = 'https://www.mobile01.com' + soup.find('a',class_="c-pagination c-pagination--next")['href']  #Find new url
    url=newUrl


import pandas as pd
a = pd.read_csv('mobile01_new_open2.csv',encoding='utf-8')
print(a)