import requests
import bs4
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/detik-populer")
def detik_populer():
    url = 'https://www.detik.com/terpopuler?tag_from=wp_cb_mostPopular_more'
    html_doc = requests.get(url, params=('tag_from: wp_cb_mostPopular_more'))
    sup = bs4.BeautifulSoup(html_doc.text, "html.parser")
    popular_area = sup.find(attrs={'class': 'grid-row list-content'})
    judul = popular_area.findAll(attrs={'class': 'media__title'})
    gambar = popular_area.findAll(attrs={'class': 'media__image'})

    return render_template('index.html', images=gambar)





if __name__ == '__main__':
    app.run(debug=True)
