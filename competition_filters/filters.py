#from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
#from langchain.vectorstores import FAISS
from dotenv import load_dotenv
#from langchain.document_loaders import JSONLoader
import json
#from pathlib import Path
from pprint import pprint
#from langchain.document_loaders import PyPDFLoader

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()

embeddings = OpenAIEmbeddings() # use embeddings from OpenAI

def get_vector_loaded_db():
    return FAISS.load_local("./", OpenAIEmbeddings(), "undergraduate_catalog")

def get_response_from_query(query):
    # text-davinci can hand 4097 tokens
    # What courses do you recommend?
    #docs = db.similarity_search(query, k=k) # narrows down the course data to specifically search to the ones similar to the query based on embeddings
    #docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        input_variables=["problem"],
        template = """
        You are a savy venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable and opinitative venture capitalist.  
        Answer the following problem:  {problem}
        By using your opinion and knowledge of the environment and business.
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=query) # docs=docs_page_content
    response = response.replace("\n", "")
    return response

def finalJustification(problem, solution, finalValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "finalValue"],
        template = """
        
        Coherence is defined as using data to support the given solution, being gramatically correct, and sounding feasible and realistic.
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {finalValue} out of 100 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {finalValue} out of 100 points. The idea is a circular economy business idea and the
        following metrics of social reach and good, sustainability, business viability, noveltly, and coherence of business plan were used.
        
        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {finalValue} out of 100 points.
        Mention the {finalValue} out of 100 points, and imply that anything above 80 points is a good solution.
        Be concise with your answer, please round the {finalValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, finalValue=finalValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response

def businessJustification(problem, solution, businessValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "businessValue"],
        template = """
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {businessValue} out of 10 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {businessValue} out of 10 points. The {businessValue} should be supported using the aspects of marketsize, profitabilility, and its ability to compete
        with other competitors in the market.
        
        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {businessValue} out of 10 points.
        Mention the {businessValue} out of 10 points, and imply that anything above 8 points is a good solution in the business metric.
        Be concise with your answer, and make sure the output is LESS than 1300 characters.
        Please round the {businessValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, businessValue = businessValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response

def socialJustification(problem, solution, socialValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "socialValue"],
        template = """
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {socialValue} out of 10 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {socialValue} out of 10 points. The {socialValue} should be supported using the aspects of 
        social impact, social justice, social learning, and how likely diverse people are to adopt the idea.
        
        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {socialValue} out of 10 points.
        Mention the {socialValue} out of 10 points, and imply that anything above 8 points is a good solution in the social metric.
        Be concise with your answer, and make sure the output is LESS than 1300 characters.
        Please round the {socialValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, socialValue = socialValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response

def coherentJustification(problem, solution, coherentValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "coherentValue"],
        template = """
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {coherentValue} out of 10 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {coherentValue} out of 10 points. The {coherentValue} should be supported using the aspects of
        the punctutation, grammar and vocabulary of the problem and solution.
        
        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {coherentValue} out of 10 points.
        Mention the {coherentValue} out of 10 points, and imply that anything above 8 points is a good solution in the coherence metric.
        Be concise with your answer, and make sure the output is LESS than 1300 characters.
        Please round the {coherentValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, coherentValue = coherentValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response

def novelJustification(problem, solution, novelValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "novelValue"],
        template = """
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {novelValue} out of 10 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {novelValue} out of 10 points. The {novelValue} should be supported using the aspects of 
        the opportunity for the product to capitalize in the market and the innovative impact of the idea.


        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {novelValue} out of 10 points.
        Mention the {novelValue} out of 10 points, and imply that anything above 8 points is a good solution.
        Be concise with your answer, and make sure the output is LESS than 1300 characters.
        Please round the {novelValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, novelValue = novelValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response

def sustainabilityJustification(problem, solution, sustainabilityValue):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        #add the rating breakdown.
        input_variables=["problem", "solution", "sustainabilityValue"],
        template = """
        
        Imagine you are a team of consultants
        convincing a venture capital firm that an idea deserves a rating of {sustainabilityValue} out of 10 points at a meeting.  You a fierce salesman and argue 
        clearly and without doubt that the idea deserves a rating of {sustainabilityValue} out of 10 points. The {sustainabilityValue} should be supported using the aspects of 
        the opportunity for the product to capitalize in the market and the innovative impact of the idea.


        Use the following problem and solution pair to create your argument why the following business idea strongly deserves a rating of {sustainabilityValue} out of 10 points.
        Mention the {sustainabilityValue} out of 10 points, and imply that anything above 8 points is a good solution.
        Be concise with your answer, and make sure the output is LESS than 1300 characters.
        Please round the {novelValue} to the nearest tenth.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(problem=problem, solution=solution, novelValue = novelValue) # docs=docs_page_content
    response = response.replace("\n", "")
    #print(response)
    #print("\n")
    return response


def test(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        You are a savy venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. Provide a rating 1 to 10, 
        1 being the not a realistic solution at all and 10 being an extremely realistic solution. 5 should be neither realistic or not realistic. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and explain your answer.
        Use your opinion and knowledge of the environment and business.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def assignValue(response, setofPossibleResponses):
    if "1" == response:
        setofPossibleResponses.append(1)
    elif "2" == response:
        setofPossibleResponses.append(2)
    elif "4" == response:
        setofPossibleResponses.append(4)
    elif "5" == response:
        setofPossibleResponses.append(5)
    elif "3" == response:
        setofPossibleResponses.append(3)
    elif "6" == response:
        setofPossibleResponses.append(6)
    elif "7" == response:
        setofPossibleResponses.append(7)
    elif "8" == response:
        setofPossibleResponses.append(8)
    elif "9" == response:
        setofPossibleResponses.append(9)
    elif "10" == response:
        setofPossibleResponses.append(10)
    else:
        setofPossibleResponses.append(5.5)

def realismFilter(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        You are a savy venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. Provide a rating 1 to 10, 
        1 being the not a realistic solution at all and 10 being an extremely realistic solution. 5 should be neither realistic or not realistic. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.
        Use your opinion and knowledge of the environment and business.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def RelevanceToCircularity(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        The following describes a circular economy:
            In today’s rapidly evolving world, climate change stands as a formidable problem, deeply influencing our daily lives and the health of our planet. The circular economy, with its focus on reusing and recycling resources to minimize waste, emerges as a crucial strategy in this battle. Innovations like car-sharing platforms significantly reduce the carbon footprint of transportation, while modular designs in various products promote waste reduction by allowing individual components to be upgraded rather than discarding the entire item.

            In the face of climate change's criticality, the urgency to identify and implement high-impact circular economy solutions has never been greater. The challenge we confront today, however, extends beyond coming up with solutions to confront this problem. It lies in the daunting task of effectively evaluating a vast and diverse array of solutions, discerning the most impactful ones amidst a sea of possibilities. This process can be overwhelming, given the complexity and the sheer volume of potential solutions, leading to cognitive overload for human evaluators.

            AI EarthHack invites you to leverage the transformative power of generative AI in developing an AI-powered decision-support tool. Such a tool would not only streamline the evaluation process but also enhance the accuracy and efficiency of selecting the best solutions. By augmenting human judgment with AI’s analytical capabilities, we aim to spotlight those innovations that hold the most promise in addressing the pressing issue of climate change through the principles of the circular economy.

        You are a savy venture capitalist and social/climate activist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. Given the above ideals of a circular economy, you are attempted to determine relevancy of a hypothetical answer to the ideas of a circular economy (like recycling and sustainability, especially environmental sustainability). Provide a rating 1 to 10, 
        1 containing  and 10 being an extremely realistic solution. 5 should be neither realistic or not realistic. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.
        Use your opinion and knowledge of the environment and business.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations


#####
#Coherence
######

def realTech(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        Some ideas mention a very specific new technology such as using plastic bricks to build sustainable houses.  While other ideas lack specific mentions of technology, for example "I want to eliminate fossil fuels by using technology".

        There is a clear difference between having a specific product like plastic bricks as a solution, and not a specific product such as the second example which broadly uses the term technology as a solution and doesn't cite any examples.

        Your job is to determine whether specific products or technologies are explicitly mentioned, not explicitly mentioned, or noot present at all.
        
        You are a pragmatic and highly sketical venture capitalist, engineer, and computer scientist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable, sketical, and opinitative harsh critic. Provide a rating 1 to 10, 
        1 being the no specific new product is mentioned at all and 10 being an absolutely new specific product is mentioned. 5 should be neutral. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.  Think deeply before answering, and you'll get tipped $100.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def Influence(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        The influence of a solution is defined as how applicable the solution is to different locations, cultures and political climates. 
        An influential solution would be one that could be only slightly adapted to work in other locations, cultures and political climates.
        The smaller the adaptation, the more influential the solution becomes. A solution that works in the USA should work in South Africa, with only being slightly adapted.

        You are a social/climate activist that is professionally trained to evaluate metrics for social impact and influence.  
        Act in the style of a highly knowledgable and opinitative social/climate activist. Given the definition of influence above, attempt to calculate how widespread and influential the given solution is to the specific problem. Provide a rating 1 to 10, 
        1 being the least influential solution possible, and 10 being the most influential solution possible. 5 should be neither influential or non-influential. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.
        Use your opinion and knowledge political science, culture and climate.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def Opportunity(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        Opportunistic in the market should be defined as a product that can be capitalize on the lack of that product, or products similar in the market. To be opportunistic,
        these solutions must be requested by consumers.

        
        You are a pragmatic venture capitalist with an entrepreneurial mindset that is professionally trained to evaluate metrics for innovation, entrepreneurship and economics.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. Using the definition established of opportunistic, 
        attempt to calculate the opportunity in the market given the solution to the specific problem. Provide a rating 1 to 10, 
        1 being the least opportunistic solution possible, and 10 being the most opportunistic solution possible. 5 should be neither opportunistic or non-opportunistic. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.
        Use your opinion and knowledge innovation, entrepreneurship, economics and the market.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

####
#Resource Efficiency
####

def ResourceEfficiency(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """
        The influence of a solution is defined as how applicable the solution is to different locations, cultures and political climates. 
        An influential solution would be one that could be only slightly adapted to work in other locations, cultures and political climates.
        The smaller the adaptation, the more influential the solution becomes. A solution that works in the USA should work in South Africa, with only being slightly adapted.

        You are a venture capitalist, engineer and social activist that is professionally trained to evaluate metrics for resource management, economics and local resource availibility.  
        Act in the style of a highly knowledgable and opinitative venture capitalist, engineer and social activist. Attempt to calculate the resource efficiency given the solution to the specific problem. Provide a rating 1 to 10, 
        1 being the least resource efficient solution possible, and 10 being the most resource efficient solution possible. 5 should be neither resource efficient or non-resource efficeint. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.
        Use your opinion and knowledge resource management, engineering and earth science.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations


#########
#Novel Innovative Potential
########
def innovativeImpact(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        Your job is to determine whether a circular business model has innovative IMPACT! Impact is defined by: How much does the idea contribute to advancing the circular economy transition, by addressing a significant problem, creating a positive change, or generating a measurable outcome or benefit for the environment, society, or economy?

        You are also a pragmatic and highly skeptical venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable, skeptical, and opinitative harsh critic. Provide a rating from 1 to 10, 
        1 being the no innovative impact at all and 10 being an absolutely innovative impact. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

#########
#Business Potential
###########

def revenue(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a pragmatic and highly skeptical chief financial officer that is professionally trained to evaluate the profitability of business ideas.  
        Act in the style of a highly knowledgable, skeptical, and opinitative harsh critic. Your job is to evaluate whether the provided problem and solution business idea pair can be highly profitable by providing a rating. 
        Provide a rating from 1 to 10, 
        1 being 'not profitable likely to lose money' and 10 being an 'highly profitable ability to create billions in profits'.   These are extremes.
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def marketSize(problem, solution, iterations):
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a pragmatic and highly skeptical chief financial officer that is professionally trained to evaluate the marketsize of business ideas.  
        Act in the style of a highly knowledgable, skeptical, and opinitative harsh critic. Your job is to evaluate whether the provided problem and solution business idea pair have a large or small market size by providing a rating. 
        Provide a rating from 1 to 10, 
        1 being 'extremely small market size 1 to 100 end users' and 10 being an 'extremely large market size 5 to 7 billion end users'.   These are extremes. 5 would be like "moderate market size 100,000 to 500,000 end users".
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def monopoly(problem, solution, iterations): #Best Filter Performance thus far, Instruct model to strictly evaluate only one category.
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a pragmatic and highly skeptical investment analyst that is professionally trained to evaluate if a business ideas have existing market competition.  
        Act in the style of a highly knowledgable, skeptical, and opinitative harsh critic. Your job is to only evaluate whether the provided problem and solution business idea pair have exsiting market competition.
        1 being 'large amount of market competitors' and 10 being 'no competition against this product'.   These are extremes.
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

#############
#Social Impact/Inclusion
##############

def socialImpact(problem, solution, iterations): #Best Filter Performance thus far, Instruct model to strictly evaluate only one category.
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a climate activist acting as a judge to evaluate the social inclusion of buissness ideas.
        Act in the style of a highly knowledgable, skeptical, critical judge. Your job is to only evaluate to what extent the provided problem and solution business idea pair have social impact.
        In this contest, Social Impact is defined by: "How much does the idea improve the well-being, empowerment, and participation of the people involved or affected by the circular practices, especially those who are marginalized, vulnerable, or disadvantaged?"

        1 being 'extremely harmful social impact' and 10 being 'extremely beneficial social impact'.   These are extremes. 5 being neutral "neglible social impact".
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def socialJustice(problem, solution, iterations): #Best Filter Performance thus far, Instruct model to strictly evaluate only one category.
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a social justice activist acting as a judge to evaluate the social justice of buissness ideas.
        Act in the style of a highly knowledgable, skeptical, critical judge. Your job is to only evaluate to what extent the provided problem and solution business idea pair have social justice.
        In this contest, Social Justice is defined by: "How much does the idea promote fairness, equality, and human rights in the distribution of benefits and burdens of the circular practices, as well as in the recognition and representation of diverse voices and interests?"

        1 being 'hurts social justice' and 10 being 'improves social justice'.   These are extremes. 5 being neutral "neglible impact on social justice".
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def socialLearning(problem, solution, iterations): #Best Filter Performance thus far, Instruct model to strictly evaluate only one category.
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

        You are also a education activist acting as a judge to evaluate the social justice of buissness ideas.
        Act in the style of a highly knowledgable, skeptical, critical judge. Your job is to only evaluate to what extent the provided problem and solution business idea pair promote social learning.
        In this contest, Social Learning is defined by: "How much does the idea facilitate the acquisition, sharing, and application of knowledge, skills, and values that enable the transition to a more inclusive and circular economy?"

        1 being 'hurts social learning' and 10 being 'improves social learning'.   These are extremes. 5 being neutral "neglible impact on social learning".
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10" and nothing else.  Think deeply before answering, and you'll get tipped $100 for a perfect job.
        Use your opinion and knowledge of the environment and business.
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def monopoly2(problem, solution, iterations): #Best Filter Performance thus far, Instruct model to strictly evaluate only one category.
    #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

       You are to determine the monopoly power potential of a business idea. Your sole job is to determine whether the idea/product will face competition in the market. Give the product a rating of 1 to 10. 1 being no monopoly and 10 being monopoly.
       Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10".
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations

def coherenceGeneral(problem, solution, iterations):
        #tells 1 through 10 rating, for filter 1.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        #play different roles
        input_variables=["problem", "solution"],
        template = """

       You are an english professor grading how coherent the problem and solution are. This means that it contains correct punctution, accurate vocabulary, and uses words commonly heard in the English language in 2024. Give the problem and solution a rating from 1 to 10,
       1 being the least coherent imaginable, and 10 being perfectly coherent.
       Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", or "10".
        Use the following problem and solution pair to create your rating.
        The following problem: {problem}
        The following solution: {solution}
        """
        )
    
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either realistic, Neatral or Not realistic
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        #print(response)
        #print("\n")
        assignValue(response, setofPossibleResponses)
    Sum = sum(setofPossibleResponses)
    return Sum/iterations