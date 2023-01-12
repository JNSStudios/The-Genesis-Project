# The-Genesis-Project
A relatively-simple Python program that simulates the Infinite Monkey Theorem by randomly generating characters and punctuation, attempting to match against the first chapter of the book of Genesis. (Originally programmed in 2020)

# Synopsis
When the program is launched, it will start generating random characters (including letters, numbers, punctuation, and spaces). If it matches the current character in the string it is looking to match against, it will move onto the next character. If it doesn't match, it resets the string back to the beginning. The goal is for the program to generate the entire string using the randomly-generated characters in a single go, or to simulate how long such a thing would take. 
The program is designed to ignore letter case, and the current goal string is the first chapter of the book of Genesis, pasted below.
For every one million random character generations, the program will print out a report to the terminal. (Note that the frequency of the reports can be altered by changing the "checksBetweenReports" variable on Line 16 of the .py file.

An example report looks like this:
```
PROGRESS REPORT (once every 1000000 checks)
Current High Score: "In t"
Latest incorrect guess: Character " 5 " with index of 0
Total number of letter checks: 1000000
Program has been running for a total of 1.41 seconds.
```
To exit the program, simply terminate it with Ctrl+C in the terminal. The program will print out one last report, and save all the reports to a .txt file in the same directory as the .py file.


An example exit report looks like this:
```
Program exiting.
High Score: "In t"
(Highest character of " t " at index 4/4087 (0.001% through))
Latest incorrect guess: Character " 9 " with index of 0
Total number of letter checks: 2943122
Program ran for a total of 4.05 seconds.
Average of 726696.79 letter checks per second (43601807.4 per minute, 2616108444.0 per hour)

This output will be saved under the file name "Genesis Project Stats (01-12-2023 11.44.16).txt"
```
# Acceptable Characters
a b c d e f g h i j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 . , ? ! ' " ( ) : ; (space)

# Goal string
"In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light. And God saw the light, that it was good: and God divided the light from the darkness. And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day. And God said, Let there be a firmament in the midst of the waters, and let it divide the waters from the waters. And God made the firmament, and divided the waters which were under the firmament from the waters which were above the firmament: and it was so. And God called the firmament Heaven. And the evening and the morning were the second day. And God said, Let the waters under the heaven be gathered together unto one place, and let the dry land appear: and it was so. And God called the dry land Earth; and the gathering together of the waters called he Seas: and God saw that it was good. And God said, Let the earth bring forth grass, the herb yielding seed, and the fruit tree yielding fruit after his kind, whose seed is in itself, upon the earth: and it was so. And the earth brought forth grass, and herb yielding seed after his kind, and the tree yielding fruit, whose seed was in itself, after his kind: and God saw that it was good. And the evening and the morning were the third day. And God said, Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days, and years: And let them be for lights in the firmament of the heaven to give light upon the earth: and it was so. And God made two great lights; the greater light to rule the day, and the lesser light to rule the night: he made the stars also. And God set them in the firmament of the heaven to give light upon the earth, And to rule over the day and over the night, and to divide the light from the darkness: and God saw that it was good. And the evening and the morning were the fourth day. And God said, Let the waters bring forth abundantly the moving creature that hath life, and fowl that may fly above the earth in the open firmament of heaven. And God created great whales, and every living creature that moveth, which the waters brought forth abundantly, after their kind, and every winged fowl after his kind: and God saw that it was good. And God blessed them, saying, Be fruitful, and multiply, and fill the waters in the seas, and let fowl multiply in the earth. And the evening and the morning were the fifth day. And God said, Let the earth bring forth the living creature after his kind, cattle, and creeping thing, and beast of the earth after his kind: and it was so. And God made the beast of the earth after his kind, and cattle after their kind, and every thing that creepeth upon the earth after his kind: and God saw that it was good. And God said, Let us make man in our image, after our likeness: and let them have dominion over the fish of the sea, and over the fowl of the air, and over the cattle, and over all the earth, and over every creeping thing that creepeth upon the earth. So God created man in his own image, in the image of God created he him; male and female created he them. And God blessed them, and God said unto them, Be fruitful, and multiply, and replenish the earth, and subdue it: and have dominion over the fish of the sea, and over the fowl of the air, and over every living thing that moveth upon the earth. And God said, Behold, I have given you every herb bearing seed, which is upon the face of all the earth, and every tree, in the which is the fruit of a tree yielding seed; to you it shall be for meat. And to every beast of the earth, and to every fowl of the air, and to every thing that creepeth upon the earth, wherein there is life, I have given every green herb for meat: and it was so. And God saw every thing that he had made, and, behold, it was very good. And the evening and the morning were the sixth day."
