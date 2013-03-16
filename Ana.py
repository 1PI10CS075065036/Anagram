'''
Created on 10-Mar-2013

@author: Dhiren Rachamallu
'''
import enchant

def Language_Selection():
    count =0
    print "The type of English to be used:-\n\t1)For American English type US\n\t2)For British English type GB\n"
    while(1):
        if count>5:
            print "Sorry Timed Out!"
            exit(1)
        else:
            a=raw_input()
            if a=="US":
                b=enchant.Dict("en_US")
                break
            elif a=="GB":
                b=enchant.Dict("en_GB")
                break
            else:
                print"Invalid Input\nTry again"
                count=count+1
    return b

def Get_String(a):
    print "Enter the anagram subject:-\t"
    b=raw_input()
    c=b.lower()
    c=c.split()
    for i in b:
        if a.check(i):
            pass
        else:
            print "The anagram subject\"",b,"\"is NOT a english word.\n"
            exit(2)
    c=''.join(c)
    c=sorted(c)
    return c

def Validation(a,b):
    if a == b:
        print "The given angram is TRUE for the given subject.\n"
    else:
        print "The given anagram is FALSE for the given subject.\n"
        exit(4)

def main():
    a=Language_Selection()
    b=Get_String(a)
    c=Get_String(a)
    Validation(b,c)

main()
