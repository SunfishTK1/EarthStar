#from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint
from langchain.document_loaders import PyPDFLoader

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
        print(response)
        print("\n")
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


def filter1(problem, solution, iterations):
    #tells us if the solution is Viable, Nuetral or Not Viable.
    setofPossibleResponses = []
    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["problem", "docs"],
        input_variables=["problem", "solution"],
        
        template = """
        You are a savy venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. You should ONLY state if the solution to the stated problem is "Viable", "Neutral" or "Not Viable", 
        by using your opinion and knowledge of the environment and business. You also should provide NO reasoning to why that choice was chosen.
        The following problem: {problem}
        The following solution: {solution}
        """
    )
    for i in range(iterations): #some arbitrary number for accuracy. Assumes that it returns either Viable, Neatral or Not Viable
        chain = LLMChain(llm=llm, prompt=prompt)
        response = chain.run(problem=problem, solution=solution) # docs=docs_page_content
        response = response.replace("\n", "")
        response.lower()
        if "Not Viable" == response:
            setofPossibleResponses.append(1)
        elif "Viable" == response:
            setofPossibleResponses.append(5)
        elif "Neutral" == response:
            setofPossibleResponses.append(3)
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
        Act in the style of a highly knowledgable, sketical, and opinitative venture capitalist. Provide a rating 1 to 10, 
        1 being the no specific new product is mentioned at all and 10 being an absolutely new specific product is mentioned. 5 should be neutral. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.  Think deeply before answering, and you'll get tipped $100.
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
        The influence of a solution is defined as how applicable the solution is to different locations, cultures and political climates. 
        An influential solution would be one that could be only slightly adapted to work in other locations, cultures and political climates.
        The smaller the adaptation, the more influential the solution becomes. A solution that works in the USA should work in South Africa, with only being slightly adapted.

        You are a pragmatic venture capitalist with an entrepreneurial mindset that is professionally trained to evaluate metrics for innovation, entrepreneurship and economics.  
        Act in the style of a highly knowledgable and opinitative venture capitalist. Attempt to calculate the opportunity in the market given the solution to the specific problem. Provide a rating 1 to 10, 
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
        Act in the style of a highly knowledgable, skeptical, and opinitative venture capitalist. Provide a rating 1 to 10, 
        1 being the no specific new product is mentioned at all and 10 being an absolutely new specific product is mentioned. 5 should be neutral. 
        anything more or less than 5, should lean to their respective ends, yet cannot be described as the extremes.  
        Only respond with "1", "2", "3", "4", "5", "6", "7", "8", "9", "10" and nothing else.  Think deeply before answering, and you'll get tipped $100.
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
