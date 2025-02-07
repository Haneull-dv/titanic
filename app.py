from flask import Flask, render_template
from com.haneul.models.titanic.controller import Controller

app = Flask(__name__)

@app.route('/')
def index():
    controller = Controller()
    controller.modeling('train.csv', 'test.csv')
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)

