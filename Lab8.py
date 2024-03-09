#Matthew Stephenson
#Lab8
#3/9/2024
#this program computes the GC content of a DNA molecule. 

str_param = input("Dear Genome Sequencer, inject a string representing where each character is one of G, C, T or A, the GC ratio is computed as the count of G+C values over the total count of A, T, C, G values\n")
#at the line above you prompt the user for an input, and store that at the stack
def computeGCRatio(str_param):
#above you take in str_param as your parameter, which is what is currently at the stack and pass it into the func
    str_arr = list(str_param)  # Fix the typo here, change 'str_arr = str_param' to 'str_arr = list(str_param)'
    count1 = str_arr.count('A') #using the count method.
    count2 = str_arr.count('T') #using the method again for 'T' at the stack location at str_param
    count3 = str_arr.count('C') #using method again for 'C' at entire sequence
    count4 = str_arr.count('G') #doing same thing as line above.
    return (count3 + count4) / (count1 + count2 + count3 + count4)  # Corrected the formula

gcratio = computeGCRatio(str_param)  # Call the function and store the result in 'gcratio'
#function has to be called, to actually get the little 'function machine' to start working.
print("For the sequence:", str_param)  # Print the original DNA sequence
print("The GC-Ratio is {:6.3f}".format(gcratio))  # Print the calculated GC ratio



#ps: If you invoke a func, in python it seems like you also need to use it's affiliated param
#I could not connect to Zoom earlier for the lab
#I sent peter an email regarding this. I think it was related to me connection
#this issue has since been fixed
