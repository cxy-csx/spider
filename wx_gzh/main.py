import requests
from bs4 import BeautifulSoup

url = "https://mp.weixin.qq.com/s?__biz=MzU1NjMwMzA1Ng==&amp;mid=2247486483&amp;idx=1&amp;sn=35b03e96c6116ae47a916cdad9369657&amp;chksm=fbc65bacccb1d2bac4287d47535c48f8771237f442f8292ffa132741953b474765054320143a&amp;scene=27#wechat_redirect"
resp = requests.get(url)

html = BeautifulSoup(resp.text, 'lxml')

try:
    div = html.find('div', attrs={'id': 'js_content'})
    img_tags = div.find_all('img')
    # 处理图片
    for img_tag in img_tags:
        img_url = img_tag.get('data-src')
        title = img_url.split('/')[-2]
        ext = img_url.split('=')[-1]
        full_img_name = title + '.' + ext
        print(img_url)
        img_tag["src"] = img_url
    # 处理样式
    link_tags = html.find_all('link')
    print(link_tags)
    for link_tag in link_tags:
        href = link_tag.get("href")
        if href.startswith("//"):
            print(href)
            link_tag["href"] = "http:" + href
        print(link_tag["href"])

    # 保存为html格式文件
    with open("1.html", "w", encoding="utf-8") as fp:
        fp.write(str(html))

except Exception as e:
    print(e)
