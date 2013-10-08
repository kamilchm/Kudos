import os
from boto.s3.connection import S3Connection
import sys
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True #CROSS-SITE REQUEST FORGERY
SECRET_KEY = 'you-will-never-guess'



try:
	AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
	AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
	S3_BUCKET = os.environ.get('S3_BUCKET')
	if AWS_ACCESS_KEY_ID == None or AWS_SECRET_ACCESS_KEY == None or S3_BUCKET is None:
		msg = (
			"You must configure the environment variables AWS_ACCESS_KEY_ID, "
			"AWS_SECRET_ACCESS_KEY and S3_BUCKET. Please see "
			"https://devcenter.heroku.com/articles/s3"
			)
		raise Exception(msg)


	conn = S3Connection(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY)
	S3_BUCKET = conn.get_bucket(S3_BUCKET)
	USE_S3 = True
except Exception, e:
	USE_S3 = False

	print e
	sys.stdout.flush()

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#URI is required fy flask-sqlalchemy extension. This is path to database file
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
#folder where we store sqlalchemy migrate data files


#mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

#administrator list
ADMINS = ['mskeving@gmail.com']
