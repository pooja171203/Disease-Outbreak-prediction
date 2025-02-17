import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="👩‍⚕️")

diabetes_model=pickle.load(open(r"diabetes_model.sav","rb"))
heart_disease_model=pickle.load(open(r"heart_disease_model.sav","rb"))
parkinsons_model=pickle.load(open(r"parkinsons_model.sav","rb"))
with st.sidebar:
    selected=option_menu("Prediction of disease outbreak system",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"],
                         menu_icon="hospital.fill",icons=["activity","heart","person"],default_index=0)
if selected=="Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies = st.text_input("Number of pregnancies")
    with col2:
        Glucose = st.text_input("Glucose Level")
    with col3:
        BloodPressure = st.text_input("Blood Pressure value")
    with col1:
        SkinThickness= st.text_input("Skin Thickness value")
    with col2:
        Insulin = st.text_input("Insulin Level")
    with col3:
        BMI = st.text_input("BMI value")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function")
    with col2:
        Age=st.text_input("Age of the person")

    diab_diagnosis=''    
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction=diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is not diabetic'  
    st.success(diab_diagnosis)
if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        age = st.text_input("Age of the person")
    with col2:
        gender = st.text_input("Enter Gender")
    with col3:
        cp = st.text_input("cp value")
    with col1:
        trestbps= st.text_input("trestbps value")
    with col2:
        chol = st.text_input("chol Level")
    with col3:
        fbs = st.text_input("fbs value")
    with col1:
        restecg=st.text_input("restecg value")
    with col2:
        thalach=st.text_input("thalach value")
    with col3:
        exang = st.text_input("exang")
    with col1:
        oldpeak= st.text_input("oldpeak value")
    with col2:
        slope = st.text_input("slope")
    with col3:
        ca = st.text_input("ca value")
    with col1:
        thal=st.text_input("thal")
    

    heart_diagnosis=''    
    if st.button('Heart Disease Test Result'):
        user_input=[age,gender,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction=heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis='The Person has Heart Disease'
        else:
            heart_diagnosis='The Person has no heart disease'  
    st.success(heart_diagnosis)
elif selected=="Parkinsons Prediction":
    st.title("Parkinsons Disease Prediction using ML")

    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            MDVPFo = st.text_input("MDVP:Fo(Hz)")
            MDVP_Jitter = st.text_input("MDVP:Jitter(%)")
            MDVP_Shimmer = st.text_input("MDVP:Shimmer")
            Shimmer_APQ3 = st.text_input("Shimmer:APQ3")
            MDVP_APQ = st.text_input("MDVP:APQ")
            NHR = st.text_input("NHR")
            RPDE = st.text_input("RPDE")
            spread1 = st.text_input("spread1")
            D2 = st.text_input("D2")

        with col2:
            MDVP_Fhi = st.text_input("MDVP:Fhi(Hz)")
            Insulin = st.text_input("MDVP:Jitter(Abs)")
            MDVP_Shimmer_dB = st.text_input("MDVP:Shimmer(dB)")
            Shimmer_APQ5 = st.text_input("Shimmer:APQ5")
            Shimmer_DDA = st.text_input("Shimmer:DDA")
            HNR = st.text_input("HNR")
            DFA = st.text_input("DFA")
            spread2 = st.text_input("spread2")
            PPE = st.text_input("PPE")

        with col3:
            MDVP_Flo = st.text_input("MDVP:Flo(Hz)")
            MDVP_RAP= st.text_input("MDVP:RAP")
            MDVP_PPQ = st.text_input("MDVP:PPQ")
            Jitter_DDP = st.text_input("Jitter:DDP")

    park_diagnosis=''    
    if st.button('Parkinsons Test Result'):
        user_input = [
    "MDVPFo", "MDVP_Fhi", "MDVP_Flo", "MDVP_Jitter", "MDVP_JitterAbs", "MDVP_RAP", 
    "MDVP_PPQ", "Jitter_DDP", "MDVP_Shimmer", "MDVP_Shimmer_dB", "Shimmer_APQ3", "Shimmer_APQ5", 
    "MDVP_APQ", "Shimmer_DDA", "NHR", "HNR", "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
    ]        
        user_input=[float(x) for x in user_input]
        park_prediction=parkinsons_model.predict([user_input])
        if park_prediction[0]==1:
            park_diagnosis='The Person has Parkinsons Disease'
        else:
            park_diagnosis='The Person has no Parkinsons Disease'  
    st.success(park_diagnosis)