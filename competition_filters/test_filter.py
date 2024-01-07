import streamlit as st
import filters as fil



st.title("EarthStar Team")

with st.sidebar:
    with st.form(key="my_form"):
        query = st.sidebar.text_area(
            label = "What are your academic interests?",
            max_chars=3000, #100
            key="query"
        )

        submit_button = st.form_submit_button(label='Submit')

if query and submit_button:
    response = fil.test(query) # Change this to test out filters!
    st.subheader("Answer: ")
    repo = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">' + response + '</p>'
    st.markdown(repo, unsafe_allow_html=True)