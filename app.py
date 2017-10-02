from flask import Flask
from flask import render_template #a Flask function we can use to combine data with HTML to make a webpage
app = Flask(__name__)  # Note the double underscores on each side!

@app.route("/")
def index(): #this function returns our rendered index.html template
    template = 'index.html'
    return render_template(template)

if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)