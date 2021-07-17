import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/detik-populer")
def detik_populer():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    html_doc = requests.get(url, params=('tag_from: wp_cb_mostPopular_more'))
    sup = bs4.BeautifulSoup(html_doc.text, "html.parser")
    popular_area = sup.find(attrs={'class': 'grid-row list-content'})
    judul = popular_area.findAll(attrs={'class': 'media__title'})
    gambar = popular_area.findAll(attrs={'class': 'media__image'})
    return render_template('detik-scraper.html', images=gambar)

@app.route("/idr-rates")
def idr_rates():
    source = requests.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr-rates.html', datas=json_data.values())





if __name__ == '__main__':
    app.run(debug=True)
