from re import I
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import joblib

st.set_page_config(page_title = "My Webpage", page_icon=":tada:", layout = "wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
filename = 'finalized_model.sav'
test = [[0, 0, 0,0,0,0,0,0, 0, 0,  0]]
test2 = []
loaded_model = joblib.load(filename)
result = loaded_model.predict(test)
print(result)

with st.container():
    st.subheader("Hi, We ara The Matrix :wave:")
    st.title("A Data analysis site for the MonkeyPox Virus")
    st.write(result)
    st.write("Let creat a world free from MonkeyPox")
    st.write("[Learn More >](https://www.linkedin.com/in/africandatascientist/)")

    lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_nkmkuqhm.json")
    img_contact_form = Image.open("images/Image2-scaled.jpg")
   


    with st.container():
        st.write("---")
        left_column, right_column =  st.columns(2)
        with left_column:
            st.header("What we do")
            st.write("##")
            st.write(
                """
                To predict whether a patient is negative or positive for monkeypox based on the symptoms they exhibit
                To analyze the various variables such as Sore Throat,Penile Oedema, Oral Lesions ,Systemic illness and STIs and know their relationship with monkeypox
                """
            )
            st.write("[Company >](https://www.moringa.com)")

with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("View your Monkeypox status today")
        st.write(
            """
            Add all your symptoms here to know if you may have MonkeyPox.
            Prevention is better than cure guys

            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=Z_BHtuz8Em0&ab_channel=CNN)")

with st.container():
    st.write("---")
    left_column, right_column =  st.columns(2)
    with left_column:
        with st.form('form1', clear_on_submit=True):
            st.header("Run your test")
           # name = st.text_input('Enter Ofueneke')
            #age = st.text_input('Enter age')
            #sex = st.text_input('Enter sex')
            illnesses = ['Fever','Muscle Aches & Pain','Swolen Lymph Nodes', 'Rectal Pain', 'Sore Throat', 'Penile Oedema',
                            'Oral Lesions', 'Solitary Lesion', 'Swollen Tonsils', 'HIV Infection',
                             'STI']
            for x in illnesses:
                
                x= st.checkbox(x)
                if x:
                    test2.append(1)
                else:
                    test2.append(0)
            st.form_submit_button()

           
            #st.write(test2)

            if len(test2) == 11:
                filename = 'finalized_model.sav'
                test = [test2]
                loaded_model = joblib.load(filename)
                result = loaded_model.predict(test)
                       
                if result == 1:
                    st.warning("70% chance of beng Positive ")
                    st.write("You may be having MonkeyPox Virus Kindly Visits the nearest hospital for a Test")
                else:
                    st.success("Virus Free")
                    st.write("You are may not be having the Monkeypox Virus But to be sure get a test")

            

            

    
          
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding1")



