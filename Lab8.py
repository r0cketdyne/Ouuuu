
###Part IIa: Writing your own functions
###We will complete this program that requires the definition of a function named computeGCRatio to
###compute the GC content of a DNA molecule.
###Given a single string as input where each character is one of G, C, T or A, the GC ratio is computed as the
###count of G+C values over the total count of A,T,C,G values. It is often written in texts as the following,
###where each letter represents the count of instances in the string

# Lab 8
# PUT YOUR DEFINITION OF THE FUNCTION computeGCRatio HERE!
# Hint: your function will need 4 counter variables ( one for each
# letter. And you will need to write a loop that steps through each
# character in the string

#shit python is dynamically typed I don't need this
str_param = input("Dear Genome Sequencer, inject a string representing where each character is one of G, C, T or A, the GC ratio is computed as thecount of G+C values over the total count of A,T,C,G values\n")

def computeGCRatio(str_param): # what is/are the parameters needed here?
    str_arr = str_param #fuck, I forgot to att str to str_param. typos ffs
#I think arrays are dynamically allocated at Python, else I would have allocated space for it below str_param
#    print(rando_stackalloc)
    count1 = str_arr.count('A') #ok there's a literal count method
    
    count2 = str_arr.count('T') #use count method
    
    count3 = str_arr.count('C') #just use the count method 
    
    count4 = str_arr.count('G') #just going to use the count method
    
    rando_stackalloc = (count1 + count2 + count3 + count4)
    print(rando_stackalloc)




computeGCRatio(str_param)
#If you invoke a func, in python it seems like you also need to use it's affiliated param
#not sure why. will research
#chatbots are dumb. It couldn't even tell me
#that I just needed to invoke this function. which I did at line 23. it was functional



#in music, studio time is essential. faculty and student complaints, strikes. 
#all people to at Concordia is protest. Have they tried 
#putting in actual work lol. This isn't McGill. At least the campus is nice

#FUGAZZI

#gc_ratio = (count3 + count4) / (count1 + count2 + count3 + count4)  # Compute GC ratio
#    print("GC Ratio:", gc_ratio)
#two lines above are the ratio I need, but not implementing this yet. this
#program is waaaay easier than I anticipated that it would be


#import math
#x = 3.1;
#y = 1.0 - x;

#print("This evalues to ", math.fabs(y))
#1 evaluated to 2.1 returns the absolute val of a num, as a float

#print("This evalues to ", math.floor(x))
#2 evaluates to 3. this particular method rounds a number DOWN to the nearest integer.
#print("This evalues to ", math.ceil(x))
#this evaluates to 4. rounds up to nearest int
#print("This evaluates to", math.floor(y))
#this evaluates to -3 this, obviously then must round down to nearest int
#print("This evalues to", math.ceil(y))
#this evaluates to -2, and again, here it must again round up

#biggest thing here. help(math) is a GREAT in console problem solving toolkit. 
