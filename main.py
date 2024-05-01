from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# @app.route('/<user>')
# def success(user):
#     return render_template('index.html', name = user)
# # app.add_url_rule('/', 'hello', helloWorld)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/booking')
def booking():
        return render_template('booking.html')

if __name__== "__main__":
        app.run(debug= True)

