import requests
from bs4 import BeautifulSoup
from time import sleep
from proxy import get_proxies
from userAgent import get_user_agent
import matplotlib.pyplot as plt
import pygal

def error_log(s):
    with open('error','a') as f:
        f.write(s)
        f.write('\n')

def get_url_list():
    index_url='https://www.liaoxuefeng.com/wiki/'\
        '001374738125095c955c1e6d8bb493182103fac9270762a000#0'
    try:
        index_r=requests.get(index_url,headers=get_user_agent(),timeout=1)
        bs_obj=BeautifulSoup(index_r.text,'html.parser')
        url_list=list(map(lambda x:'https://www.liaoxuefeng.com'+x['href'],bs_obj.find_all('a',{'class':'x-wiki-index-item'})))
        return url_list
    except:
        return []

def get_count_of_reading():
    url_list=get_url_list()
    result={}
    for url in url_list:
        try:
            r=requests.get(url,headers=get_user_agent(),timeout=1)
            bs_obj=BeautifulSoup(r.text,'html.parser')
            title=bs_obj.h4.string
            count=int(str(bs_obj.find_all('div',{'class':'x-wiki-info'})[0].span.string).split()[1])
            result[url_list.index(url)]=[title,count]
            print('successly')
            sleep(3)
        except:
            error_log(url)
            print('error')
            sleep(3)
    with open('result.txt','w') as f:
        f.write(str(result))
    
    print(len(result))
    return result

def to_plt(result):
    index_values=[]
    x_values=[]
    y_values=[]
    for k ,v in result.items():
        index_values.append(k)
        x_values.append(v[0])
        y_values.append(v[1])
    plt.plot(index_values,y_values)
    plt.title('Count of Reading')
    plt.show()

def to_svg(result):
    index_values=[]
    x_values=[]
    y_values=[]
    for k ,v in result.items():
        index_values.append(k)
        x_values.append(v[0])
        y_values.append(v[1])
    hist=pygal.Bar()
    hist.x_labels=x_values
    hist.add('count',y_values)
    hist.render_to_file('test.svg')


if __name__ == '__main__':
    """
    list=[k for k,v in result.items()]
    res={}
    for k ,v in result.items():
        for k1,v1 in v.items():
            res[k]=[k1,v1]

    with open('result.txt','w') as f:
        f.write(str(res))
    """
    

    
