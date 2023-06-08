import requests
import lxml.html
import json
import time

dict = {}

def add(name, title, content):
    print(f"\rAdding item {name} ... {len(dict)} in total.", end='')
    dict[name] = {'种植':'', '炮制':'', '药性':'', '主治':''}
    for i, t in enumerate(title):
        if t == '生境分部': dict[name]['种植'] = content[i].replace("[br]", "<br>")
        if t == '炮制': dict[name]['炮制'] = content[i].replace("[br]", "<br>")
        if t == '性味': dict[name]['药性'] = content[i].replace("[br]", "<br>")
        if t == '功能主治': dict[name]['主治'] = content[i].replace("[br]", "<br>")

def get(url):
    #print(f"\rLoading page {url} ...", end='')
    while True:
        try:
            response = requests.get(url)
        except:
            print(url)
            time.sleep(5)
            continue
        break
    try:
        tree = lxml.html.fromstring(response.text)
        name = tree.xpath('//*[@id="main-container"]/div/div/div/article/div/h2/text()')[0]
        title = tree.xpath('//div[@class="row-head col-md-2"]/text()')
        content =  tree.xpath('//div[@class="row-content col-md-10"]/text()')
    except: return
    #print(name, title, content)
    #print(name, title)
    require = ['生境分部', '炮制', '功能主治']
    if set(require) & set(title) != set():
        add(name, title, content)
    #print(dict)

def geturl():
    for i in range(1, 271):
        print(f"\rLoading page {i} ...", end='')
        #catalog = f'https://baike.zhuayao.net/Zhongyiyao/Content/zhongyaocai/zl/%E5%85%A8%E5%9B%BD%E4%B8%AD%E8%8D%89%E8%8D%AF%E6%B1%87%E7%BC%96/p/{i}.html'
        catalog = f'https://baike.zhuayao.net/Zhongyiyao/Content/zhongyaocai/zl/%E4%B8%AD%E5%8D%8E%E6%9C%AC%E8%8D%89/p/{i}.html'
        while True:
            try:
                response = requests.get(catalog)
            except:
                print(i)
                time.sleep(5)
                continue
            break
        tree = lxml.html.fromstring(response.text)
        url = tree.xpath('//*[@id="main-container"]/div/div/div/div[2]/ul/*/a/@href')
        #url += 'https://baike.zhuayao.net/'
        #print(url)
        for j in url:
            j = 'https://baike.zhuayao.net/' + j
            get(j)

geturl()

with open("zhuayaowang1.json", 'w') as f:
    f.write(json.dumps(dict))