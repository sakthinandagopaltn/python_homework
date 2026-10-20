# Task 1 
def hello():
    return "Hello!"

# Task 2
def greet(name):
    return f"Hello, {name}!"

# Task 3
def calc(num1, num2, op='multiply'):
    try:
        match op:
            case 'add':
                return num1 + num2
            case 'subtract':
                return num1 - num2
            case 'multiply':
                try:
                    return num1 * num2
                except TypeError:
                    return "You can't multiply those values!"
            case 'divide':
                return num1 / num2
            case 'modulo':
                return num1 % num2
            case 'int_divide':
                return num1 // num2
            case 'power':
                return num1 ** num2
            case _:
                return "Unknown operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"

#Task 4
def data_type_conversion(value,type):
    try:
        if type=='float':
            return float(value)
        elif type == 'int':
            return int(value)
        elif type == 'str':
            return str(value)
        else:
            return f"You can't convert {value} into a {type}."
    except ValueError:
        return f"You can't convert {value} into a {type}."

#Task 5
def grade(*args):
    try:
        total = sum(args)
        num = len(args)
        marks=total/num
    except:
        return f"Invalid data was provided."
    else:
        if marks>=90 and marks<=100:
            return 'A'
        elif marks>=80 and marks<=89:
            return 'B'
        elif marks>=70 and marks<=79:
            return 'C'
        elif marks>=60 and marks<=69:
            return 'D'
        else:
            return 'F'

# Task 6
def repeat(string,count):
    text=""
    for i in range(count):
        text=text+string
    return text

# Task 7
def student_scores(mode, **kwargs):
    if mode == 'best':
        return max(kwargs, key=kwargs.get)
    elif mode == 'mean':
        return sum(kwargs.values()) / len(kwargs)

# Task 8
def titleize(string):
    little=["a", "on", "an", "the", "of", "and", "is", "in"]
    words=string.split()
    for i,word in enumerate(words):
        if i==0 or i==len(words)-1 or word.lower() not in little:
            words[i]=word.capitalize()
    return " ".join(words)

# Task 9
def hangman(secret,guess):
    answer=''
    for alphabet in secret:
        if alphabet in guess:
            answer=answer+alphabet
        else:
            answer=answer+'_'
    return answer

# Task 10
def pig_latin(string):
    vowels='aeiou'
    result = []
    for word in string.split():
        consonants = ""      
        rest = ""          
        found_vowel = False
        i = 0
        while i < len(word):
            letter = word[i]
            if found_vowel:
                rest += letter
            elif letter in vowels:
                found_vowel = True
                rest += letter
            elif letter == "q" and i + 1 < len(word) and word[i + 1] == "u":
                consonants += "qu"
                i += 1    
            else:
                consonants += letter
            i += 1
        result.append(rest + consonants + "ay")
    return " ".join(result)
            
                


            

    