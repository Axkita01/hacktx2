from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('0.0.0.0:$PORT', 0.0.0.0:$PORT), app)
http_server.serve_forever()
