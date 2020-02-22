#!/usr/bin/env python

""" 
Calculate successful hits with dices 

PROBABILITY: Initially the probability of an event to occur was defined as 
the number of cases favorable for the event, 
over the number of total outcomes possible 
in an equiprobable sample space
"""

"""
    1. What is the probability to occur number 1 
    if we roll 1 dice?
"""
event = (1) # the succesful number of the dice
sample_space = (1,2,3,4,5,6) # the numbers of the dice sides
dices = 1  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

for i in sample_space:
    possible_outcomes_list.append(i)

# print(possible_outcomes_list)
    
occurences =  possible_outcomes_list.count(1)       # favorable cases
possible_outcomes_total = len(possible_outcomes_list)

# %.0f stands for "print a float with 0 decimal places", so %.2f would print 33.33
probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the number {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences, possible_outcomes_total, probability))
######################################################################################################
"""
    1. What is the probability to occur number 1 or 2
    if we roll 1 dice?
"""
event = (1,2)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 1  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

for i in sample_space:
    possible_outcomes_list.append(i)

# print(possible_outcomes_list)


def countOccurance(possibleOutcomeList, eventList):
    count = 0
    for item in possibleOutcomeList:
        if item in eventList:
            count += 1
    return count

occurences = countOccurance(possible_outcomes_list, event)       # favorable cases

possible_outcomes_total = len(possible_outcomes_list)

# %.0f stands for "print a float with 0 decimal places", so %.2f would print 33.33
probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences, possible_outcomes_total, probability))


######################################################################################################
"""
    What are the probabilities to occur number 1
    if we roll 2 dices?
"""
print("QUESTION: What are the probabilities to occur number 1, if we roll 2 dices?")

# Empty tuples are constructed by an empty pair of parentheses
# a tuple with one item is constructed by following a value with a comma
# (it is not sufficient to enclose a single value in parentheses)
event = (1,)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 2  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

# create all possibles combinations
# the depth loop depends on the number of dices
# 2 dices = 2 for loops
# for d1 in sample_space:
#     for d2 in sample_space:
#         possible_outcomes_list.append([d1, d2])
# the above code as comprehensive list:

possible_outcomes_list = [(d1,d2) for d1 in sample_space for d2 in sample_space ]
# print(possible_outcomes_list)

# TODO: https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# occurences = possible_outcomes_list.count([1,1])       # favorable cases
succesful_pairs = []
# iterate through possible_outcomes_list and select the items (pair)  
# if they contain numbers that match any number contained in the event tuple
# print("SUCCESSFUL PAIRS:")
# https://www.youtube.com/watch?v=AhSvKGTh28Q
succesful_pairs = [pair for pair in possible_outcomes_list if any(event) in pair]
# print(succesful_pairs)



occurences = len(succesful_pairs)
possible_outcomes_total = (len(sample_space))**dices # or len(possible_outcomes_list) 

# %.0f stands for "print a float with 0 decimal places", so %.2f would print 33.33
probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences, possible_outcomes_total, probability))


######################################################################################################
"""
    What are the probabilities to occur number 1
    if we roll 3 dices?
"""
print("QUESTION: What are the probabilities to occur number 1, if we roll 3 dices?")

event = (1,)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 3  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

# create all possibles combinations
# the depth loop depends on the number of dices
# 3 dices = 3  loops
possible_outcomes_list = [(d1, d2, d3)
                          for d1 in sample_space 
                          for d2 in sample_space
                          for d3 in sample_space]

# print(possible_outcomes_list)

# TODO: https://snakify.org/en/lessons/two_dimensional_lists_arrays/
# occurences = possible_outcomes_list.count([1,1])       # favorable cases
succesful_pairs = []
# iterate through possible_outcomes_list and select the items (pair)
# if they contain numbers that match any number contained in the event tuple
# print("SUCCESSFUL PAIRS:")
# https://www.youtube.com/watch?v=AhSvKGTh28Q
succesful_pairs = [
    pair for pair in possible_outcomes_list if any(event) in pair]
# print(succesful_pairs)


occurences = len(succesful_pairs)
# or len(possible_outcomes_list)
possible_outcomes_total = (len(sample_space))**dices

# %.0f stands for "print a float with 0 decimal places", so %.2f would print 33.33
probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences, possible_outcomes_total, probability))

######################################################################################################
"""
    What are the probabilities to occur number 1
    if we roll 4 dices?
"""
print("QUESTION: What are the probabilities to occur number 1, if we roll 4 dices?")

event = (1,)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 4  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

possible_outcomes_list = [(d1, d2, d3, d4)
                          for d1 in sample_space
                          for d2 in sample_space
                          for d3 in sample_space
                          for d4 in sample_space]

# print(possible_outcomes_list)

succesful_pairs = []
succesful_pairs = [
    pair for pair in possible_outcomes_list if any(event) in pair]
# print("SUCCESSFUL PAIRS:")
# print(succesful_pairs)


occurences = len(succesful_pairs)
possible_outcomes_total = (len(sample_space))**dices

probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences,
                    possible_outcomes_total, probability))


######################################################################################################
"""
    What are the probabilities to occur number 1
    if we roll 5 dices?
"""
print("QUESTION: What are the probabilities to occur number 1, if we roll 5 dices?")

event = (1,)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 5  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

possible_outcomes_list = [(d1, d2, d3, d4, d5)
                          for d1 in sample_space
                          for d2 in sample_space
                          for d3 in sample_space
                          for d4 in sample_space
                          for d5 in sample_space]

# print(possible_outcomes_list)

succesful_pairs = []
succesful_pairs = [
    pair for pair in possible_outcomes_list if any(event) in pair]
# print("SUCCESSFUL PAIRS:")
# print(succesful_pairs)


occurences = len(succesful_pairs)
possible_outcomes_total = (len(sample_space))**dices

probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences,
                    possible_outcomes_total, probability))

######################################################################################################
"""
    What are the probabilities to occur number 1
    if we roll 6 dices?
"""
print("QUESTION: What are the probabilities to occur number 1, if we roll 6 dices?")

event = (1,)  # the succesful numbers of the dice
sample_space = (1, 2, 3, 4, 5, 6)  # the numbers of the dice sides
dices = 6  # how many times do we roll the dice, or how many dices do we use

possible_outcomes_list = []

possible_outcomes_list = [(d1, d2, d3, d4, d5, d6)
                          for d1 in sample_space
                          for d2 in sample_space
                          for d3 in sample_space
                          for d4 in sample_space
                          for d5 in sample_space
                          for d6 in sample_space]

# print(possible_outcomes_list)

succesful_pairs = []
succesful_pairs = [
    pair for pair in possible_outcomes_list if any(event) in pair]
# print("SUCCESSFUL PAIRS:")
# print(succesful_pairs)


occurences = len(succesful_pairs)
possible_outcomes_total = (len(sample_space))**dices

probability = "{0:.2%}".format(occurences/possible_outcomes_total)

print(probability)
result = "If we roll the dice {} times, the numbers {} appears {} times out of {} possible sequences, so probability is {} \n"
print(result.format(dices, event, occurences,
                    possible_outcomes_total, probability))
