from flask import Flask, render_template, request, redirect, url_for, session
from src.prediction import predict_crop
from database.models import db, User
from data.crops_data import crops_database
from data.state_data import state_data
from data.price_data import base_prices
import joblib
import requests
import os

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# -----------------------------
# Flask Config
# -----------------------------

app.config['SECRET_KEY'] = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# -----------------------------
# Load ML Model
# -----------------------------

model = joblib.load("model/crop_model.pkl")

# -----------------------------
# First Appearance
# -----------------------------

@app.route("/")
def firstAppearance():
    return render_template("firstAppearance.html")

# -----------------------------
# Authentication Routes
# -----------------------------

@app.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            return "Username already exists"

        hashed_password = generate_password_hash(password)

        user = User(username=username, email=email, password=hashed_password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template("signup.html")


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):

            session['user'] = username
            return redirect(url_for('home'))

        else:
            return "Invalid Credentials"

    return render_template("login.html")

@app.route('/logout')
def logout():

    session.pop('user', None)

    return render_template("logout.html")

# -----------------------------
# Protected Pages
# -----------------------------

@app.route('/home')
def home():

    if 'user' not in session:
        return redirect(url_for('login'))

    return render_template("home.html")


@app.route('/about')
def about():
    return render_template("about.html")



@app.route('/stateAdvisory', methods=['GET','POST'])
def stateAdvisory():

    advisory = None
    state_name = None

    

    if request.method == "POST":

        state = request.form['state']

        advisory = state_data.get(state)

        state_name = state.replace("_"," ").title()

    return render_template(
        "stateAdvisory.html",
        advisory=advisory,
        state_name=state_name
    )

@app.route('/weatherInsights', methods=['GET','POST'])
def weatherInsights():

    weather = None
    city = None

    API_KEY = "661fc6460b81e2cde81cac36347022eb"

    if request.method == "POST":

        city = request.form['city']

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_desc = data["weather"][0]["description"]

            advice = "Good weather for farming activities."

            if temperature > 35:
                advice = "High temperature. Ensure proper irrigation."

            elif humidity > 80:
                advice = "High humidity. Monitor crops for fungal diseases."

            weather = {
                "temperature": f"{temperature} °C",
                "humidity": f"{humidity} %",
                "rainfall": weather_desc,
                "advice": advice
            }

        else:
            weather = {
                "temperature":"N/A",
                "humidity":"N/A",
                "rainfall":"City not found",
                "advice":"Please enter a valid city."
            }

    return render_template(
        "weatherInsights.html",
        weather=weather,
        city=city
    )

@app.route('/cropPrice', methods=['GET','POST'])
def cropPrice():

    prediction = None
    crop = None

    if request.method == "POST":

        crop = request.form['crop']
        state = request.form['state']
        month = request.form['month']

        

        base_price = base_prices.get(crop,2000)

        # Seasonal effect
        seasonal_increase = ["apr","may","jun","jul"]

        if month in seasonal_increase:
            price = base_price + 200
            trend = "Increasing"
        else:
            price = base_price - 100
            trend = "Stable"

        prediction = {
            "price":price,
            "trend":trend,
            "advice":f"Market prices for {crop} in {state} during {month} may fluctuate depending on supply and demand."
        }

    return render_template(
        "cropPrice.html",
        prediction=prediction,
        crop=crop
    )


@app.route('/marketInsights')
def marketInsights():
    return render_template("marketInsights.html")



# -----------------------------


@app.route('/cropRecommendation', methods=['GET','POST'])
def cropRecommendation():

    if request.method == "POST":

        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)

        return render_template(
            "result.html",
            crop=crop,
            N=N,
            P=P,
            K=K,
            temperature=temperature,
            humidity=humidity,
            ph=ph,
            rainfall=rainfall
        )

    return render_template("cropRecommendation.html")


@app.route('/cropsInfo', methods=['GET','POST'])
def cropsInfo():

    crop_data = None
    crop_name = None

    

    if request.method == "POST":

        crop_name = request.form['crop'].lower()

        crop_data = crops_database.get(crop_name)

    return render_template("cropsInfo.html", crop_data=crop_data, crop_name=crop_name)

# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)