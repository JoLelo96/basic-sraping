import requests
import bs4

url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
html_doc = requests.get(url, params=('tag_from: wp_cb_mostPopular_more'))
sup = bs4.BeautifulSoup(html_doc.text, "html.parser")
popular_area = sup.find(attrs={'class':'grid-row list-content'})
print(popular_area)
