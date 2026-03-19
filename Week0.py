#Indoor
#a=input("Enter value:")
#print(a.lower())

#Playback
#b=input("Enter value:")
#print(b.replace(" ","..."))

#Faces
'''def faces(value):
  value= value.replace(":)", "🙂").replace(":(", "🙁")
  return value
c=input("Enter value:")
print(faces(c))'''

#Einstien
m=int(input("Enter value: "))
E= m*9*10**16
print(E)




# Tip calculator

def tip(dollars, percent):
    a = dollars * percent
    return f"Leave ${a:.2f}"

dollars = float(input("How much was the meal? "))
percent = float(input("What percentage would you like to tip? ")) / 100

print(tip(dollars, percent))