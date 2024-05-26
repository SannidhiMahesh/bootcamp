class PalindromeChecker:
    def __init__(self):
        self.value = ""

    def get_input(self):
        # Taking input from the user
        self.value = input("Enter a number or a string to check if it is a palindrome: ")
        
    def is_palindrome(self):
        # Check if the value reads the same forwards and backwards
        return self.value == self.value[::-1]
    
    def display_result(self):
        # Display the result based on the palindrome check
        if self.is_palindrome():
            print(f"'{self.value}' is a palindrome.")
        else:
            print(f"'{self.value}' is not a palindrome.")

# Example usage
if __name__ == "__main__":
    checker = PalindromeChecker()
    checker.get_input()
    checker.display_result()
