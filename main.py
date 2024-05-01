from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return "Welcome to Flask"
# app.add_url_rule('/', 'hello', helloWorld)

if __name__== "__main__":
        app.run()

