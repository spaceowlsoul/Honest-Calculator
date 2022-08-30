msg_ = [
       'Enter an equation\n',
       'Do you even know what numbers are? ',
       "Yes ... an interesting math operation. You've slept through "
       "all classes, haven't you?",
       'Yeah... division by zero. Smart move...',
       'Do you want to store the result? (y / n):\n',
       'Do you want to continue calculations? (y / n):\n',
       ' ... lazy',
       ' ... very lazy',
       ' ... very, very lazy',
       'You are',
       'Are you sure? It is only one digit! (y / n)\n',
       "Don't be silly! It's just one number! Add to the memory? (y / n)\n",
       'Last chance! Do you really want to embarrass yourself? (y / n)\n'
    ]

operators = ['+', '-', '*', '/']
memory = 0


def main():
    while True:
        x, operator, y = check_input()
        check_laziness(x, operator, y)
        result = calculation(x, operator, y)
        memorizing(result)
        continue_calculations = input(msg_[5])
        if continue_calculations == 'y':
            continue
        else:
            break


def check_input():
    while True:
        x, operator, y = input(msg_[0]).split(' ', 3)
        if x == 'M':
            x = memory
        if y == 'M':
            y = memory
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print(msg_[1])
            continue
        if operator not in operators:
            print(msg_[2])
            continue
        elif operator == operators[3] and y == 0:
            check_laziness(x, operator, y)
            print(msg_[3])
            continue
        return x, operator, y


def is_one_digit(v):
    if 10 > v > -10 and v.is_integer():
        return True
    else:
        return False


def check_laziness(x, operator, y):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_[6]
    if (x == 1 or y == 1) and operator == operators[2]:
        msg = msg + msg_[7]
    if (x == 0 or y == 0) and (operator == operators[0] or operator == operators[1] or operator == operators[2]):
        msg = msg + msg_[8]
    if msg != '':
        msg = msg_[9] + msg
    print(msg)


def calculation(x, operator, y):
    result = 0
    if operator == operators[0]:
        result = x + y
    elif operator == operators[1]:
        result = x - y
    elif operator == operators[2]:
        result = x * y
    elif operator == operators[3]:
        result = x / y
    print(result)
    return result


def memorizing(result):
    global memory
    store_result = input(msg_[4])
    if store_result == 'y':
        if is_one_digit(result):
            msg_index = 10
            while True:
                sure_question = input(msg_[msg_index])
                if sure_question == 'y':
                    if msg_index < 12:
                        msg_index += 1
                        continue
                    else:
                        memory = result
                        break
                elif sure_question == 'n':
                    break
                else:
                    continue
        else:
            memory = result
    elif store_result == 'n':
        pass


if __name__ == '__main__':
    main()
