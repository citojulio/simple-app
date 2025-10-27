# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return "Halo dari Flask + Docker + Jenkins!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Ambil data harga dari API CoinGecko
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    data = requests.get(url).json()

    bitcoin = data['bitcoin']['usd']
    ethereum = data['ethereum']['usd']

    return render_template('index.html', btc=bitcoin, eth=ethereum)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
