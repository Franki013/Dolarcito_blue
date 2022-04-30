from flask import Flask, render_template, url_for
from bs4 import BeautifulSoup
import pandas as pd
import requests


url = 'https://dolarhoy.com/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


dol = soup.find_all('div', class_='val')


count = 0
dolar = list()
for i in dol: 
    if count < 2:
        dolar.append(i.text)
    else:
        break
    count += 1

dolarC = dolar[0]
dolarV = dolar[1]


dolarCo = "".join(dolarC)
dolarVe = "".join(dolarV)

characters = "$"

for i in range(len(characters)):
    dolarCo = dolarCo.replace(characters[i],"")
for i in range(len(characters)):
    dolarVe = dolarVe.replace(characters[i],"")


app = Flask(__name__)
@app.route("/")
def home():
    dolarCompra = dolarCo
    dolarVenta = dolarVe
    return render_template('index.html', dolarCompra= dolarCompra, dolarVenta= dolarVenta)

if __name__ == '__main__':
    app.run(debug=True)