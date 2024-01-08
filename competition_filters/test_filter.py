import streamlit as st
import filters as fil
import fevaluate as eval



st.title("EarthStar")

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

if not (problem or solution):
    st.markdown(":red[Please Enter A Circular Economy Business Problem and Corresponding Solution]")

if problem and solution and submit_button:
    data = eval.runEvaluate(problem, solution)
    overall_score = data[0]
    sustainability_score = data[1]
    social_score = data[2]
    business_score = data[3]
    novelty_score = data[4]
    coherence_score = data[5]

    if(overall_score < 60):
        overall_color = "red"
    elif(overall_score < 80):
        overall_color = "orange"
    else:
        overall_color = "green"
    
    if(sustainability_score < 6):
        sustainability_color = "red"
    elif(sustainability_score < 8):
        sustainability_color = "orange"
    else:
        sustainability_color = "green"

    if(social_score < 6):
        social_color = "red"
    elif(social_score < 8):
        social_color = "orange"
    else:
        social_color = "green"

    if(business_score < 6):
        business_color = "red"
    elif(business_score < 8):
        business_color = "orange"
    else:
        business_color = "green"
    
    if(novelty_score < 6):
        novelty_color = "red"
    elif(novelty_score < 8):
        novelty_color = "orange"
    else:
        novelty_color = "green"

    if(coherence_score < 6):
        coherence_color = "red"
    elif(coherence_score < 8):
        coherence_color = "orange"
    else:
        coherence_color = "green"

    #response = fil.monopoly2(problem, solution, 1) # Change this to test out filters!
    #st.subheader("The Monopoly Power of this Idea is: ")
    #repo = '<p style="font-family:sans-serif; color:Black; font-size: 20px;">' + str(response) + '</p>'
    #st.markdown(repo, unsafe_allow_html=True)
    with st.container():
        col0, col1, col2 = st.columns(3)

        with col0:
            with st.container():
                st.subheader(":" + overall_color + "[Overall Score]")
    
        with col1:
            with st.container():
                st.subheader(":" + sustainability_color + "[Sustainability Score]")

        with col2:
            st.subheader(":" + social_color + "[Social Inclusion Score]")
    
    col0, col1, col2 = st.columns(3)

    with col0:
        st.metric(label="out of 100 points", value=round(overall_score, 1))
    
    with col1:
        st.metric(label="out of 10 points", value=round(sustainability_score, 1))

    with col2:
        st.metric(label="out of 10 points", value=round(social_score, 1))

    
    with st.container():
        
        col3, col4, col5 = st.columns(3)

        with col3:
            st.subheader(":" + business_color + "[Business Score]")

        with col4:
            st.subheader(":" + novelty_color + "[Novelty Score]")

        with col5:
            st.subheader(":" + coherence_color + "[Idea Coherence Score]")

        col3, col4, col5 = st.columns(3)

    with col3:
        st.metric(label="out of 10 points", value=round(business_score, 1))
    
    with col4:
        st.metric(label="out of 10 points", value=round(novelty_score, 1))

    with col5:
        st.metric(label="out of 10 points", value=round(coherence_score, 1))

    with st.container():
        overall = st.expander("Overall Score Explanation")
        overall.write(data[6])
        sustainability = st.expander("Sustainability Score Explanation")
        sustainability.write(data[7])
        social = st.expander("Social Inclusion Score")
        social.write(data[8])
        business = st.expander("Business Score")
        business.write(data[9])
        novel = st.expander("Novelty Score")
        novel.write(data[10])
        coherence = st.expander("Idea Coherence Score")
        coherence.write(data[11])

