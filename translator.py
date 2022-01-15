import sys


class Morse:
    def __init__(self, morse, text):
        self.morse = morse
        self.text = text


A = ".-"
B = "-..."
C = "-.-."
D = "-.."
E = "."
F = "..-."
G = "--."
H = "...."
I = ".."
J = ".---"
K = "-.-"
L = ".-.."
M = "--"
N = "-."
O = "---"
P = ".--."
Q = "--.-"
R = ".-."
S = "..."
T = "-"
U = "..-"
V = "...-"
W = ".--"
X = "-..-"
Y = "-.--"
Z = "--.."


def encode(english):
    if english.replace(" ", "").isalpha():
        m2 = Morse("", english)
        for char in english:
            if char.upper() == "A":
                m2.morse += A + " "
            elif char.upper() == "B":
                m2.morse += B + " "
            elif char.upper() == "C":
                m2.morse += C + " "
            elif char.upper() == "D":
                m2.morse += D + " "
            elif char.upper() == "E":
                m2.morse += E + " "
            elif char.upper() == "F":
                m2.morse += F + " "
            elif char.upper() == "G":
                m2.morse += G + " "
            elif char.upper() == "H":
                m2.morse += H + " "
            elif char.upper() == "I":
                m2.morse += I + " "
            elif char.upper() == "J":
                m2.morse += J + " "
            elif char.upper() == "K":
                m2.morse += K + " "
            elif char.upper() == "L":
                m2.morse += L + " "
            elif char.upper() == "M":
                m2.morse += M + " "
            elif char.upper() == "N":
                m2.morse += N + " "
            elif char.upper() == "O":
                m2.morse += O + " "
            elif char.upper() == "P":
                m2.morse += P + " "
            elif char.upper() == "Q":
                m2.morse += Q + " "
            elif char.upper() == "R":
                m2.morse += R + " "
            elif char.upper() == "S":
                m2.morse += S + " "
            elif char.upper() == "T":
                m2.morse += T + " "
            elif char.upper() == "U":
                m2.morse += U + " "
            elif char.upper() == "V":
                m2.morse += V + " "
            elif char.upper() == "W":
                m2.morse += W + " "
            elif char.upper() == "X":
                m2.morse += X + " "
            elif char.upper() == "Y":
                m2.morse += Y + " "
            elif char.upper() == "Z":
                m2.morse += Z + " "
            elif char == " ":
                m2.morse += "/ "
        return m2.morse
    else:
        for char in english:
            if char.isalpha():
                print("Error")
                sys.exit()
