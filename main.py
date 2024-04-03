from passwordmaker import PasswordMaker

word = PasswordMaker(20)
word.generate()

print(word.password)