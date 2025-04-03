from environs import Env

env = Env()
env.read_env()

APP_NAME = env('APP_NAME')
APP_ENV = env('APP_ENV')
APP_KEY = env('APP_KEY')
APP_INSTALLED = env('APP_INSTALLED')
APP_DEBUG = env('APP_DEBUG')
APP_CACHE = env('APP_CACHE')
APP_URL = env('APP_URL')
LOG_CHANNEL = env('LOG_CHANNEL')
DB_CONNECTION = env('DB_CONNECTION')
DB_HOST = env('DB_HOST')
DB_PORT = env('DB_PORT')
DB_DATABASE = env('DB_DATABASE')
DB_USERNAME = env('DB_USERNAME')
DB_PASSWORD = env('DB_PASSWORD')
BROADCAST_DRIVER = env('BROADCAST_DRIVER')
CACHE_DRIVER = env('CACHE_DRIVER')
QUEUE_DRIVER = env('QUEUE_DRIVER')
QUEUE_CONNECTION = env('QUEUE_CONNECTION')
SESSION_DRIVER = env('SESSION_DRIVER')
FILESYSTEM_DRIVER = env('FILESYSTEM_DRIVER')
REDIS_HOST = env('REDIS_HOST')
REDIS_PASSWORD = env('REDIS_PASSWORD')
REDIS_PORT = env('REDIS_PORT')
MAIL_DRIVER = env('MAIL_DRIVER')
MAIL_HOST = env('MAIL_HOST')
MAIL_PORT = env('MAIL_PORT')
MAIL_USERNAME = env('MAIL_USERNAME')
MAIL_PASSWORD = env('MAIL_PASSWORD')
MAIL_ENCRYPTION = env('MAIL_ENCRYPTION')
PUSHER_APP_ID = env('PUSHER_APP_ID')
PUSHER_APP_KEY = env('PUSHER_APP_KEY')
PUSHER_APP_SECRET = env('PUSHER_APP_SECRET')
PUSHER_APP_CLUSTER = env('PUSHER_APP_CLUSTER')
MIX_PUSHER_APP_KEY = env('MIX_PUSHER_APP_KEY')
MIX_PUSHER_APP_CLUSTER = env('MIX_PUSHER_APP_CLUSTER')
SCOUT_QUEUE = env('SCOUT_QUEUE')
DEBUGBAR_ENABLED = env('DEBUGBAR_ENABLED')
QUERY_DETECTOR_ENABLED = env('QUERY_DETECTOR_ENABLED')
INVISIBLE_RECAPTCHA_SITEKEY = env('INVISIBLE_RECAPTCHA_SITEKEY')
INVISIBLE_RECAPTCHA_SECRETKEY = env('INVISIBLE_RECAPTCHA_SECRETKEY')
INVISIBLE_RECAPTCHA_BADGEHIDE = env('INVISIBLE_RECAPTCHA_BADGEHIDE')
INVISIBLE_RECAPTCHA_DATABADGE = env('INVISIBLE_RECAPTCHA_DATABADGE')
INVISIBLE_RECAPTCHA_TIMEOUT = env('INVISIBLE_RECAPTCHA_TIMEOUT')
INVISIBLE_RECAPTCHA_DEBUG = env('INVISIBLE_RECAPTCHA_DEBUG')
