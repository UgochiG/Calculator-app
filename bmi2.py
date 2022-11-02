import streamlit as st


w=st.sidebar.number_input("What is your weight\n",step=1)
h=st.sidebar.number_input("What is your height in meters\n",step=1)
st.selectbox('Choose your Gender',['Male','Female'])

if st.button('Calculate'):
    BMI=(w/(h**2))
    BMI=round(BMI,1)
    
    if BMI < 18.5:
        st.write(f"Your BMI is :{BMI}\nUnderweight")
    elif 18.4< BMI < 25:
        st.write(f"Your BMI is :{BMI}\nNormal")
    elif 24.9< BMI < 30:
        st.write(f"Your BMI is :{BMI}\nOverweight")
    elif 29.9< BMI < 35:
        st.write(f"Your BMI is :{BMI}\nClass 1 Obesity")
    elif 34.9< BMI < 40:
        st.write(f"Your BMI is :{BMI}\nClass 2 Obesity")
    else:
        st.write(f"Your BMI is :{BMI}\nExtreme Obesity")
        
st.image('bae.jpeg')

