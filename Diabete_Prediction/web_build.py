import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler
import pandas as pd
import feature_engineer # self-build

scaler = joblib.load('robust_scaler.pkl')
model = joblib.load('diabetes_predict.pkl')

st.title("Machine Learning Diabetes Prediction")

###
pregnancies = st.number_input("Enter Numbers of Pregnant times:", min_value=0)
glucose = st.number_input("Enter glucose concentration:", min_value=0)
bp = st.number_input("Enter blood pressure (mm/Hg):", min_value=0)
skinthicknes = st.number_input("Enter tricep skin fold thickness (mm):", min_value=0)
insulin = st.number_input("Enter 2-Hour serum insulin (mu U/ml):", min_value=0)
weight = st.number_input("Enter weight index:" , min_value=0.0, step=0.01)
height = st.number_input("Enter height index (Example: 175cm = 1.75):", min_value=1.0, step=0.1)
bmi = 0
if height > 0:  # Tránh lỗi chia cho 0
    bmi = weight / (height ** 2)
    st.write(f"Chỉ số BMI: {bmi:.2f}")  # Làm tròn 2 chữ số thập phân
else:
    st.write("Chiều cao không hợp lệ!")

dpf = st.number_input("Enter Diabetes pedigree function:", min_value=0.0, step=0.001) # DiabetesPedigreeFunction
age = st.number_input("Enter Age:", min_value=0)
###

###
input_data = pd.DataFrame([[pregnancies, glucose, bp, skinthicknes, insulin, bmi, dpf, age]], 
                            columns=["Pregnancies","Glucose","BloodPressure","SkinThickness",
                                    "Insulin","BMI","DiabetesPedigreeFunction","Age"])
###

###
new = feature_engineer
new_features = pd.DataFrame([[*new.New_BMI(bmi), new.New_Insulin(insulin), *new.New_Glucose(glucose)]],
                            columns=["NewBMI_Obesity 1", "NewBMI_Obesity 2", "NewBMI_Obesity 3", 
                                     "NewBMI_Overweight", "NewBMI_Underweight",
                                     "NewInsulinScore_Normal",
                                     "NewGlucose_Low", "NewGlucose_Normal",
                                     "NewGlucose_Overweight", "NewGlucose_Secret"])
###

if st.button('Dự đoán (Kết quả có thể không chính xác 100%)'):
    input_scaled = scaler.transform(input_data)
    
    input_scaled = pd.DataFrame(input_scaled, columns=["Pregnancies","Glucose","BloodPressure","SkinThickness",
                                        "Insulin","BMI","DiabetesPedigreeFunction","Age"])
    

    input_scaled = pd.concat([input_scaled, new_features], axis=1)
    result = model.predict(input_scaled)
    result_proba = model.predict_proba(input_scaled)


    if result[0] == 0:
        st.write("Kết quả dự đoán: Khả năng không mắc bệnh cao")
        st.write(f"Có {result_proba[0][1]:.2%} khả năng mắc bệnh")
    elif result[0] == 1:
        st.write("Kết quả dự đoán: Khả năng mắc bệnh cao")
        st.write(f"Có {result_proba[0][1]:.2%} khả năng mắc bệnh")
