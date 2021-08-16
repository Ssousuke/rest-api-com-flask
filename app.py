from flask import Flask
from flask_restful import Api

from resources.hotel_resources import Hotels, Hotel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database-api.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)


@app.before_request
def create_db():
    db.create_all()


api.add_resource(Hotels, '/hotels')
api.add_resource(Hotel, '/hotels/<int:id>')

if __name__ == '__main__':
    from sql_alchemy import db

    db.init_app(app)
    app.run(debug=True)
