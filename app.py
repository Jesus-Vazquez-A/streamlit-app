import streamlit as st
import joblib
import streamlit as st


st.write(""" # Predicted Insurence Price """)

st.image("""bg-insurance.jpg""")


st.cache(allow_output_mutation=True)

def json_file():
    
    with open("features.json") as F:
        
        features_names = json.loads(F.read())
      
    return np.array(features_names['features'])



st.cache(allow_output_mutation=True)


def input_data():
    
    age=st.slider(label="Age",min_value=18,max_value=64,step=1),
    
    sex=st.selectbox("Sex",("Male","Female")),
    
    bmi=st.number_input(label="BMI",min_value=18.0,max_value=47.0,step=0.0001),
    
    children=st.slider(label="Children",min_value=0,max_value=5,step=1),
    
    smoker=st.selectbox("Smoker",("No","Yes")),
    
    medical_problem=st.selectbox("Medical Problem",("Light","Severe")),
    
    region=st.radio("Region",('Southeast', 'Northeast', 'Southwest', 'Northwest'))
    
    
    return age,sex,bmi,children,smoker,medical_problem,region



st.cache(allow_output_mutation=True)

def preprocessing():
    
    age,sex,bmi,children,smoker,medical_problem,region = input_data()

    columns = json_file()
    data = np.zeros(len(columns))
    
    region_idx = np.where(region == columns)[0][0]
    
    
    if region_idx >= 0:
        data[region_idx] = 1
        
        
    data[4] = age
    data[5] = np.where(sex  == 'male',1,0)
    data[6] = children
    data[7] = bmi
    data[8] = np.where(medical_problem == 'severe',1,0)
    data[9] = np.where(smoker == 'smoker',1,0)
    
    return  np.asarray([data])



st.cache(allow_output_mutation=True)

def predict(new_data):
    model = joblid.load('linear_model.pkl')
    return  model.predict(new_data)



st.cache(allow_output_mutation=True)

def main():
    
    st.subheader("User Input")
    new_data =  preprocessing()
    if st.button(label = 'Predict'):
        
        charges = predict(new_data)
        st.success(f'The estimated health insurance charge is: $ {charges} USD')
        
        
if __name__ == "__main__":
    
    main()


