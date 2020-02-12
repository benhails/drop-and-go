from drop_and_go_api.blueprints.stores.views import stores_api_blueprint
from drop_and_go_api.blueprints.users.views import users_api_blueprint
from drop_and_go_api.blueprints.bookings.views import bookings_api_blueprint
from app import app
from flask_cors import CORS

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

## API Routes ##


app.register_blueprint(users_api_blueprint, url_prefix='/api/v1/users')
app.register_blueprint(stores_api_blueprint, url_prefix='/api/v1/stores')
app.register_blueprint(bookings_api_blueprint, url_prefix='/api/v1/bookings')
