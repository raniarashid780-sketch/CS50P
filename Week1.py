#DEEP THOUGHT
#question=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").lower()
#if question == "42" or question == "forty-two" or question == "forty two":
 #   print("Yes")
#else:
#    print("No")

#HOME FEDERAL SAVINGS BANK
# greet=input("Greeting: ").lower().strip()
#if greet.startswith("hello"):
#    print("$0") 
#elif greet.startswith("h"):
#    print("$20")    
#else:    print("$100")

#FILE EXTENSIONS
# import os
# filename=input("File name: ")
# extension = os.path.splitext(filename)[1].lower()
# if extension == ".gif":
#     print("image/gif")
# elif extension == ".jpg" or extension == ".jpeg":
#     print("image/jpeg")
# elif extension == ".png":
#     print("image/png")
# elif extension == ".pdf":
#     print("application/pdf")
# elif extension == ".txt":
#     print("text/plain")
# elif extension == ".zip":
#     print("application/zip")
# else:
#     print("application/octet-stream")

#MATH INTERPRETER 
# expression = input("Expression: ")
# x, y, z = expression.split() 
# x = int(x)
# z = int(z)
# if y == "+":
#     result = x + z
# elif y == "-":
#     result = x - z
# elif y == "*":
#     result = x * z
# elif y == "/":
#     result = x / z
# print(f"{result:.1f}")

#MEAL CALCULATOR
def convert(meal):
        hours, minutes = meal.split(":")
        hours = int(hours)
        minutes = int(minutes) / 60
        return hours + minutes
    
def main():
        t = convert(input("What time is it? "))
        if 7 <= t < 8:
            print("breakfast time")
        elif 12 <= t < 13:
            print("lunch time")
        elif 18 <= t < 19:
            print("dinner time")
        else:
            print("not meal time")
    
if __name__ == "__main__":
        main()    