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
print("Type of 'a' variable is " + str(type(b)))
print("Type of 'a' variable is " + str(type(C)))

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
print(c)
#-------- Subtraction------------#
c=a-b
print(c)
#-------- Mulitplication------------#
c=a*b
print(c)
#-------- Divsion------------#
c=b/a
print(c)
#-------- Modulus------------#
c=b%a
print(c)
#-------- Exponent------------#
c=b**a
print(c)
#-------- Floor division without floot values------------#
c=b//a
print(c)
#-------- Floor division with floot values------------#
c=e//d
print(c)

""" 2)Logical Operators
        == comparision
        != not equals to
        <= less than or equals
        >= greater than or equals
        > is greater than
        < is less than

Note: For if else conditions syntax are mandatory
        if ():
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
        -+
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
"""Truth Table
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
"""a="cat"
b="cat"
c="dog"
d="mouse"
if 1==1 and 2==2:
    print("T and T ; both are True")
elif 1==1 and 1==2:
    print("T and F ; True and False")
elif 1==2 and 1==1:
    print("F and T ; False and True")
else:
    print("F and F ; both are False")"""

def TandT():
    return """Selected arugemnet = 1 :
    T and T ; both are True"""
def TandF():
    return """Selected arugemnet = 1 :
    T and F ; True and False"""
def FandT():
    return """Selected arugemnet = 1 :
    F and T ; False and True"""
def FandF():
    return """Selected arugemnet = 1 :
    F and F ; both are False"""
def and_operator(argument):
    switcher = {
        1: TandT(),
        2: TandF(),
        3: FandT(),
        4: FandF(),
    }
    return switcher.get(argument, "Please enter value from 1 to 4 only")
if __name__ == "__main__":
    argument=5 ###
    print(and_operator(argument))
