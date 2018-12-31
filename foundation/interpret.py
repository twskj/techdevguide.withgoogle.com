# Write a simple interpreter which understands "+", "-", and "*" operations. 
# Apply the operations in order using command/arg pairs starting with the initial value of `value`. 
# If you encounter an unknown command, return -1. 

# interpret(1, ["+"], [1]) → 2 
# interpret(4, ["-"], [2]) → 2 
# interpret(1, ["+", "*"], [1, 3]) → 6
from collections import deque

def interpret(val,cmds,args):

    args = deque(args)
    for cmd in cmds:
        if cmd == '+':
            val = val + args.popleft()
        elif cmd == '-':
            val = val - args.popleft()
        elif cmd == '*':
            val = val * args.popleft()
        else:
            return -1

    return val


print(interpret(1, ['+'], [1]))
print(interpret(4, ['-'], [2]))
print(interpret(1, ['+', '*'], [1, 3]))