'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import math 
def count_th(word):
    count = max(len(word.split("th"))-1, 0);
    if(count > 0):
        count += count_th(""); #see it utilize recurtion;
    return count;
    
