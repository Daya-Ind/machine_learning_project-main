import imp
from flask import Flask
from housing import logger
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)
