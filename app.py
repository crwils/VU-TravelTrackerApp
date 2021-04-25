from flask import Flask, render_template

from controllers.country_controller import countries_blueprint
from controllers.vu_point_controller import vu_points_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(vu_points_blueprint)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

