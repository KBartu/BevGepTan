import streamlit as st
import pickle

#python -m streamlit run app.py

loaded_model = pickle.load(open('dtClassifier.sav','rb'))

st.write("""
         # LA Crimes Classification
         Koltai Barnabás - EI52B1
         """)

def click():
    st.session_state.bt = True

def pred():
    st.session_state.pred = True

def predOff():
    st.session_state.pred = False

def reset():
    st.session_state.bt = False
    st.session_state.pred = False
    st.session_state.links = False

def lnk():
    st.session_state.links = True

if('bt' not in st.session_state):
    st.session_state.bt = False
    st.session_state.pred = False
    st.session_state.links = False

if(st.session_state.bt is False):
    startButton = st.button('Start the classification', on_click=click)
    linksButton = st.button('Links', on_click=lnk)
    if(st.session_state.links):
        st.write('Dataset: https://www.kaggle.com/datasets/chaitanyakck/crime-data-from-2020-to-present?select=Crime_Data_from_2010_to_2019.csv')
        st.write('Git Repository: https://github.com/KBartu/BevGepTan')
        st.button('Close Links', on_click=reset)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

def saveResult(res):
    f = open('result.txt','w')
    f.write(str(res))
    f.close()
def getResult():
    f = open('result.txt','r')
    return f.read()

if(st.session_state.bt and st.session_state.pred is False):
    with col1:
        col1_data = st.number_input('Area ID', min_value=0, value=0, step=1)
    with col2:
        col2_data = st.number_input('Crime ID', min_value=0, value=0, step=1)
    with col3:
        col3_data = st.number_input('Age', min_value=0, value=0, step=1)
    with col4:
        col4_data = st.number_input('Descent ID', min_value=0, value=0, step=1)
    with col5:
        col5_data = st.number_input('Premis ID', min_value=0, value=0, step=1)
    with col6:
        col6_data = st.number_input('Weapon ID', min_value=0, value=0, step=1)
    with col7:
        col7_data = st.number_input('Location ID', min_value=0, value=0, step=1)
  
    PredictionButton = st.button('Predict the sex of the victim')
    if(PredictionButton):
        prediction = loaded_model.predict([[col1_data,col2_data,col3_data,col4_data,col5_data,col6_data,col7_data]])
        saveResult(prediction)
        pred()

if(st.session_state.pred):
    res = getResult()
    if(res == '[0]'):
        st.write('Az áldozat nő volt!')
    if(res == '[1]'):
        st.write('Az áldozat férfi volt!')
    restart = st.button('New Classification', on_click=predOff)
    mainPage = st.button('Main Page', on_click=reset)
    #if(restart):
        #st.session_state.bt = False
        #st.session_state.pred = False




#nő
#prediction = loaded_model.predict([[6,0,47,0,0,0,0]])
#férfi
#prediction = loaded_model.predict([[1,2,51,2,2,2,2]])

