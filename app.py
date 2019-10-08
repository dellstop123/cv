from flask import Flask, redirect, url_for, session, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
 return 'Hello buddy!'   
 
    

def main():
 app.run(debug=True, port=5000 )

if __name__ == '__main__':
 main()