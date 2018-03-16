#this code is for python for everybody (python data structures) assignment 6.5
###############################################################
#Write code using find() and string slicing (see section 6.10) to
#extract the number at the end of the line below. Convert the
#extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
finds = text.find('0')
var = text[finds:finds+6]
vali = float(var)
print(vali)
