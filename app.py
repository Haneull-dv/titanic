from flask import Flask, render_template
from com.haneul.models.titanic.titanic_controller import TitanicController
from com.haneul.models.matjip.matjip_controller import MatjipController

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/titanic')
def titanic():
    titaniccontroller = TitanicController()
    titaniccontroller.modeling('train.csv','test.csv')
    return render_template('/index.html')


@app.route('/matjip')
def matjip():
    matjipcontroller = MatjipController()
    matjipcontroller.modeling('matjip.csv')
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(debug=True)

