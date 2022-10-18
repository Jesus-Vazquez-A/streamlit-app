import streamlit as st
import joblib
import streamlit as st



st.cache(allow_output_mutation=True)

def json_file():
    
    with open("faetures.json") as F:
        
        features_names = json.loads(F.read())
        features_names = np.asarray(data_json['features'])

    return features_names



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

def predict(region,age,sex,children,bmi,medical_problem,smoker):
    
    model = joblib.load('linear_model.pkl')
    
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
    
    data = np.asarray([data])
    
    
    return model.predict(data)


