import random

LettreMaj = "abcdefghijklmnopqrstuvwxyz"
LettreMin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Chiffre = "0123456789"
symbole = "()[]{}#,;:!+=/\_-"


A = LettreMaj + LettreMin + Chiffre + symbole

Lenght = 10


Password = "".join(random.sample(A, Lenght))
print(Password)
