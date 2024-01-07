import streamlit as st
import filters as fil
import evaluate as eval



st.title("EarthStar Team                                        ")

with st.sidebar:
    with st.form(key="my_form"):
        problem = st.sidebar.text_area(
            label = "What is the circular economy business problem?",
            max_chars=3500, #100
            key="problem"
        )

        solution = st.sidebar.text_area(
            label = "What is the circular economy business solution?",
            max_chars=3500, #100
            key="solution"
        )

        submit_button = st.form_submit_button(label='Submit')



overall_color = "green"
sustainability_color = "green"
social_color = "green"
business_color = "green"
novelty_color = "green"
coherence_color = "green"

overall_score = 0
sustainability_score = 0
social_score = 0
business_score = 0
novelty_score = 0
coherence_score = 0

if problem and solution and submit_button:
    response = fil.monopoly2(problem, solution, 1) # Change this to test out filters!
    st.subheader("The Monopoly Power of this Idea is: ")
    repo = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">' + str(response) + '</p>'
    st.markdown(repo, unsafe_allow_html=True)
    with st.container():
        col0, col1, col2 = st.columns(3)

        with col0:
            with st.container():
                st.subheader(":" + overall_color + "[Overall Score]")
    
        with col1:
            with st.container():
                st.subheader(":" + overall_color + "[Sustainability Score]")

        with col2:
            st.subheader(":" + overall_color + "[Social Inclusion Score]")
    
    col0, col1, col2 = st.columns(3)

    with col0:
        st.metric(label="Excellent", value=overall_score)
    
    with col1:
        st.metric(label="Excellent", value=overall_score)

    with col2:
        st.metric(label="Excellent", value=overall_score)

    col3, col4, col5 = st.columns(3)

    with col3:
        st.header("Business")

    with col4:
        st.header("Novelty")

    with col5:
        st.header("Business Plan Coherence")
