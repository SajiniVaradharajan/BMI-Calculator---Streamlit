
import streamlit as st


st.title('Welcome to BMI Calculator - Created by Sajini Varadharajan')
st.text('HPL Focus:')
st.text('ACPs: Connection Finding (Linking to Science),')
st.text('VAAs: Creative and Enterprising (Making an App)')

weight = st.number_input("Enter your weight (in kgs)")

status = st.radio('Select your height format: ',
                  ('cms', 'meters', 'feet'))


if (status == 'cms'):
    height = st.number_input('Centimeters')

    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.text("Enter your height")

elif (status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:

    height = st.number_input('Feet')


    try:
        bmi = weight / (((height / 3.28)) ** 2)
    except:
        st.text("Enter some value of height")


if (st.button('Calculate BMI')):


    st.text("Your BMI Index is {}.".format(bmi))


    if (bmi < 16):
        st.error("You are Extremely Underweight. Add extra calories to your meals and increase frequency of meals.")
    elif (bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight. Nutrient-rich food and exercise should be your priority.")
    elif (bmi >= 18.5 and bmi < 25):
        st.success("You are Healthy. Health is wealth. Good going!")
    elif (bmi >= 25 and bmi < 30):
        st.warning("You are Overweight. Stay hydrated and eat mindfully.")
    elif (bmi >= 30):
        st.error("You are Obese. Choosing healthy foods, limiting unhealthy foods, reducing beverages and "
                 "increasing physical activity will be of help.")