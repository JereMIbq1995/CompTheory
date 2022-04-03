def q(printedString, machineName):
    return f"def {machineName}(): return '{printedString}'"

def A(): return "def B(input): return q(input, 'A') + '\\n' + A()"

def B(input): return q(input, 'A') + '\n' + A()

if __name__ == "__main__":
    print(B(A()))