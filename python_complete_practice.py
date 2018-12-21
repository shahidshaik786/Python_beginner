#/bin/python

#Printing output in python 3.x
print("Hellow world.! This is Shahid_Shaik")

#Variables in python
""" No need to difene tha variable type.
    Python takes numerics as intgers and characters as string.
    Variables cannot start with numbers and special characters
    Python is case sensitive
"""
a=34
b="shahid"
C=0.23

print("Type of 'a' variable is " + str(type(a)))
print("Type of 'b' variable is " + str(type(b)))
print("Type of 'c' variable is " + str(type(C)))

#Operators in python
""" 1)Arthimetic Operators
        + addition
		- subtraction
		* mulitplication
		% modulas
		** exponent
        // Floor Division
"""
a=2
b=9
d=2.0
e=9.0
#-------- Addition------------#
c=a+b
print("Addition " + str(c))
#-------- Subtraction------------#
c=a-b
print("Subtraction " + str(c))
#-------- Mulitplication------------#
c=a*b
print("Mulitplication " + str(c))
#-------- Divsion------------#
c=b/a
print("Divsion "+ str(c))
#-------- Modulus------------#
c=b%a
print("Modulus "+ str(c))
#-------- Exponent------------#
c=b**a
print("Exponent "+ str(c))
#-------- Floor division without floot values------------#
c=b//a
print("Floor division without floot values" + str(c))
#-------- Floor division with floot values------------#
c=e//d
print("Floor division with floot values " + str(c))

""" 2)Logical Operators
        == comparision
        != not equals to
        <= less than or equals
        >= greater than or equals
        > is greater than
        < is less than

Note: For if else conditions syntax are mandatory
        if <Statement>:
            <tap space>
        else:
            <tab space>
"""
#-------- comparision------------#
if a == b:
    print("both A="+ str(a)+ " and B="+ str(b) +" values are same ")
else:
    print("both A="+ str(a)+ " and B="+ str(b) +" values are NOT same ")
#-------- Not equals------------#
if a != b:
    print("both A="+ str(a)+ " and B="+ str(b) +" values are NOT same ")
else:
    print("both A="+ str(a)+ " and B="+ str(b) +" values are same ")
#-------- less than or equals------------#
a=3
b=4
if a <= b:
    print("A less than or equals B "+"A="+str(a)+" and B="+str(b))
else:
    print("A greate than or not equals B "+"A="+str(a)+" and B="+str(b))
#-------- greater than or equals------------#
a=7
b=4
if a >= b:
    print("A greater than or equals B "+"A="+str(a)+" and B="+str(b))
else:
    print("A less than or not equals B "+"A="+str(a)+" and B="+str(b))
#-------- greater than------------#
if a > b:
    print("A greater than B "+"A="+str(a)+" and B="+str(b))
else:
    print("A not greater than B "+"A="+str(a)+" and B="+str(b))
#-------- less than------------#
if a < b:
    print("A less than B "+"A="+str(a)+" and B="+str(b))
else:
    print("A not less than B "+"A="+str(a)+" and B="+str(b))
""" 3)Assignment Operators
        =
        +=
        -=
        *=
        /=
        %=
        **=
        //=
"""
#-------- = ------------#
a=10
b=23
c=a
print("A="+str(a)+" B="+str(b)+" C="+str(c))
#-------- += ------------#
a=10
b=23
b+=a #b=b+a
print("b+=a = "+str(b))
#-------- += ------------#
a=10
b=23
b-=a #b=b-a
print("b-=a = "+str(b))
#-------- *= ------------#
a=2
b=4
b*=a #b=b-a
print("b*=a = "+str(b))
#-------- /= ------------#
a=2
b=9
b/=a #b=b/a
print("b/=a = "+str(b))
#-------- %= ------------#
a=2
b=4
b%=a #b=b%a
print("b%=a = "+str(b))
#-------- **= ------------#
a=2
b=4
b**=a #b=b**a
print("b**=a = "+str(b))
#-------- //= ------------#
a=2.0
b=9.0
b//=a #b=b//a
print("b//=a = "+str(b))
"""4)Logical Operators
        and
        or
        not
"""
"""Truth Table for AND Operator
---------------------------
|   a    |   b    |a and b|
---------------------------
|   T    |   T    |   T   |
---------------------------
|   T    |   F    |   F   |
---------------------------
|   F    |   T    |   F   |
---------------------------
|   F    |   F    |   F   |
---------------------------"""
#-------- and ------------#
def TandT():
    return """Selected arugemnet = 1 :
    T and T ; returns True"""
def TandF():
    return """Selected arugemnet = 2 :
    T and F ; returns False"""
def FandT():
    return """Selected arugemnet = 3 :
    F and T ; returns True"""
def FandF():
    return """Selected arugemnet = 4 :
    F and F ; returns False"""
def and_operator(argument):
    switcher = {
        1: TandT(),
        2: TandF(),
        3: FandT(),
        4: FandF(),
    }
    return switcher.get(argument, "Please enter value from 1 to 4 only")
if __name__ == "__main__":
    argument=1 ###
    print(and_operator(argument))
"""Truth Table for OR Operator
---------------------------
|   a    |   b    |a OR b|
---------------------------
|   T    |   T    |   T   |
---------------------------
|   T    |   F    |   T   |
---------------------------
|   F    |   T    |   T   |
---------------------------
|   F    |   F    |   F   |
---------------------------"""
#-------- OR ------------#
def TandT():
    return """Selected arugemnet = 1 :
    T and T ; returns True"""
def TandF():
    return """Selected arugemnet = 2 :
    T and F ; returns True """
def FandT():
    return """Selected arugemnet = 3 :
    F and T ; returns True"""
def FandF():
    return """Selected arugemnet = 4 :
    F and F ; returns False"""
def and_operator(argument):
    switcher = {
        1: TandT(),
        2: TandF(),
        3: FandT(),
        4: FandF(),
    }
    return switcher.get(argument, "Please enter value from 1 to 4 only")
if __name__ == "__main__":
    argument=1 ###
    print(and_operator(argument))
"""Truth Table for NOT Operator
-------------------
|   a    |   ~a   |
-------------------
|   T    |   F    |
-------------------
|   F    |   T    |
-------------------"""
#-------- NOT ------------#
def T():
    return """Selected arugemnet = 1 :
    T ; returns False"""
def F():
    return """Selected arugemnet = 2 :
    F ; returns True """
def and_operator(argument):
    switcher = {
        1: T(),
        2: F(),
    }
    return switcher.get(argument, "Please enter value from 1 or 2 only")
if __name__ == "__main__":
    argument=1 ###
    print(and_operator(argument))
"""5)Bitwise Operators
        & Binary AND
        | Binary OR
        ^ Binary XOR
        ~ Binary Once Complement
        << Binary Left shift
        >> Binary Right shift
"""
""" Binary position as follows
    128 64 32 16  8  4  2  1
    x8  x7 x6 x5 x4 x3 x2 x1
    ------------------------
    Let a = 60 and b = 13
a = 0   0  1   1  1  1  0  0 = 60
b = 0   0  0   0  1  1  0  1 = 13
"""

a = 60
b = 13
c = a & b
print("C value after binary & operation is =",c)
c = a | b
print("C value after binary | operation is =",c)
c = a ^ b
print("C value after binary ^ operation is =",c)
c = ~a
print("C value after binary ~ operation is =",c)
c = a << b
print("C value after binary << operation is =",c)
c = a >> b
print("C value after binary >> operation is =",c)
