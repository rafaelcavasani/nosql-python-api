from flask import Flask
import os
from routes.ingressos import ingressos_blueprint

app = Flask(__name__)
app.register_blueprint(ingressos_blueprint)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)