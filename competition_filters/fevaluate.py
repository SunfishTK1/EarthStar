import filters as fil

import csv
id = []
problems = []
solutions = []

with open('AI_EarthHack_Dataset.csv', mode ='r', encoding="latin1")as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        id.append(lines[0])
        problems.append(lines[1])
        solutions.append(lines[2])
        ##print(lines)


def retQuality100(score):
    if(int(score) < 60 ):
        return "Very Bad"
    elif(int(score) < 80 ):
        return "Mediocre"
    else:
        return "Exceptional"
    
    
def retQuality10(score):
    if(int(score) < 6 ):
        return "Very Bad"
    elif(int(score) < 8 ):
        return "Mediocre"
    else:
        return "Exceptional"

def runEvaluate(problem, solution):
    vals = []
    sustainability = []
    business = []
    social = []
    novel = []
    coherent = []

    vals_final = []
    sustainability_final = []
    business_final = []
    social_final = []
    novel_final = []
    coherent_final = []
    totals_final = dict() 
    number_of_filters_final = 1
    number_of_iterations = 3 ##Change back to 5

    for x in range (1,2):
        i = 0
        problems[0] = problem
        solutions[0] = solution
        vals = []
        sustainability = []
        business = []
        social = []
        novel = []
        coherent = []
        ##print(problems[i], solutions[i])
        social.append(fil.socialImpact(problems[i], solutions[i], number_of_iterations))
        #print("Social Imapact: ")
        #print(fil.socialImpact(problems[i], solutions[i], number_of_iterations))
        social.append(fil.socialJustice(problems[i], solutions[i], number_of_iterations))
        social.append(fil.socialLearning(problems[i], solutions[i], number_of_iterations))
        social.append(fil.Influence(problems[i], solutions[i], number_of_iterations))
        

        business.append(fil.revenue(problems[i], solutions[i], number_of_iterations))
        business.append(fil.marketSize(problems[i], solutions[i], number_of_iterations))
        business.append(fil.monopoly(problems[i], solutions[i], number_of_iterations))


        coherent.append(fil.realismFilter(problems[i], solutions[i], number_of_iterations))
        coherent.append(fil.realTech(problems[i], solutions[i], number_of_iterations))
        coherent.append(fil.coherenceGeneral(problems[i], solutions[i], number_of_iterations))

        sustainability.append(fil.RelevanceToCircularity(problems[i], solutions[i], number_of_iterations))
        sustainability.append(fil.ResourceEfficiency(problems[i], solutions[i], number_of_iterations))
        

        novel.append(fil.innovativeImpact(problems[i], solutions[i], number_of_iterations))
        novel.append(fil.Opportunity(problems[i], solutions[i], number_of_iterations))
        

        """"
        social.append(fil.socialImpact(problems[i], solutions[i], 5))
        social.append(fil.socialImpact(problems[i], solutions[i], 5))
        social.append(fil.socialImpact(problems[i], solutions[i], 5))
        """
        social_sum = sum(social)
        #print("Sum of Social")
        #print(social_sum)
        business_sum = sum(business)
        coherent_sum = sum(coherent)
        sustainability_sum = sum(sustainability)
        novel_sum = sum(novel)

        social_final.append(social_sum/(4))
        business_final.append(business_sum/(3))
        coherent_final.append(coherent_sum/(3))
        sustainability_final.append(sustainability_sum/(2))
        novel_final.append(novel_sum/(2))

    for i in range(0, len(social_final)):
        vals_final.append(((social_final[i] + business_final[i] + coherent_final[i] + sustainability_final[i] + novel_final[i])/(5*10))*100)

    #print("Social Final\n")
    #print(social_final)
    #print("Business Final\n")
    #print(business_final)

    #print("Coherent Final\n")
    #print(coherent_final)
    #print("Sustainability Final\n")
    #print(sustainability_final)
    #print("novel Final\n")
    #print(novel_final)



        
    #print("Final Values")
    #print(vals_final)

    #print("Vals Final Value: \n")
    #print(vals_final[0])
    #print("\n")

    #print("Social Justification")
    #print(fil.socialJustification(problems[i], solutions[i], social_final[0]))

    #print("Business Justification")
    #print(fil.businessJustification(problems[i], solutions[i], business_final[0]))

    #print("Coherence Justification")
    #print(fil.coherentJustification(problems[i], solutions[i], coherent_final[0]))

    #print("Novel Justification")
    #print(fil.novelJustification(problems[i], solutions[i], novel_final[0]))

    #print("Sustainibility Justification")
    #print(fil.sustainabilityJustification(problems[i], solutions[i], business_final[0]))

    #print("Justification")
    #print(fil.finalJustification(problems[i], solutions[i], vals_final[0]))

    finalArr = [] ## Pass Final Values to Streamlit User Interface

    finalArr.append(vals_final[0])
    finalArr.append(sustainability_final[0])
    finalArr.append(social_final[0])
    finalArr.append(business_final[0])
    finalArr.append(novel_final[0])
    finalArr.append(coherent_final[0])
    finalArr.append(fil.finalJustification(problems[i], solutions[i], retQuality100(vals_final[0])))
    finalArr.append(fil.sustainabilityJustification(problems[i], solutions[i], retQuality10(sustainability_final[0])))
    finalArr.append(fil.socialJustification(problems[i], solutions[i], retQuality10(social_final[0])))
    finalArr.append(fil.businessJustification(problems[i], solutions[i], retQuality10(business_final[0])))
    finalArr.append(fil.novelJustification(problems[i], solutions[i], retQuality10(novel_final[0])))
    finalArr.append(fil.coherentJustification(problems[i], solutions[i], retQuality10(coherent_final[0])))
    
    return finalArr


#id = []
#problems = []
#solutions = []


#for i in range (1, 1302):
#    id.append(i)

##print(id)
##print(id)
##print(problems)
##print(solutions)

"""
row = []
for row in csvreader:
    rows.append(row)
#print(rows)
""" #ideally it would be better if we access the id, problem and solution in the same list (this would output a 2-d list). 

#concept: we evalaute each data point of the list with the filter. Remove it if the filter returns not viable.

#Another Idea: Just identify the problem and solution based on what its index in the list is, e.g. item 1 has index 0, etc...  we can match up these things.