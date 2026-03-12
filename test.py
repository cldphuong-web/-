# Program to calculate the sum from 1 to N

def mis2a():
    # Function to input N
    N = int(input("Enter a number N: "))
    return N

def mis2b(N):
    # Function to calculate the sum from 1 to N
    total = sum(range(1, N + 1))
    print(f"The sum from 1 to {N} is: {total}")

def main():
    N = mis2a()   # input N
    mis2b(N)      # calculate and print result

if __name__ == "__main__":
    main()
