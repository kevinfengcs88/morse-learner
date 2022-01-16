# Morse Learner
Morse Learner is a browser automation script built with [selenium](https://www.selenium.dev/) that helps you learn Morse code by translating your strings (created from the 26
letters of the English alphabet) into Morse code sequences and then keying it on an online Morse code telegraph. 

https://user-images.githubusercontent.com/80129996/149639806-7dde14ef-8ecb-4059-b6be-c1f789047d00.mp4

## How to use
1. Star :star: this repo (definitely won't work if you don't) :3
2. Download the `.zip` file from this repository's file navigation and extract the `.exe` titled `MorseLearner.exe` (alternative: install the `.exe` from the [latest release](https://github.com/kevinfengcs88/morse-learner/releases/tag/v1.0))
3. Focus on the terminal and type in a string using characters from the 26 English letters
4. Press `RETURN` to send your string to the bot
5. Press "Clear" on the website to start the bot
6. Repeat steps 3-6

## Don't know Morse code?
Don't worry! There are plenty of resources that can facilitate your learning along with MorseLearner; here are just a few:
| URL | Description |
|---|---|
| https://www.youtube.com/watch?v=HY_OIwideLg | A great video from Michael "Vsauce" Stevens that explains mnemonics for the Morse code sequences of the alphabet (along with some very interesting commentary and fun facts from Michael, as expected). I would definitely recommend this video as a starting point, as mnemonics can really help to break that initial barrier of trying to translate letters, which are highly conceptual, to what is essentially short sequences in binary. |
| https://morse.withgoogle.com/learn/ | A fun Chrome experiment that teaches you Morse code sequencing through your own input of two buttons that represent the short signal, "dit," and the long signal, "dah." I wouldn't practice on this website too much; it will habituate you towards translating from English to Morse code through two separate inputs, rather than one input of two different types. |
| http://morsecode.me/?room=1 | A live Morse code radio chatroom with multiple channels that are sorted by WPM. Although you likely won't find more than one or two other people in the same channel as you, it's still fun to try to communicate with others through Morse code. The timings on the key inputs are pretty tight, though, and I wouldn't necessarily recommend it for a beginner's first single-input Morse code experience. |
| https://genemecija.github.io/learn-morse-code/ | The online Morse code telegraph that the Morse Learner script uses! Has much more lenient input timings than morsecode.me and displays what you're inputting live. The pause timing between letters is about half a second and the pause timing between words is about one second. Try out the challenge mode, and set the word count to 26. See if you can key all 26 letters without making a mistake or looking at a cheatsheet. Challenge mode can be toggled at the top of the web app. |

## Couldn't have done it without
- [genemecija's Morse code web app](https://github.com/genemecija/learn-morse-code)
- Everyone working on the selenium Python package; the [issues](https://github.com/SeleniumHQ/selenium/issues) were particularly helpful
- The extensive library of pages on browser automation through selenium in Python at [GeeksforGeeks](https://www.geeksforgeeks.org/browser-automation-using-selenium/)
- Stack Overflow (obviously:laughing:)
