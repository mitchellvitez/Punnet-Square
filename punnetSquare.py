string = raw_input("Enter your alleles in form \"AaBB x AAbb\": ")
square = [0] * 25
square[0] = string

string2 = string.replace(" ","")
strings = string2.split('x')
string1 = strings[0]
string2 = strings[1]

string11 = string1[0]
string12 = string1[1]
string13 = string1[2]
string14 = string1[3]

string21 = string2[0]
string22 = string2[1]
string23 = string2[2]
string24 = string2[3]

square[1] = string11 + string13
square[2] = string11 + string14
square[3] = string12 + string13
square[4] = string12 + string14

square[5] = string21 + string23
square[10] = string21 + string24
square[15] = string22 + string23
square[20] = string22 + string24

square[6] = square[1] + square[5]
square[7] = square[2] + square[5]
square[8] = square[3] + square[5]
square[9] = square[4] + square[5]

square[11] = square[1] + square[10]
square[12] = square[2] + square[10]
square[13] = square[3] + square[10]
square[14] = square[4] + square[10]

square[16] = square[1] + square[15]
square[17] = square[2] + square[15]
square[18] = square[3] + square[15]
square[19] = square[4] + square[15]

square[21] = square[1] + square[20]
square[22] = square[2] + square[20]
square[23] = square[3] + square[20]
square[24] = square[4] + square[20]

squareBegin = square[0]
square[0] = " " 
line1 = square[0] +"\t"+ square[1] +"\t"+ square[2] +"\t"+ square[3] +"\t"+ square[4]
line2 = square[5] +"\t"+ square[6] +"\t"+ square[7] +"\t"+ square[8] +"\t"+ square[9]
line3 = square[10] +"\t"+ square[11] +"\t"+ square[12] +"\t"+ square[13] +"\t"+ square[14]
line4 = square[15] +"\t"+ square[16] +"\t"+ square[17] +"\t"+ square[18] +"\t"+ square[19]
line5 = square[20] +"\t"+ square[21] +"\t"+ square[22] +"\t"+ square[23] +"\t"+ square[24]

print "\t    " + squareBegin
print line1
print line2
print line3
print line4
print line5
