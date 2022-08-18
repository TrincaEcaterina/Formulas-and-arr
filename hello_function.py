# HW1: upgrade the function with  parametr <name> - of person 
# when call   Hi en John --- Hello John
lang=input("Enter the language: ")
name=input("Enter your name: ")

def hi ( lang ):
    if lang == "en":
        print (f"Hello {name}")
    elif lang == "ru":
        print (f"Привет {name}")
    elif lang == "ro":
        print ( f"Salut {name}")
    else:
        print( f"Error {lang} is not recognize")

hi(lang)