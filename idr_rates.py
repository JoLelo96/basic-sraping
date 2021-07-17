import requests

#jason_data = requests.get('http://www.floatrates.com/daily/idr.json')
jason_data = {"usd":{"code":"USD","alphaCode":"USD","numericCode":"840","name":"U.S. Dollar","rate":6.9023031278661e-5,"date":"Sat, 17 Jul 2021 11:55:01 GMT","inverseRate":14487.917749697},"eur":{"code":"EUR","alphaCode":"EUR","numericCode":"978","name":"Euro","rate":5.8428941006033e-5,"date":"Sat, 17 Jul 2021 11:55:01 GMT","inverseRate":17114.806169373}}

for data in jason_data.values():
    print (data['code'])
    print (data['name'])
    print (data['date'])
    print (data['inverseRate'])