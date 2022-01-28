class TuringMachine2:
    """
        This is the machine for Exercise 3.8b
        It should recognize all strings that have 2 times as many 0's as 1's
        (NOT including the empty string, even though it's not that hard to make
        it accept the empty string as well)
        It is built based on my state machine diagram number 1 included in
            this repository
    """
    def __init__(self):
        # I'm actually not using this list. Maybe you can find a good use for it?
        self._valid_states = ["qs", "q0", "q1", "q01", "q00", "q10", "q2", "q3", "q_accept", "q_reject"]
        self._state = "qs"   # start state
        self._head = 0       # initial head
    
    def restart_machine(self):
        """
            Restart the state to start state
            Restart the head to the beginning of the tape
        """
        self._state = "qs"
        self._head = 0

    def read_input(self, input: str = ""):
        """
            This function won't make much sense if you don't have the state
            diagram since it is programmed exactly according to the state diagram
        """
        tape = []
        for symbol in input:
            tape.append(symbol)
        tape.append('_') # signifies the end of the input on the tape
        
        halted = False
        while not halted:
            if (self._state == "qs"):
                if tape[self._head] == '0':
                    tape[self._head] = '_'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '1':
                    tape[self._head] = '_'
                    self._head += 1
                    self._state = "q1"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
            
            elif (self._state == "q1"):
                if tape[self._head] == 'X' or tape[self._head] == '1':
                    self._head += 1
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q10"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
            
            elif (self._state == "q10"):
                if tape[self._head] == 'X' or tape[self._head] == '1':
                    self._head += 1
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head -= 1
                    self._state = "q2"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
            
            elif (self._state == "q2"):
                if tape[self._head] == 'X' or tape[self._head] == '1' or tape[self._head] == '0':
                    self._head -= 1
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q3"
            
            elif (self._state == "q3"):
                if tape[self._head] == 'X':
                    self._head += 1
                elif tape[self._head] == '1':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q1"
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_accept"
                    halted = True
            
            elif (self._state == "q0"):
                if tape[self._head] == 'X':
                    self._head += 1
                elif tape[self._head] == '1':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q01"
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q00"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
            
            elif (self._state == "q00"):
                if tape[self._head] == 'X' or tape[self._head] == '0':
                    self._head += 1
                elif tape[self._head] == '1':
                    tape[self._head] = 'X'
                    self._head -= 1
                    self._state = "q2"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
            
            elif (self._state == "q01"):
                if tape[self._head] == 'X' or tape[self._head] == '1':
                    self._head += 1
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head -= 1
                    self._state = "q2"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_reject"
                    halted = True
        
        return self._state