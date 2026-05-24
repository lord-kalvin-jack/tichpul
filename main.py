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
def example_function_1():
    print("\n--- Running Function 1: Hello World! ---\n")


def example_function_2():
    print("\n--- Running Function 2: Math is fun! (2 + 2 = 4) ---\n")


def main():
    lfuncs = []
    lstrs = []

    while True:
        print("\nYour choices:")
        print("0  :  Exit the program")  # Added clear instruction for the exit condition

        for (i, s) in enumerate(lstrs):
            print(f"{i + 1}  :  {s}")  # Adjusted to show 1-based indexing for the user

        try:
            c = int(input("\nPlease enter your choice: "))

            if c == 0:
                print("Exiting program. Goodbye!")
                break
            elif 1 <= c <= len(lstrs):
                lfuncs[c - 1]()  # Executes the chosen function
            else:
                print("Error: Invalid choice. Please try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")


if __name__ == "__main__":
    main()