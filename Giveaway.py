#! /usr/bin/python3
# THE ENCHANTED SCROLL
# Script opens a file containing list of email addresses used to
# Enter a giveaway.  List 'entries' is created, and then
# A random email is chosen for first and second place prizes.
# The total number of entries is also printed after
# Determining the length of the list.

import random

# Opens the txt file containing the entries.
# Creates list 'entries' of each email address, and returns.
def create_list_of_entries(filename):
    with open(filename) as file_object:
        entries = file_object.readlines()
    return(entries)

# Determines # of entries from the length of the 'entries' list,
# Then prints the value. 
def entry_counter(entries):
    total_entries = len(entries)
    print("The Enchanted Scroll reveals...\n")
    print(f"There are {total_entries} total entries in this giveaway\n")
    
#Makes random choice from list of entries,
# For first and second place, and prints the result. If second
# Place is the same as first, makes a new selection,
# Ensuring one person doesn't win both.
def choose_winners(entries):   
    first = random.choice(entries)
    print(f"The winner of {firstprize} is {first}")
    second = random.choice(entries)
    if second == first:
        second = random.choice(entries)
    print(f"The winner of {secondprize} is {second}")
    print("Congratulations to our winners!")




filename = 'entries.txt'
firstprize = "The Ice Blade"
secondprize = "A Crown of their choice"
entries = create_list_of_entries(filename)
entry_counter(entries)
choose_winners(entries)
