import pandas as pd
import streamlit as st
with st.form("my_form",clear_on_submit=True):
    students = pd.read_csv('cookies.csv')
    colt, coli = st.columns(2)
    with colt:
        st.title("My students deserve it...")
    with coli:
        st.text('OM NOM NOM')
        st.image('cartoon-cookie.gif',width = 75)

    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    col1, col2= st.columns([1,2])

    with col1:
        st.title('Students')
    with col2:
        st.image('cartoon-cookie.gif',width = 70)
    list_of_checkbox = []
    list_of_columns = []
    list_of_two=[]

    for i,student in enumerate(students['Students']):
        list_of_two[0:1] = st.columns([1,2])
        list_of_columns.append(list_of_two)
        with list_of_columns[i][0]:
            list_of_checkbox.append(st.checkbox(student,key=student,value=False))
        with list_of_columns[i][1]:
            st.text(students.iloc[i]['cookies'])

    # st.button('GIVE THIS MAN A COOKIE!')
    if st.form_submit_button('GIVE THIS MAN A COOKIE!'):
        for i, box in enumerate(list_of_checkbox):
            if (box == True):
                students.iloc[i,1] += 1
                st.balloons()
        students.to_csv('cookies.csv',index=False)
        st.experimental_rerun()