from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis
import json
import time

app = Flask(__name__)

# Configuration MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configuration Redis
cache = redis.Redis(host='localhost', port=6379, db=0)

# Modèle utilisateur
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100))

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'email': self.email}

# Route avec cache Redis
@app.route('/users', methods=['GET'])
def get_users():
    cached_users = cache.get('users')

    if cached_users:
        users = json.loads(cached_users)
        source = 'redis'
    else:
        time.sleep(2)  # simulate slow DB query
        users = [user.to_dict() for user in User.query.all()]
        cache.setex('users', 60, json.dumps(users))  # TTL = 60s
        source = 'mysql'

    return jsonify({'source': source, 'users': users})

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

