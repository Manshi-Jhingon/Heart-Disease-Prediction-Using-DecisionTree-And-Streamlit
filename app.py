# import os
# print("Current Working Directory:", os.getcwd())

# import streamlit as st
# import numpy as np
# import joblib

# #load model and sclaer


# model = joblib.load('dt_model.pkl')  # ✅ Correct

# scaler=joblib.load('scaler_model.pkl')

# st.title("Heart Disease Detection app")

# Age=st.slider("Age",min_value=1,max_value=120,value=55)
# Sex=st.selectbox("Sex",[0,1],format_func=lambda x: "Female" if x==0 else "Male")
# Cp=st.slider("Chest pain type (cp)",0,3,0)
# Trestbps=st.slider("Resting Blood Pressure (trestbps)",80,100,120)
# Chol=st.slider("Serum Cholestrol in mg/dl (chol)",100,600,200)
# Fbs=st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)",[0,1])
# Restecg=st.slider("Resting Electrocardiographic Result (restecg)",0,2,1)
# Thalach=st.slider("Maximum heart rate achived (thalach)",60,220,150)
# Exang=st.selectbox("Excerice Included Angina (exang)",[0,1])
# Oldpeak=st.slider("ST Depression Induced by Exercise (oldpeak)",0.0,6.0,1.0,step=0.1)
# Slope=st.slider("Slope of the Peak Exercise ST segment (sloop)",0,2,1)
# Ca=st.slider("Number of Major Vessels Colored by Fluoroscopy(ca)",0,4,0)
# Thal=st.slider("Thalassemia (thal)",0,3,2)

# #predic

# if(st.button("predict")):
#     input_data=np.array([[Age,Sex,Cp,Trestbps,Chol,Fbs,Restecg,Thalach,Exang,Oldpeak,Slope,Ca,Thal]])
#     input_scaled=scaler.transform(input_data)
#     prediction =model.predict(input_scaled)[0]
#     result="Jine ke hai 4 din jee lo as you have Heart Disease" if prediction==1 else "Zinda Bach Gya re tu to"
#     st.success(result)



import os
import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('dt_model.pkl')
scaler = joblib.load('scaler_model.pkl')

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        /* Centered title with Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

        html, body, [class*="css"]  {
            font-family: 'Poppins', sans-serif;
            background-color: #f4f6f9;
        }

        .main-title {
            text-align: center;
            font-size: 36px;
            color: #1f77b4;
            margin-bottom: 30px;
        }

        .stButton>button {
            background-color: #1f77b4;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
            font-weight: bold;
            font-size: 16px;
        }

        .stButton>button:hover {
            background-color: #155b85;
            color: #ffffff;
        }

        .result-box {
            background-color: #e8f5e9;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: green;
        }

        .danger-box {
            background-color: #ffebee;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: red;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown('<div class="main-title">💓 Heart Disease Prediction App</div>', unsafe_allow_html=True)

# --- Sidebar for user input ---
st.sidebar.title("Enter Patient Details")

Age = st.sidebar.slider("Age", 1, 120, 55)
Sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
Cp = st.sidebar.slider("Chest pain type (cp)", 0, 3, 0)
Trestbps = st.sidebar.slider("Resting Blood Pressure (trestbps)", 80, 200, 120)
Chol = st.sidebar.slider("Serum Cholesterol in mg/dl (chol)", 100, 600, 200)
Fbs = st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
Restecg = st.sidebar.slider("Resting Electrocardiographic Result (restecg)", 0, 2, 1)
Thalach = st.sidebar.slider("Maximum Heart Rate Achieved (thalach)", 60, 220, 150)
Exang = st.sidebar.selectbox("Exercise-Induced Angina (exang)", [0, 1])
Oldpeak = st.sidebar.slider("ST Depression Induced by Exercise (oldpeak)", 0.0, 6.0, 1.0, step=0.1)
Slope = st.sidebar.slider("Slope of the Peak Exercise ST segment (slope)", 0, 2, 1)
Ca = st.sidebar.slider("Major Vessels Colored by Fluoroscopy (ca)", 0, 4, 0)
Thal = st.sidebar.slider("Thalassemia (thal)", 0, 3, 2)

# --- Prediction ---
if st.button("🔍 Predict"):
    input_data = np.array([[Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg,
                            Thalach, Exang, Oldpeak, Slope, Ca, Thal]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    # if prediction == 1:
    #     st.markdown(f'<div class="danger-box">😔 Jine ke hai 4 din... You may have Heart Disease.</div>', unsafe_allow_html=True)
    # else:
    #     st.markdown(f'<div class="result-box">😊 Zinda Bach Gya re Tu! You are safe from Heart Disease.</div>', unsafe_allow_html=True)
    if prediction == 1:
        st.markdown(f'<div class="danger-box">⚠️ Warning: The model indicates a high likelihood of heart disease. Please consult a medical professional for further diagnosis and treatment.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="result-box">✅ Great news! The model predicts no significant signs of heart disease. However, regular checkups are recommended for maintaining good health.</div>', unsafe_allow_html=True)

