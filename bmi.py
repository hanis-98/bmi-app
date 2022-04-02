import streamlit as st

st.title('BMI Calculator ✨')
st.markdown("""
This app will calculate your BMI""")

st.subheader('Measurement System Preferred')
st.write("""
The **Metric System** uses meter(m) for height and kilogram(kg) for weight.
\nMeanwhile, the **Imperial System** uses feet(ft) and pound(Lbs) respectively.""")

userchoice = st.container()
with userchoice:
    choose = st.selectbox('System Preferred', ["Choose...","Metric System", "Imperial System"])

    st.write('You have chosen: ' + str(choose))

    if choose in ['Choose...']:
        st.write("Choose a system first")

    if choose in ['Metric System']:
        heightM = st.number_input('Height', 1.3, 2.0, 1.6)
        weightM = st.number_input('Weight', 35, 200, 55)
        bmiM = weightM/(heightM*heightM)

        bmi = bmiM
        bmidisp = "{:.2f}".format(bmiM)
        st.write('\nYour BMI is ' + str(bmidisp))

    if choose in ['Imperial System']:
        heightIf = st.number_input('Height (ft)', 5)
        heightIi = st.slider('Height (inch)', 0,12,6)
        weightI = st.number_input('Weight (lbs)', 100)

        heightI = (heightIf*12)+heightIi
        bmiI = (703*weightI)/(heightI*heightI)
        bmi = bmiI
        bmidisp = "{:.2f}".format(bmiI)
        st.write('\nYour BMI is ' + str(bmidisp))


bodytype = st.container()
with bodytype:
    if choose in ['Choose...']:
        st.write(' ')

    else:
        if (bmi < 18.5):
            st.write('From your BMI, you are underweight')
        if ((bmi>=18.5) and (bmi < 25)):
            st.write('From your BMI, you have the ideal weight for your height')
        if((bmi>=25) and (bmi<30)):
            st.write('You are an overweight')
        if((bmi>=30)):
            st.write('You are obese')
