from flask import Flask ,render_template, request


app = Flask(__name__)

def readDetails(filename):
    with open(filename,'r') as f:
        return [line for line in f ]

def writeToFile(filename, message):
    with open(filename, 'a') as f:
        f.write(message)

@app.route("/")
def homePage():
    return render_template('base.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/social")
def social():
    return render_template('social.html')

@app.route("/education")
def education(): 
    return render_template('education.html')


@app.route('/form', methods=['GET','POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        # if request.form['name']:
        #     name = request.form['name']
        if request.form['message']:
            writeToFile('static/comments.txt', request.form['message'])

    return render_template('form.html', name=name)

if __name__ == "__main__":
   app.run(debug=True, port=3000)