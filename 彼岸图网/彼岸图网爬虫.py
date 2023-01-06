import requests
import parsel
import os
os.mkdir('彼岸图网（美女）')
for page in range(1,11):
    print(f'-------正在爬取第{page}页----------')
    sub_url = ''if page == 1 else '_' + str(page)
    url = f'https://pic.netbian.com/4kmeinv/index{sub_url}.html'
    if not os.path.exists('彼岸图网（美女）/' + f'第{page}页'):
        os.mkdir('彼岸图网（美女）/' + f'第{page}页')
    response = requests.get(url=url)
    response.encoding = 'gbk'

    data_html = response.text
    selector = parsel.Selector(data_html)
    a_href_list = selector.css('#main > div.slist > ul > li > a::attr(href)').getall()  # 获取每个图片的url
    for a_href in a_href_list:
        a_href = 'https://pic.netbian.com' + a_href
        response_1 = requests.get(a_href)
        selector_1 = parsel.Selector(response_1.text)  # 每个图片的网页链接
        img = selector_1.css('#main > div > div > div > a > img::attr(src)').getall()[0]  # 照片的url
        download_url = 'https://pic.netbian.com/' + img
        title = img.split('/')[-1]
        download = requests.get(download_url).content

        with open(f'彼岸图网（美女）/第{page}页/{title}', mode='wb')as f:
            f.write(download)
        print(title, '下载完成')
    print(f'第{page}页全部下载完成')