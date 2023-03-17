from flask import Flask

app = Flask(__name__)


@app.route('/')  # декоратор -- позволяет запустить ту страницу, где мы сейчас находимся
# один / = главная страница
def main():
    return "<h1>Hello world</h1><br><a href='/index'>Index</a>"


if __name__ == '__main__':
    app.run()


@app.route('/index')
def index():
    return 'Index'


if __name__ == '__main__':
    app.run()
