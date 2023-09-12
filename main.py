from flask import Flask

import random

 

app = Flask(__name__)

 

@app.route("/yazitura")

def hello_world():
    x = random.randint(1, 6)
    return f"<p>sonuc: {x} </p> <h1></h1>"

@app.route("/sifre")
def sifre_olusturucu():
    sifre = ""
    for i in range(15):
        karakter = chr(random.randint(40, 126))
        sifre = sifre+karakter

    #x = random.randint(50000, 999999)
    #x = random.randint("+-/!'^^%&=?_#$qwertyuıopğüasdfghjklşizxcvbnmöçQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNMÖÇ.1234567890*<|>")
    return f"<p>sifre: {sifre} </p> <h1>Harika! şimdi kopyalama zamanı.</h1>"

app.run(debug=True)