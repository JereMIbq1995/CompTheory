class TuringMachine1:
    def __init__(self):
        self._valid_states = ["qs", "q0", "q1", "q2", "q3", "q_accept", "q_reject"]
        self._state = "qs"   # start state
        self._head = 0       # initial head
    
    def restart_machine(self):
        self._state = "qs"
        self._head = 0

    def read_input(self, input: str = ""):
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
                    self._state = "q1"
                elif tape[self._head] == '1':
                    tape[self._head] = '_'
                    self._head += 1
                    self._state = "q0"
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_accept"
                    halted = True
            
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
                elif tape[self._head] == '_':
                    self._head += 1
                    self._state = "q_accept"
                    halted = True
        
        return self._state