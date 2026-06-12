# 🌾 FarmiWise AI — Agricultural Intelligence Platform

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Visit%20App-brightgreen?style=for-the-badge)](https://farmiwise-ai.onrender.com)
[![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)](https://scikit-learn.org)

> **Enter your soil's NPK values → Get the best crop recommendation → Check real-time mandi prices → Plan smarter with state-wise weather data.**

🔗 **[Try it Live](https://farmiwise-ai.onrender.com)**

---

## 🚀 What It Does

FarmiWise AI is an end-to-end agricultural decision support platform built to help Indian farmers make smarter, data-driven farming decisions.

- 🌱 **Crop Recommendation** — Enter NPK (Nitrogen, Phosphorus, Potassium) values + soil conditions → ML model recommends the best crop to grow
- 💰 **Mandi Price Prediction** — Predicts real market (mandi) prices for crops so farmers can plan when and where to sell
- 🌦️ **State-wise Weather Analytics** — Shows temperature and weather data by state to help with farming decisions
- 📊 **Market Intelligence** — Real-time data integration to show actual crop rates in markets across India
- 🔐 **User Authentication** — Secure login for personalized experience
- 🌐 **Fully Deployed** — Live on Render, accessible from any device

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Python, Flask |
| **ML Models** | Scikit-learn, XGBoost, Pandas, NumPy |
| **Frontend** | HTML, CSS, JavaScript, Bootstrap |
| **Database** | SQLite |
| **Deployment** | Render |
| **Data** | Real mandi price datasets, weather APIs |

---

## ✨ Key Features

- ✅ NPK-based intelligent crop recommendation engine
- ✅ Mandi price prediction using trained ML models
- ✅ State-wise temperature and weather data display
- ✅ Real-time market intelligence for crop rates across India
- ✅ User authentication with secure session management
- ✅ Responsive UI — works on mobile and desktop
- ✅ Fully deployed and production-ready on Render

---

## 🧠 ML Models Used

| Feature | Model | Input |
|---|---|---|
| Crop Recommendation | Random Forest / Scikit-learn | NPK values, humidity, pH, rainfall |
| Mandi Price Prediction | XGBoost Regressor | Crop type, state, season, market |
| Weather Display | API Integration | State name |

---

## 📁 Project Structure

```
FarmiWise-Ai/
│
├── app.py                  # Main Flask application & routes
├── requirements.txt        # Python dependencies
├── procfile                # Render deployment config
│
├── data/                   # Datasets (crop, mandi prices, weather)
├── model/                  # Trained ML model files (.pkl)
├── notebook/               # Jupyter notebooks (EDA + model training)
├── src/                    # Core ML logic and prediction functions
├── utils/                  # Helper functions
├── database/               # Database setup
│
├── templates/              # Jinja2 HTML templates
└── static/                 # CSS, JS, images
```

---

## ⚙️ Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/Vxrun10/FarmiWise-Ai.git
cd FarmiWise-Ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```

Open `http://localhost:5000` in your browser.

---

## 🌐 Live Demo

The app is deployed and live on Render:

👉 **[https://farmiwise-ai.onrender.com](https://farmiwise-ai.onrender.com)**

> Note: Free tier on Render may take 30–60 seconds to wake up on first visit.

---

## 📊 Sample Use Case

```
Farmer Input:
  → Nitrogen: 90, Phosphorus: 42, Potassium: 43
  → Temperature: 28°C, Humidity: 82%, pH: 6.5
  → Rainfall: 202mm
  → State: Punjab

FarmiWise AI Output:
  → Recommended Crop: Rice 🌾
  → Expected Mandi Price: ₹1,940/quintal
  → Current Market Rate in Punjab: ₹1,960/quintal
  → Weather Advisory: Favorable conditions for sowing
```

---

## 🔮 Future Improvements

- [ ] Integrate live mandi price API (Agmarknet)
- [ ] Add disease detection from crop images using CNN
- [ ] Hindi language support for rural farmers
- [ ] SMS alerts for price changes
- [ ] Soil health report generation as PDF

---

## 👨‍💻 Author

**Varun Panchal**
- 📧 varunpanchal1008@gmail.com
- 🔗 [GitHub](https://github.com/Vxrun10)
- 💼 [LinkedIn](https://linkedin.com/in/your-linkedin)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this useful, please give it a star!**
