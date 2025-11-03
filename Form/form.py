import streamlit as st

st.markdown("<h1 style='text-align:center;'>User RegistrationForm</h1>",unsafe_allow_html=True)
# method-1
# form=st.form("form-1")
# form.text_input("First name")
# form.form_submit_button("Submit")
#method-2

with st.form("form-2",clear_on_submit=True):
    col1,col2=st.columns(2)
    f_name= col1.text_input("First name")
    l_name=col2.text_input("Last name")
    st.text_input("Email",type="default")
    st.text_input("Password",type="password")
    st.text_input("Confirm Password",type="password")
    day,month,year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    btn_status=st.form_submit_button("submit")
    if btn_status:
        if f_name=="" and l_name=="":
            st.warning("Please fill above field")
        else:
            st.success("Submitted Successfully")
        

