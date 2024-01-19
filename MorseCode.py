#%%
def Build_Character_Encoder():
    '''
    return Character_Encoder, a dictionary
    Specification:
        Character_Encoder is a mapping from Character to Morse Code
        Every character in list('abcdefghijklmnopqrstuvwxyz0123456789') can be encoded in Morse code:
            Character_Encoder['a'] is '.-', which means 'a' is encoded to '.-' (Morse code)
            Character_Encoder['0'] is '-----'
        see https://en.wikipedia.org/wiki/Morse_code
        Let's 'enhance' Morse code to handle other characters
        Every character in list("""`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?""") is encoded to '.-.-.-'
            Character_Encoder['@'] is '.-.-.-'
            Character_Encoder['#'] is '.-.-.-'
        Now, every character on computer keyboard can be represented by Morse code
    '''
    # CodeList1 contains Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # CodeList2 contains Morse codes of the 10 integers from 0 to 9
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    CodeList3 = ['.-.-.-']*32
    # define three lists of characters
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')
    CharList3 = list("""`~!@#$%^&*()-_=+[{]}\|;:'",<.>/?""") #32
    # define an empty dictionary
    Character_Encoder={}
    # add your code from here to create your dictionary mapping. Do NOT manually create it.
    CodeList3 = ['.-.-.-']*32
    CharListAll = CharList1 + CharList2 + CharList3
    CodeListAll = CodeList1 + CodeList2 + CodeList3

    for n in range(0,(len(CharListAll))):
        Character_Encoder[CharListAll[n]] = CodeListAll[(n)]

    # Use the lists defined above to generate the dictionary key-value pairs.

    return Character_Encoder

#%%
def Build_Character_Decoder():
    '''

            Character_Decoder is a mapping from Morse Code to Character
            Character_Decoder['.-'] is 'a', which means '.-' is decoded to 'a'
        All decoded letters are in lower case
            '.-' is 'a', not 'A'
        The special Morse code '.-.-.-' is decoded to '#':
             Character_Decoder['.-.-.-']  is '#'
    '''
    # add your code from here
# CodeList1 contains Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # CodeList2 contains Morse codes of the 10 integers from 0 to 9
# CodeList1 contains Morse codes of the 26 English letters (a to z)
    CodeList1 = ['.-','-...','-.-.','-..','.','..-.','--.','....','..',
                 '.---','-.-','.-..','--','-.','---','.--.','--.-','.-.',
                 '...','-','..-','...-','.--','-..-','-.--','--..']
    # CodeList2 contains Morse codes of the 10 integers from 0 to 9
    CodeList2 = ['-----', '.----', '..---', '...--', '....-', '.....',
                 '-....', '--...', '---..', '----.']
    CodeList3 = ['.-.-.-']
    # define three lists of characters
    CharList1 = list('abcdefghijklmnopqrstuvwxyz')
    CharList2 = list('0123456789')
    CharList3 = list('#')

    # define an empty dictionary

    Character_Decoder={}
    # add your code from here to create your dictionary mapping. Do NOT manually create it.
    CharListAll = CharList1 + CharList2 + CharList3
    CodeListAll = CodeList1 + CodeList2 + CodeList3

    for n in range(0,(len(CharListAll))):
        Character_Decoder[CodeListAll[n]] = CharListAll[n]

    return Character_Decoder
# %%
def Word_Encoder(Word, Character_Encoder=None):
    '''
    Word is an english word (str), e.g. 'Python'
    Character_Encoder is from BuildEncoder
    return Word_in_Morse_Code
    a blank space is added between the two Morse codes of two adjacent letters in Word
    Examples: (enable the option Source->Show Blank Spaces in Sypder)
        Word "Gin" is converted to lowercase 'gin'
        then, "gin" is encoded to Word_in_Morse_Code "--. .. -." (NOT "--...-.")
    '''
    if Character_Encoder == None:
        Character_Encoder = Build_Character_Encoder()
    # add your code from here
    Word = Word.lower()
    Word = list(Word)
    encoded_morse = []
    for n in Word:
        to_morse = Character_Encoder[n]
        encoded_morse.append(to_morse)

    Word_in_Morse_Code = ''
    for n in range(0, len(encoded_morse)):
        Word_in_Morse_Code += encoded_morse[n]
        if n < (len(encoded_morse)-1):
            Word_in_Morse_Code += ' '

    return Word_in_Morse_Code
# %%
def Word_Decoder(Word_in_Morse_Code, Character_Decoder=None):
    '''
    Word_in_Morse_Code is from Word_Encoder
    Character_Decoder is from Build_Character_Decoder
    return the Word in Engilish
    Examples:
        Word_in_Morse_Code "--. .. -." is decoded to Word "gin" in English
        Word_in_Morse_Code "--. .. -. .-.-.-" is decoded to Word "gin#" in English
    '''
    if Character_Decoder == None:
        Character_Decoder = Build_Character_Decoder()
    # add your code from here
    Word_in_Morse_Code = Word_in_Morse_Code.split()
    Word_in_Morse_Code = list(Word_in_Morse_Code)
    decoded_word = []
    for n in Word_in_Morse_Code:
        to_word = Character_Decoder[n]
        decoded_word.append(to_word)

    Word = ''
    for n in range(0, len(decoded_word)):
        Word += decoded_word[n]
        if n < (len(decoded_word)-1):
            Word += ' '
    Word = Word.replace(" ","")


    return Word
# %%
def Message_Encoder(Message, Character_Encoder=None):
    '''
    Message is an english sentence (str)
    Character_Encoder is from Build_Character_Encoder
    return Message_in_Morse_Code (str)
    steps:
    (1) split Message to words
    (2) use Word_Decoder to transform each word to Morse codes
    (3) add a comma between Morse codes of two adjacent words in Message
        before concatenating all Morse codes into a string
    Message_in_Morse_Code is the concatenation of all Morse codes, blank spaces and commas
    Examples:
        Message 'Hello Python 3.6'-> ['Hello', 'Python', '3.6']
        'Hello' is transformed to '.... . .-.. .-.. ---'
        'Python' is transformed to '.--. -.-- - .... --- -.'
        '3.6' is transformed to '...-- .-.-.- -....'
        Message 'Hello Python 3.6' is transformed to Message_in_Morse_Code:
            '.... . .-.. .-.. ---,.--. -.-- - .... --- -.,...-- .-.-.- -....'
    '''
    if Character_Encoder == None:
        Character_Encoder = Build_Character_Encoder()
    # add your code from here
    Message_in_Morse_Code = []
    Message = Message.lower().split()
    for wordtomorse in Message:
        encoded_Message = Word_Encoder(wordtomorse)
        Message_in_Morse_Code.append(encoded_Message)
    Message_in_Morse_Code= ','.join(Message_in_Morse_Code)


    return Message_in_Morse_Code


# %%
def Message_Decoder(Message_in_Morse_Code, Character_Decoder=None):
    '''
    Message_in_Morse_Code is from Message_Encoder
    Character_Decoder is from Build_Character_Decoder
    return the Message in English
    Examples:
        Message_in_Morse_Code is
        '.... . .-.. .-.. ---,.--. -.-- - .... --- -.,...-- .-.-.- -....'
        It is transformed/decoded to Message 'hello python 3#6' in English
    '''
    if Character_Decoder == None:
        Character_Decoder = Build_Character_Decoder()
    # add your code from here
    Message = []
    Message_in_Morse_Code = Message_in_Morse_Code.split(',')
    for morsetoword in Message_in_Morse_Code:
        decoded_Message = Word_Decoder(morsetoword)
        Message.append(decoded_Message)
    Message = ' '.join(Message)

    return Message
