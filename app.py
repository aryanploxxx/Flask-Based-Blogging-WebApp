from flask import Flask

# Creating an instance of the FLask class and the constructor Flask() take the name variable as a required arguement
app= Flask(__name__)

@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)