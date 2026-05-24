from functools import reduce
import operator
#binyamin godfrey 218804581
#elad zwecher
#------------------------------q1------------------------------
#------------------------------q2------------------------------
#------------------------------q3------------------------------
def flatten(data):
    # Base Case 1: If it's a string, break it into a list of individual characters
    if isinstance(data, str):
        return list(data)

    # Base Case 2: If it's a single number, wrap it in a list so it can be combined later
    if not isinstance(data, list):
        return [data]

    # Recursive Case: If it's a list, map 'deep_flatten' over every item,
    # then use 'reduce' and 'operator.add' to merge all the resulting lists together.
    return reduce(operator.add, map(flatten, data), [])


# Output: [1, 2, '3', '4', 5, 6, '7', 8]
def isPalindrome(n):
    return n == n[::-1]
def q3():
    n = eval(input("Enter a list: "))
    flattend = flatten(n)
    if isPalindrome(flattend):
        print("It is a palindrome")
    else: print("It is not a palindrome")
#------------------------------q4------------------------------
#------------------------------q5------------------------------
def main():
    lfuncs = [q3]

    lstrs = ["is a list a palindrome"]

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