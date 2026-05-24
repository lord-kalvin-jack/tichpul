from functools import reduce
import operator
#binyamin godfrey 218804581
#elad zwecher
#------------------------------q1------------------------------
#------------------------------q2------------------------------
def reverseList(n):
    if isinstance(n, (int , float)):
        return n
    if isinstance(n, str):
        return n[::-1]
    elif isinstance(n, tuple):
        return tuple(reverseList(list(n)))
    elif isinstance(n, list):
        if not n:
            return []
        return [reverseList(item) for item in n][::-1]
    else:
        return [n]
def q2():
    n = eval(input("Enter a list: "))
    print(reverseList(n))

#------------------------------q3------------------------------
def isPalindrome(n):
     return n == reverseList(n)
def q3():
    n = eval(input("Enter a list: "))
    if isPalindrome(n):
        print("It is a palindrome")

    else: print("It is not a palindrome")
#------------------------------q4------------------------------
#------------------------------q5------------------------------
def main():
    lfuncs = [q2,q3]

    lstrs = ["reverses the list", "is a list a palindrome"]

    while True:
        print("your choices: ")
        for (i, s) in enumerate(lstrs, start=1):
            print(i, " : ", s)

        print("0 : exit")

        c = int(input("please enter your choice: "))

        if c == 0:
            break
        elif c >= 1 and c <= len(lstrs):
            lfuncs[c - 1]()
        else:
            print("error")


if __name__ == "__main__":
    main()