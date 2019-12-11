parts_of_speech = ['BLANK_1', 'BLANK_2', 'BLANK_3', 'BLANK_4']   
#the parts of the questions that will be replaced with user input answers.

answers_to_blanks = ['Python', 'programs', 'syntax', 'Guido van Rossum', 
                     'variable', '==', 'list', 'string', 
                     'function', 'def', 'colon', 'parameters' ]
#answers to the blanks in the questions. The answers are in order, 
#the first 4 are the 4 blanks in the easy level, the next 4 are the answers in the medium level, 
#and the last 4 are the answers in the hard level.

easy_level = """BLANK_1 is a high-level computer language. 
This computer language is used to write BLANK_2 that execute instructions 
to perform tasks for us using the computer. BLANK_3 is computer grammar. Python was created by BLANK_4."""

medium_level = """A BLANK_1 is an object that can have a value, expression, a string, or a list assigned to it. 
The BLANK_2 is the symbol used to assign a value to a variable. 
A BLANK_3 can be mutated and allied with another name, but a BLANK_4 cannot."""

hard_level = """A BLANK_1 is a block of code that can perform a single task mulitple times. 
A function begins with the keyword BLANK_2 and then is followed by the name, parentheses, 
and a BLANK_3. BLANK_4 and arguments go into the parentheses."""
#the different questions that will be asked and they are listed from easiest to hardest. 

greeting = raw_input('Hello, welcome to the Stage 2 Quiz: Press Enter to get started ')
ask_name = raw_input('Please enter your name: ')
prompt = raw_input('Select the level of difficulty: easy, medium, or hard ')
#the program opens with 3 input questions from the user

def level_difficulty(prompt): 
    """this is my function that will select which string the user will answer questions with. """
    if prompt == 'easy':     
        return easy_level
    elif prompt == 'medium':
        return medium_level
    elif prompt == 'hard':
        return hard_level

print "Thank you %s, you have chosen the %s level!" % (ask_name , prompt)
raw_input('Press Enter to begin quiz')  
#Repeat name and level difficulty back to user and prompt to begin quiz

print level_difficulty(prompt)           

def word_in_speech(word, parts_of_speech):  
    """this function compares my 2 lists to replace the answer with user input"""
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(question, parts_of_speech): 
    """this function is the heart of the game, it replaces the blank answers 
    with user input and creates the new sentence."""
    replaced_string = []                  
    question = question.split()
    for word in question:
        replacement = word_in_speech(word, parts_of_speech)
        if replacement != None:
            input = raw_input('Type in a word: ' + replacement + '? ')
            while input not in answers_to_blanks:
                input = raw_input('Incorrect, try again: ')
            if input in answers_to_blanks:
                print 'Correct!'
                word = word.replace(replacement, input)           
            replaced_string.append(word)
        else:
            replaced_string.append(word)
    new_string = " ".join(replaced_string)
    return new_string
         
print play_game(level_difficulty(prompt), parts_of_speech)
