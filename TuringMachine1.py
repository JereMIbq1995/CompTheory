class TuringMachine1:
    """
        This is the machine for Exercise 3.8a
        It should recognize all strings that have the same number 1's as 0's
        (Including the empty string)
        It is built based on my state machine diagram number 1 included in
            this repository
    """
    def __init__(self):
        self._valid_states = ["qs", "q0", "q1", "q2", "q3", "q_accept", "q_reject"]
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

        # Keep running until the machine is halted.
        while not halted:
            # Each iteration represents a configuration of the machine:
            # At each configuration, check the state, the input the head
            # is pointing at, then do the appropriate actions

            # Start state
            if (self._state == "qs"):
                if tape[self._head] == '0':
                    tape[self._head] = '_'
                    self._head += 1
                    self._state = "q1"
                elif tape[self._head] == '1':
                    tape[self._head] = '_'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_accept"
                    halted = True
            
            # Looking for a 1
            elif (self._state == "q1"):
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
            
            # Looking for a 0
            elif (self._state == "q0"):
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
            
            # Looking for the initial number backward (either a 1 or a 0)
            elif (self._state == "q2"):
                if tape[self._head] == 'X':
                    self._head -= 1
                elif tape[self._head] == '1':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q1"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q3"
            
            # Looking for the initial number forward (either 1 or 0)
            elif (self._state == "q3"):
                if tape[self._head] == 'X':
                    self._head += 1
                elif tape[self._head] == '1':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '0':
                    tape[self._head] = 'X'
                    self._head += 1
                    self._state = "q1"
                # Accept if can't find an initial number
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_accept"
                    halted = True
        
        return self._state