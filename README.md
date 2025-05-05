# Medical Insurance Cost Predictor

This Streamlit web app predicts **medical insurance costs** based on user inputs like age, sex, BMI, smoking status, children, and region. It uses a trained machine learning model and a preprocessor for clean and consistent input handling.

---

## Features

- Simple, interactive UI
- Real-time cost predictions
- Works with trained model (`best_model.pkl`) and transformer (`preprocessor.pkl`)

---

## How to Use

### 1. Clone the Repository or Copy Files

Make sure `app.py`, `best_model.pkl`, and `preprocessor.pkl` are in the same folder.

### 2. Install Dependencies

```bash
pip install -r requirements.txt

3. Run the App

streamlit run app.py

4. Input Fields

Age

Sex

BMI

Children

Smoker (Yes/No)

Region


Click Predict Medical Cost to get the estimated value.


---

File Structure

medical-cost-predictor/
│
├── app.py                 # Streamlit app script
├── best_model.pkl         # Trained ML model
├── preprocessor.pkl       # Data preprocessor
├── README.md              # Project overview and usage
└── requirements.txt       # Python dependencies


---

Author

Ankit Kumar Jha


---

License

This project is intended for learning and demonstration purposes only.