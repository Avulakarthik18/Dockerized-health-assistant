import os
import pickle
import warnings
import streamlit as st
from streamlit_option_menu import option_menu

warnings.filterwarnings("ignore")

# Set page configuration
st.set_page_config(page_title="Health Assistant", layout="wide", page_icon="💡")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetics_model = pickle.load(open(f'{working_dir}/Saved_models/diabetics_model.sav','rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/Saved_models/heart_disease_model.sav','rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/Saved_models/parkinsons_model.sav','rb'))

page_bg_img = """
<style>
   [data-testid="stForm"]{
       background-color: grey;   
   }
   [data-testid="stSidebarContent"]{
       background-color: lightgreen; 
   }
   [data-new-gr-c-s-check-loaded="14.1165.0" data-gr-ext-installed=""].body{
       background-color: lightgreen;
   }
   .st-bt{
       background-color: white;
   }
   .st-ch{
       caret-color: white;
   }
   .st-bx{
       color: white;  
       }
    .st-bs {
    border-bottom-color: white;
    }
    .st-br {
        border-top-color: white;
    }
    .st-bq {
        border-right-color: white;
    }
    .st-bp {
        border-left-color: white;
    }
    .menu .container-xxl[data-v-5af006b8] {
    background-color: red;
    border-radius: .5rem;
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetics Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           menu_icon = 'hospital-fill',
                           icons =['activity','heart','person'],
                           default_index = 0)

if selected == 'Diabetics Prediction':
    st.title('Diabetes Prediction using Machine learning.')
    
    
    with st.form(key="my_form",clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            Insulin = st.text_input('Insulin Level')

        with col2:
            SkinThickness = st.text_input(label='Skin Thickness Value')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

        with col2:
            Age = st.text_input("Age of the person")
        
        diab_diagnosis = "☝️ Results will displayed here...."

        if st.form_submit_button("Results"):
            user_input =[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                          BMI, DiabetesPedigreeFunction, Age]
            if "" in user_input:
                st.error("Please fill, all the details....",icon="😓")
            else:   
                user_input = [float(x) for x in user_input]    

                diab_prediction = diabetics_model.predict([user_input])

                if diab_prediction[0] == 1:
                    diab_diagnosis = 'The person is diabetic'
                else:
                    diab_diagnosis = 'The person is not diabetic'

        st.success(diab_diagnosis)
                               
if selected == 'Heart Disease Prediction':
    # page title
    st.title('Heart Disease Prediction using ML')
                     
    with st.form(key="my_form",clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        switch1, switch2, switch3 = st.columns(3)

        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Sex')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

        # code for Prediction
        heart_diagnosis = "☝️ Results will displayed here...."

        # creating a button for Prediction


        if st.form_submit_button("Results"):
                user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
                if "" in user_input:
                    st.error("Please fill, all the details....",icon="😒")
                else:
                    user_input = [float(x) for x in user_input]

                    heart_prediction = heart_disease_model.predict([user_input])

                    if heart_prediction[0] == 1:
                        heart_diagnosis = 'The person is having heart disease'
                    else:
                        heart_diagnosis = 'The person does not have any heart disease'

            
        st.success(heart_diagnosis)

if selected == 'Parkinsons Prediction':
    st.title("Parkinson's Disease Prediction using ML")

    
    with st.form(key="my_form",clear_on_submit=True):
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            fo = st.text_input('MDVP:Fo(Hz)')

        with col2:
            fhi = st.text_input('MDVP:Fhi(Hz)')

        with col3:
            flo = st.text_input('MDVP:Flo(Hz)')

        with col4:
            Jitter_percent = st.text_input('MDVP:Jitter(%)')

        with col5:
            Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

        with col1:
            RAP = st.text_input('MDVP:RAP')

        with col2:
            PPQ = st.text_input('MDVP:PPQ')

        with col3:
            DDP = st.text_input('Jitter:DDP')

        with col4:
            Shimmer = st.text_input('MDVP:Shimmer')

        with col5:
            Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

        with col1:
            APQ3 = st.text_input('Shimmer:APQ3')

        with col2:
            APQ5 = st.text_input('Shimmer:APQ5')

        with col3:
            APQ = st.text_input('MDVP:APQ')

        with col4:
            DDA = st.text_input('Shimmer:DDA')

        with col5:
            NHR = st.text_input('NHR')

        with col1:
            HNR = st.text_input('HNR')

        with col2:
            RPDE = st.text_input('RPDE')

        with col3:
            DFA = st.text_input('DFA')

        with col4:
            spread1 = st.text_input('spread1')

        with col5:
            spread2 = st.text_input('spread2')

        with col1:
            D2 = st.text_input('D2')

        with col2:
            PPE = st.text_input('PPE')

        # code for Prediction
        parkinsons_diagnosis = "☝️ Results will displayed here...."

        # creating a button for Prediction    
        if st.form_submit_button("Results"):
        
            user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                          RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                          APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
            if "" in user_input:
                st.error("Please fill, all the details....",icon="😒")
            else:
                user_input = [float(x) for x in user_input]

                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

        st.success(parkinsons_diagnosis)
