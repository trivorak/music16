# # inital hash to test with
# inithash = "40bd9ca32449a286618b2d7bc0e181cc50699c32"

# # hexhead is unused currently
# hexhead = "0x"           #Hex "header" for binary/hex/init conversions

# # strip string of characters for drum programming
# print(inithash[:4])      #Print first 4 characters of inithash var
# print(inithash[4:8])     #Print 2nd set of 4
# print(inithash[8:12])    #Print 3rd set of 4

# # add hex to front of 4 characters 

# print(hexhead + inithash[:4])
# print(hexhead + inithash[4:8])
# print(hexhead + inithash[8:12])

# # binary conversions
# print(bin(int(hexhead + inithash[:4], 16)))
# print(bin(int(hexhead + inithash[4:8], 16)))
# print(bin(int(hexhead + inithash[8:12], 16)))

# # chop off header of binary and store as an array 
# print((bin(int(hexhead + inithash[:4], 16)))[2:])         # chop "0b" 
# bdbinary = ((bin(int(hexhead + inithash[:4], 16)))[2:])   # store chopped val in var 
# bdbinary = bdbinary.zfill(16)                             # fill to 16 'slots'
# print(bdbinary)                                           # check output is correct
# print(len(bdbinary))                                      # check length is correct
# bdlist = list(bdbinary)                                   # convert to list/array
# print(bdlist)                                             # list/array check
# bdlist.reverse()                                          # reverse list so steps read from left to right
# print(bdlist)                                             # check reverse
# print(len(bdlist))

# # for loop test to step thru list
# print()
# print("BD PATTERN")
# print()

# for x in range(0, len(bdlist)):
#   print(bdlist[x])

var = "f3"

var2 = bin(int(var,16))

print(var2)