import requests
import bs4

url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
html_doc = requests.get(url, params=('tag_from: wp_cb_mostPopular_more'))
sup = bs4.BeautifulSoup(html_doc.text, "html.parser")
popular_area = sup.find(attrs={'class':'grid-row list-content'})
judul = popular_area.findAll(attrs={'class':'media__title'})
gambar = popular_area.findAll(attrs={'class':'media__image'})

for g in gambar:
    print(g.find('a').find('img')["title"])
#print(judul)
