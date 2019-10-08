from flask import Flask, redirect, url_for, session, render_template, request



app = Flask(__name__)






@app.route('/')
def index():
 return 'Hello World'   
 
    

def main():
 app.run(debug=True, port=5000 )

if __name__ == '__main__':
 main()