
import random
from TuringMachine1 import TuringMachine1

def num0_equals_num1(input : str):
    """
        A simple algorithm to count number of 1's and 0's
        Return q_accept if number of 1's = number of 0's
        Return q_reject otherwise
    """
    num0 = 0
    num1 = 0
    for c in input:
        if c == '0':
            num0 += 1
        elif c == '1':
            num1 += 1
    
    return "q_accept" if (num0 == num1) else "q_reject"

def generate_string(min_length, max_length):
    """
        Generates a string of 0's and 1's with the given
        min and max lengths
    """
    generated_string = ""
    string_length = random.randint(min_length, max_length)
    for i in range(0, string_length):
        generated_string += str(random.randint(0,1))
    
    return generated_string

def main():

    turing_machine = TuringMachine1()
    # print(turing_machine.read_input("11010000011110010010000011"))

    # Store all the strings that failed the test here
    failed_cases = []

    # Generate and run 1 million test cases
    for i in range(0, 1000000):
        
        generated_string = generate_string(0, 10)
        
        tm_result = turing_machine.read_input(generated_string)
        normal_result = num0_equals_num1(generated_string)
        
        result = "SUCCESS!" if (tm_result == normal_result) else "FAILED!"
        print(result + "  :  " + tm_result + "  :  " + normal_result + "  :  " + generated_string)
        
        if result == "FAILED!":
            failed_cases.append(generated_string)
        turing_machine.restart_machine() # reset the state and the head back to initial values

    print("______________________________________________________")
    print("Number of failed cases: " + str(len(failed_cases)))
    if len(failed_cases) > 0:
        print("Failed cases:")
        for failed_case in failed_cases:
            print(failed_case)

if __name__ == "__main__":
    main()