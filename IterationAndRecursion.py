
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    while True:
        try:
            number = int(input("Enter a number to calculate the factorial (or 'q' to quit): "))
            
            iterative_result = factorial_iterative(number)
            recursive_result = factorial_recursive(number)
            
            print(f"Iterative: factorial({number}) = {iterative_result}")
            print(f"Recursive: factorial({number}) = {recursive_result}")
        except ValueError:
            print("Invalid input or 'q' entered. Exiting program.")
            break

if __name__ == "__main__":
    main()
