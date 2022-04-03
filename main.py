
import random
from TuringMachine1 import TuringMachine1
from TuringMachine2 import TuringMachine2

def num0_equals_num1(input : str):
    """
        A simple algorithm to count number of 1's and 0's
        Return q_accept if number of 1's = number of 0's
        Return q_reject otherwise
        This is to be compared with Machine1's result
    """
    num0 = 0
    num1 = 0
    for c in input:
        if c == '0':
            num0 += 1
        elif c == '1':
            num1 += 1
    
    return "q_accept" if (num0 == num1) else "q_reject"

def num0_equals_2num1(input : str):
    """
        A simple algorithm to count number of 1's and 0's
        Return q_accept if 2 times number of 1's = number of 0's
        Return q_reject otherwise
        This is to be compared with Machine2's result
    """
    if (len(input) == 0):
        return "q_reject"
    num0 = 0
    num1 = 0
    for c in input:
        if c == '0':
            num0 += 1
        elif c == '1':
            num1 += 1
    
    return "q_accept" if (num0 == 2*num1) else "q_reject"

def generate_string(min_length, max_length):
    """
        Generates a random string of 0's and 1's with the given
        min and max lengths
    """
    generated_string = ""
    string_length = random.randint(min_length, max_length)
    for i in range(0, string_length):
        generated_string += str(random.randint(0,1))
    
    return generated_string

def test_turing_machine1(num_test_cases : int = 10, string_min : int = 10, string_max : int = 100):
    """
        Generate <num_test_cases> strings of 0's and 1's
        with <string_min> characters minimum and <string_max> characters maximum

        Run each string through the normal algorithm and compare the result to
        the result of the same string on TuringMachine1.

        Print out the result of each test: beginning with SUCCESS if the 2 results matches,
        beginning with FAILED! if the 2 results don't match
    """
    turing_machine = TuringMachine1()
    # print(turing_machine.read_input("11010000011110010010000011"))

    # Store all the strings that failed the test here
    failed_cases = []

    # Generate and run 1 million test cases
    for i in range(0, num_test_cases):
        
        generated_string = generate_string(string_min, string_max)
        
        tm_result = turing_machine.read_input(generated_string)
        normal_result = num0_equals_num1(generated_string)
        
        result = "SUCCESS!" if (tm_result == normal_result) else "FAILED!"
        # print(result + "  :  " + tm_result + "  :  " + normal_result + "  :  " + generated_string)
        
        if result == "FAILED!":
            failed_cases.append(generated_string)
        turing_machine.restart_machine() # reset the state and the head back to initial values

    print("______________________________________________________")
    print("Number of failed cases: " + str(len(failed_cases)))
    if len(failed_cases) > 0:
        print("Failed cases:")
        for failed_case in failed_cases:
            print(failed_case)

def test_turing_machine2(num_test_cases : int = 10, string_min : int = 10, string_max : int = 100):
    """
        Generate <num_test_cases> strings of 0's and 1's
        with <string_min> characters minimum and <string_max> characters maximum

        Run each string through the normal algorithm and compare the result to
        the result of the same string on TuringMachine2.

        Print out the result of each test: beginning with SUCCESS if the 2 results matches,
        beginning with FAILED! if the 2 results don't match
    """
    turing_machine = TuringMachine2()
    # Store all the strings that failed the test here
    failed_cases = []

    # Generate and run 1 million test cases
    for i in range(0, num_test_cases):
        
        generated_string = generate_string(string_min, string_max)
        
        tm_result = turing_machine.read_input(generated_string)
        normal_result = num0_equals_2num1(generated_string)
        
        result = "SUCCESS!" if (tm_result == normal_result) else "FAILED!"
        # print(result + "  :  " + tm_result + "  :  " + normal_result + "  :  " + generated_string)
        
        if result == "FAILED!":
            failed_cases.append(generated_string)
        turing_machine.restart_machine() # reset the state and the head back to initial values

    print("______________________________________________________")
    print("Number of failed cases: " + str(len(failed_cases)))
    if len(failed_cases) > 0:
        print("Failed cases:")
        for failed_case in failed_cases:
            print(failed_case)

def main():
    """
        Simply run the tests
        You can change the number of test cases to 1 million if you'd like,
            but that would take a while to run
    """
    test_turing_machine1(num_test_cases = 100000, string_min = 10, string_max = 30)
    test_turing_machine2(num_test_cases = 100000, string_min = 20, string_max = 100)

if __name__ == "__main__":
    main()