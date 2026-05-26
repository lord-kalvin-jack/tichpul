from functools import reduce
import operator
#Binyamin Godfrey 218804581
#Elad Zwecher 218779668
#------------------------------q1------------------------------
def q1():
    file_name = input("Enter project file name: ")
    #input validation is made in our get_proj_info
    print("Project Times Delta:")
    print(proj_times(file_name))
    
    cost_per_time = float(input("Enter cost per time unit: "))
    print("\nProject Time and Cost (Estimated, Actual, Delta):")
    print(proj_time_cost(file_name, cost_per_time))

def proj_times(file_name):
    lst = get_proj_info(file_name)

    def processProj(nodes):
        if not nodes:
            return []
        
        return [[[node[0][0], node[0][2] - node[0][1]], processProj(node[1])] for node in nodes]
        
    return processProj(lst)

def proj_time_cost(file_name, cost_per_time_unit):
    nodes = get_proj_info(file_name)
    
    estimatedTime = sum([node[0][1] for node in nodes])
    actualTime = sum([node[0][2] for node in nodes])
    timeDelta = actualTime - estimatedTime

    return (
        (estimatedTime, estimatedTime * cost_per_time_unit),
        (actualTime, actualTime * cost_per_time_unit),
        (timeDelta, timeDelta * cost_per_time_unit)
    )

def get_proj_info(file_name):
    try:
        with open(file_name, "r") as flobj:
            lines = flobj.readlines()

    except:
        print("An error occurred. File name may not be valid.")
        return []

    return [line[:-1].split(",") for line in lines]
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
    
    if (not isinstance(list)):
        print("ERROR: Input list is incorrect! ")
        return
    
    print(reverseList(n))

#------------------------------q3------------------------------
def isPalindrome(n):
     return n == reverseList(n)
def q3():
    n = eval(input("Enter a list: "))

    if (not isinstance(list)):
        print("ERROR: Input list is incorrect! ")
        return
    
    if isPalindrome(n):
        print("It is a palindrome")

    else: print("It is not a palindrome")
#------------------------------q4------------------------------
def primes(n):
    compositeNumbers = {j for i in range(2, int(n**0.5) + 1) for j in range(i * 2, n + 1, i)}

    return [i for i in range(2,n + 1) if i not in compositeNumbers]

def twinp(n):
    primeList = primes(n)
    return {prime : prime + 2 for prime in primeList if prime + 2 in primeList}

def q4():
    n = eval(input("Enter a Natural number n: "))

    if (not isinstance(n, int) or n <= 0):
        print("ERROR: Input number is incorrect! ")
        return
    prime_dict = twinp(n)

    [print(f"{key} {value}") for key, value in twinp]
      
#------------------------------q5------------------------------
def add3dicts(d1,d2,d3):
    dicts = (d1, d2, d3)
    all_keys = set().union(*(d.keys() for d in dicts))
    def merge(key):
        values = tuple(d[key] for d in dicts if key in d)
        unique_values = tuple(dict.fromkeys(values))
        return unique_values[0] if len(unique_values) == 1 else unique_values
    return {k: merge(k) for k in all_keys}

def q5():
    d1 = eval(input("Enter a dictionary: "))
    d2 = eval(input("Enter a dictionary: "))
    d3 = eval(input("Enter a dictionary: "))

    #input validation
    if not (isinstance(d1, dict) and isinstance(d2, dict) and isinstance(d3, dict)):
        print("ERROR: Input is incorrect!")
        return
    
    result = add3dicts(d1, d2, d3)
    print("Merged dictionary:")
    print(result)


def main():
    # Array of function references
    lfuncs = [q1, q2, q3, q4, q5]

    # Array of descriptions corresponding to the functions
    lstrs = [
        "Process project times and costs (q1)",
        "Reverse a nested list (q2)",
        "Check if a list is a palindrome (q3)",
        "Find twin primes up to n (q4)",
        "Merge three dictionaries (q5)"
    ]

    while True:
        print("\n--- Main Menu ---")
        for (i, s) in enumerate(lstrs, start=1):
            print(f"{i} : {s}")
        print("0 : exit")

        try:
            c = int(input("Please enter your choice: "))
        except ValueError:
            print("ERROR: Invalid input. Please enter a number.")
            continue

        if c == 0:
            print("Exiting...")
            break
        elif 1 <= c <= len(lstrs):
            lfuncs[c - 1]() # Execute the chosen function
        else:
            print("ERROR: Choice out of range.")

if __name__ == "__main__":
    main()