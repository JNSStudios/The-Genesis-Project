import random
import atexit
import time
import sys
from datetime import datetime
from contextlib import redirect_stdout
import os

highestIndex = 0
highestCorrectChar = ''
longestFullQuote = ""
currentIndex = 0
latestSetbackIndex = 0
latestIncorrectChar = ''
numOfChecks = 0
checksBetweenReports = 1000000

OUTPUTSTR = ""

filepath = os.path.dirname(os.path.realpath(__file__))

startDateTime = datetime.now()
dt_string = startDateTime.strftime("%m-%d-%Y %H.%M.%S")

def printAndSave(msg, newline):
    global OUTPUTSTR
    print(msg)
    if(newline is True):
        OUTPUTSTR += msg +"\n"
    else:
        OUTPUTSTR += msg
    

def printCurrentStats():
    global highestIndex, currentIndex, latestSetbackIndex, highestCorrectChar, latestIncorrectChar, longestFullQuote, start_time
    progTime = round(time.time() - start_time, 3)
    printAndSave(f"PROGRESS REPORT (once every {checksBetweenReports} checks)\nCurrent High Score: \"{longestFullQuote}\"\nLatest incorrect guess: Character \" {latestIncorrectChar} \" with index of {latestSetbackIndex}\nTotal number of letter checks: {numOfChecks}\nProgram has been running for a total of {progTime} seconds.\n", True)

def correctChar(character, quote):
    global highestIndex, currentIndex, highestCorrectChar, longestFullQuote
    currentIndex += 1
    if(highestIndex < currentIndex):
        highestIndex = currentIndex
        highestCorrectChar = character
        longestFullQuote = quote

def incorrectChar(character):
    global currentIndex, latestSetbackIndex, latestIncorrectChar
    latestSetbackIndex = currentIndex
    currentIndex = 0
    latestIncorrectChar = character

def exitProgram():
    global highestIndex, currentIndex, latestSetbackIndex, highestCorrectChar, latestIncorrectChar, longestFullQuote, start_time, dt_string
    progTime = round(time.time() - start_time, 3)
    checksPerSec = round(numOfChecks/progTime, 3)
    checksPerMin = round(checksPerSec*60,3)
    checksPerHour = round(checksPerMin*60,3)
    printAndSave(f"\n\nProgram exiting.\nHigh Score: \"{longestFullQuote}\"\n(Highest character of \" {highestCorrectChar} \" at index {highestIndex}/{len(quote)} ({round(highestIndex/len(quote), 4)}% through))\nLatest incorrect guess: Character \" {latestIncorrectChar} \" with index of {latestSetbackIndex}\nTotal number of letter checks: {numOfChecks}\nProgram ran for a total of {progTime} seconds.\nAverage of {checksPerSec} letter checks per second ({checksPerMin} per minute, {checksPerHour} per hour)\n", True)
    filename = f"Genesis Project Stats ({dt_string}).txt"
    print(f"This output will be saved under the file name \"{filename}\"\n")
    savefile = open(f"{filepath}\\{filename}", "w+")
    savefile.write(OUTPUTSTR)
    savefile.close()
  
   
charOpts = "a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 ."
acceptablePunctuation = '.,?!\'\"():;'
charOpts = charOpts.split()
charOpts.append(' ')
#print(charOpts)

# Can it reach the 15th sentence where God creates life?
quote = "In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light. And God saw the light, that it was good: and God divided the light from the darkness. And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day. And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so. And God called the firmament Heaven. And the evening and the morning were the second day. And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good. And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so. And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good. And the evening and the morning were the third day. And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also. And God set them in the firmament of the heaven to give light upon the earth, And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good. And the evening and the morning were the fourth day. And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven. And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good. And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. And the evening and the morning were the fifth day. And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good. And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. So God created man in his own image, in the image of God created he him; male and female created he them. And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth. And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat. And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so. And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."
quoteComplete = False

atexit.register(exitProgram)
"""
RULES FOR CHECKING CHARACTERS
Characters will be accepted whether or not they are upper- or lower-case. 
    If the program pulls an 'a' but the quote character says 'A', it still counts.
The period symbol is a stand-in for all puncuation. 
    If the program randomly chooses a period (.), comma (,), question/exclaimation mark (?) (!), apostraphe ('), quotation mark ("), open/close parenthesis (), colon (:), or semicolon (;), and the character from the quote is any of those characters, it is accepted.
"""



start_time = time.time()

printAndSave(f"\n- T H E  G E N E S I S   P R O J E C T -\nProgram started on {dt_string}\n", True)

while quoteComplete is False:
    if(currentIndex is len(quote)):
        quoteComplete = True
        break
    numOfChecks += 1
    if(numOfChecks % checksBetweenReports == 0):
        printCurrentStats()
    randomChar = charOpts[random.randrange(0, len(charOpts))].lower()
    currentQuoteChar = quote[currentIndex].lower()
    # print(f"Checking random character \" {randomChar} \" against current quote character of \" {currentQuoteChar} \" (Quote index: {str(currentIndex)}) ")
    # checks for all punctuation
    if(currentQuoteChar in acceptablePunctuation and randomChar == "."):
        print(f"\n\n\nP U N C T U A T I O N     M A T C H !\n\n\n")
        correctChar(randomChar, quote[:currentIndex+1])
    # checks for every other alphanumeric character (plus spaces)
    elif(currentQuoteChar == randomChar):
        # print(f"\n\n\nL E T T E R     M A T C H !\n\n\n")
        correctChar(randomChar, quote[:currentIndex+1])
    # all else fails and the random character doesn't match. 
    else:
        incorrectChar(randomChar)
