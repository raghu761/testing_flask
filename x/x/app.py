from flask import Flask , render_template
from flask import request
app = Flask(__name__)

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/nextProcess/' , methods=['GET' ,'POST'])
def next_process():
    image_url = request.form["image-input"] 
    print(image_url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True) 