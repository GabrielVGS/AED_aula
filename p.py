import string
punc = string.punctuation

def remove_p(s:str) -> str:
    if s!= "":
        if s[-1] in punc:
            return s[:-1]
    return s

s = remove_p("hoje,  eu fui ao estadio!")
print(s)