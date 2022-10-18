import streamlit as st
import joblib
import streamlit as st





def input_data():
    
    age=st.slider(label="Age",min_value=18,max_value=64,step=1),
    
    sex=st.selectbox("Sex",("Male","Female")),
    
    bmi=st.number_input(label="BMI",min_value=18.0,max_value=47.0,step=0.0001),
    
    children=st.slider(label="Children",min_value=0,max_value=5,step=1),
    
    smoker=st.selectbox("Smoker",("No","Yes")),
    
    medical_problem=st.selectbox("Medical Problem",("Light","Severe")),
    
    region=st.radio("Region",('Southeast', 'Northeast', 'Southwest', 'Northwest'))
    
    
    return age,sex,bmi,children,smoker,medical_problem,region
