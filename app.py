import streamlit as st
import numpy as np
import joblib
import json




def json_file():
    
    with open("features.json") as columns:
        
        data_json = json.loads(columns.read())
        data_json = np.asarray(data_json['features'])

    return data_json


st.cache(allow_output_mutation=True)


def input_data():
    
    region=st.radio("Region",('Southeast', 'Northeast', 'Southwest', 'Northwest'))
    
    age=st.slider(label="Age",min_value=18,max_value=64,step=1),
    
    sex=st.selectbox("Sex",("Male","Female")),
    
    children=st.slider(label="Children",min_value=0,max_value=5,step=1),
    
    bmi=st.number_input(label="BMI",min_value=18.0,max_value=47.0,step=0.0001),
    
    medical_problem=st.selectbox("Medical Problem",("Light","Severe")),
    
    smoker=st.selectbox("Smoker",("No","Yes"))
    
    
    return region,age,sex,children,bmi,medical_problem,smoker





def main():
    
    st.write(""" # Predicted Insurence Price """)

    st.image("""bg-insurance.jpg""")
  
  #  new_data = preprocess()
    
    data = json_file()
    
    if st.button(label = 'Predict'):
        
      #  price=predict(new_data)
        st.success(f'The estimated price of the vehicle is: $ {data} £')


st.cache(allow_output_mutation=True)

if __name__ == '__main__':
    main()



