"""
Jalen Banks
Lab 11, 03 2026
Introduction to Flask
"""

from flask import Flask, render_template

"""
Create n object 'app' from the flask module
"""
app = Flask(__name__)

#set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Jalen"
    fruits = ["Apple", "Banana", "Cherry"]
    return render_template('index.html', username=name, listfruits=fruits)

# endpoints refer to the name of the view in the app
@app.route('/about')
def about():
    images = ['images/owl.jpg', 'images/cat1.png', 'images/cat2.png']
    return render_template('about.html', images=images)

@app.route('/quotes')
def quotes():
    return '<h1>Famous Quotes</h1><p>"The only limit to our realization of tomorrow is our doubts of today." - Franklin D. Roosevelt</p>'

# set the 'app' to run if you excute this file directly (not imported as a module)
if __name__ == '__main__':
    app.run(debug=True)