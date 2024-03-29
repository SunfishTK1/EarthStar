import streamlit as st
import starter as lch
import textwrap

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
    #db = lch.get_vector_loaded_db()
    response = lch.get_response_from_query(query)
    #docs = response = lch.get_response_from_query(db, query)
    st.subheader("Answer: ")
    #st.text(textwrap.fill(response, width = 80))
    repo = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">' + response + '</p>'
    st.markdown(repo, unsafe_allow_html=True)