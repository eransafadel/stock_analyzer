# Data Source
import jinja2
from finvizfinance.quote import finvizfinance

from MyStock import MyStock
from flask import Flask, escape, request, render_template, url_for, request, redirect

env = jinja2.Environment()
env.globals.update(zip=zip)

app = Flask(__name__)
app.jinja_env.filters['zip'] = zip


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        tckr_symb = request.form["nm"]
        return redirect(url_for("ticker", tckr=tckr_symb))
    else:
        return render_template('index.html')


@app.route("/<tckr>")
def ticker(tckr):
    stock = MyStock(tckr)

    return render_template('result.html', price_s=stock.price, name=stock.name, zip=zip, content=stock.to_json(),
                           colors=stock.to_json_color())


if __name__ == '__main__':
    app.run(debug=True)
