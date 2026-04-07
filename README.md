# ✈️ Flight Price Predictor

🚀 A Machine Learning based web app that predicts flight ticket prices using user inputs like airline, route, stops, and journey date.

---

## 🌟 Features

* 🎯 Accurate flight price prediction using ML models
* ⚡ Fast and interactive UI built with Streamlit
* 🧠 Uses advanced models (Random Forest, XGBoost, etc.)
* 📊 Feature engineering (date, time, route patterns)
* 🌐 Ready for deployment (Streamlit Cloud)

---

## 🖥️ Demo

👉 Live App: *(Add your Streamlit link here after deployment)*

---

## 📂 Project Structure

```
flight-price-predictor/
│
├── app.py             # Streamlit UI
├── pipe.pkl           # Trained ML pipeline
├── Data_Train.xlsx    # Dataset
├── README.md          # Project documentation
├── requirements.txt   # Dependencies
```

---

## ⚙️ Tech Stack

* Python 🐍
* Pandas & NumPy
* Scikit-learn
* XGBoost / LightGBM
* Streamlit

---

## 🧠 How It Works

1. User enters flight details:

   * Airline
   * Source & Destination
   * Stops
   * Journey Date

2. Feature Engineering:

   * Extracts day, month, weekday
   * Calculates weekend indicator
   * Adds time-based features

3. Model Prediction:

   * Input passed into trained pipeline (`pipe.pkl`)
   * Model predicts log(price)
   * Converted back using exponential

---

## 🚀 Installation & Run Locally

### Step 1: Clone repo

```
git clone https://github.com/Sukhmanpreetkaur18/flight-price-predictor.git
cd flight-price-predictor
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
```

### Step 3: Run app

```
streamlit run app.py
```

---

## ⚠️ Limitations

* Model supports limited cities (based on training data)
* New/unseen routes may reduce prediction accuracy

---

## 💡 Future Improvements

* 🌍 Support more cities & real-time data
* 📈 Add price trend visualization
* 🤖 Integrate external APIs (flight data)
* 🎨 Enhance UI/UX with animations

---

## 👩‍💻 Author

**Sukhmanpreet Kaur**

---

## ⭐ Show your support

If you like this project, give it a ⭐ on GitHub!
