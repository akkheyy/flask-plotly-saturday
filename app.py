from flask import Flask, render_template
from plot import plot

app = Flask(__name__)


@app.route("/")
def render_plot():
    return render_template("plot.html", plot_data=plot())


if __name__ == "__main__":
    app.run(debug=True)

# data coming from pandas portion of plot file
# def plot loads series, then converts from python using plotly definition to json string so can be read by any language
# app.py imports plot plot() function
# loaded into javascript functin on html file
