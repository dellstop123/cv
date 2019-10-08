from flask import Flask, redirect, url_for, session, render_template, request
from flask_oauth import OAuth
from flaskext.mysql import MySQL
import pymysql

GOOGLE_CLIENT_ID = '685526582936-obe4bpvijn4s3p0luns5b42g5a7kj77l.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'bSbA0FzotoIMDHDBzrDz2heg'
# one of the Redirect URIs from Google APIs console
REDIRECT_URI = '/oauth2callback'

SECRET_KEY = 'development key'
DEBUG = True


app = Flask(__name__)

app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'resume'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)

google = oauth.remote_app('google', base_url='https://www.google.com/accounts/',
authorize_url='https://accounts.google.com/o/oauth2/auth', request_token_url=None,
request_token_params={
    'scope': 'https://www.googleapis.com/auth/userinfo.email', 'response_type': 'code'},
access_token_url='https://accounts.google.com/o/oauth2/token',
access_token_method='POST', access_token_params={'grant_type': 'authorization_code'},
consumer_key=GOOGLE_CLIENT_ID, consumer_secret=GOOGLE_CLIENT_SECRET)



@app.route('/')
def index():
 return 'Hello buddy!'   
 
    

def main():
 app.run(debug=True, port=5000 )

if __name__ == '__main__':
 main()