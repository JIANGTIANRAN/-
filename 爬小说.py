import html
import requests
import re

def get_chapter(number):
    url = 'http://www.xbiqugu.la/141/141755/'

    # 发送请求
    response = requests.get(url=url)
    response.encoding = response.apparent_encoding  # 自动识别编码
    html.data = response.text

    # 解析数据
    result_list = re.findall("<dd><a href='/141/141755/(.*?)' >.*?</a></dd>",html.data, re.S)
    print(result_list)

    # 爬取指定章节的小说
    chapter=result_list[number]
    print(chapter)

    #构建小说全部地址
    all_url='http://www.xbiqugu.la/141/141755/'+chapter
    response_2=requests.get(url=all_url)
    response_2.encoding=response_2.apparent_encoding
    html.data_2 = response_2.text

    #解析小说文本数据
    result=re.findall('<div id="content">(.*?)<p>.*?</p></div>',html.data_2, re.S)
    print(result)

    #保存数据
    with open('文章.txt','w',encoding='utf-8') as f:
        f.write(result[0].replace('&nbsp;','').replace('<br />',''))



chapter=int(input("请输入你想要的章节（输入数字）"))
get_chapter(chapter)