from flask import render_template, request, redirect, url_for, session, jsonify
from src.app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Define UserProfile and Prediction models
class UserProfile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)

class Prediction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.String(150), nullable=False)
    prediction_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user_profile.id'), nullable=False)

# Home Route (Redirects to login page)
@app.route('/')
def home():
    return redirect(url_for('login'))  # Corrected to redirect to the login route

# Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'], method='sha256')
        user = UserProfile(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')  # Ensure this is in the 'templates' folder

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserProfile.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password", 401  # Returning status code for invalid login
    return render_template('login.html')  # Ensure this is in the 'templates' folder

# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Ensure user is logged in before accessing the dashboard
    user = UserProfile.query.get(session['user_id'])
    predictions = Prediction.query.filter_by(user_id=user.id).all()
    prediction_data = {date.strftime('%b'): prediction.prediction for prediction in predictions}
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for month in months:
        if month not in prediction_data:
            prediction_data[month] = 'No Data'
    return render_template('dashboard.html', user=user, prediction_data=prediction_data)  # Ensure this is in the 'templates' folder

# Profile Update Route
@app.route('/profile', methods=['POST'])
def update_profile():
    user = UserProfile.query.get(session['user_id'])
    user.age = request.form['age']
    user.weight = request.form['weight']
    user.height = request.form['height']
    db.session.commit()
    return redirect(url_for('dashboard'))

# Predict Health Risk Route
@app.route('/predict', methods=['POST'])
def predict():
    user = UserProfile.query.get(session['user_id'])
    input_data = {
        "age": user.age,
        "weight": user.weight,
        "height": user.height,
        "fever": request.form.get('fever'),
        "cough": request.form.get('cough'),
        "headache": request.form.get('headache'),
        "chest_pain": request.form.get('chest_pain')
    }
    input_data["BMI"] = user.weight / (user.height / 100) ** 2
    prediction = predict_health_risk(input_data)  # Assuming this function exists and works

    new_prediction = Prediction(
        prediction=prediction,
        user_id=user.id,
        prediction_date=datetime.datetime.utcnow()
    )
    db.session.add(new_prediction)
    db.session.commit()

    return jsonify({"prediction": prediction})

# Logout Route
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))
