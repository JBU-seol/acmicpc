int_stack = []
command_arr = []

def push(value):
    int_stack.append(value)

def pop():
    if len(int_stack) == 0:
        print("-1")
    else:
        print(int_stack[-1])
        del int_stack[-1]

def size():
    print(len(int_stack))

def Empty():
    if len(int_stack) == 0:
        print("1")
    else:
        print('0')

def top():
    if len(int_stack) == 0:
        print('-1')
    else:
        print(int_stack[-1])

question_number = input()
for n in range(int(question_number)):
    command = input()
    command_arr.append(command)

for command in command_arr:
    if command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        Empty()
    elif command == 'top':
        top()
    else:
        push(int(command.split()[1]))


