import requests
from bs4 import BeautifulSoup
import lxml
html = requests.get('https://www.zhihu.com/people/marcovaldong')
soup = BeautifulSoup(html.content, 'lxml')
print(soup.prettify())  # 以标准格式显示html源码

