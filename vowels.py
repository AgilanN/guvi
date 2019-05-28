a=input()

l=["a","e","i","o","u","A","E","I","U","O"]

if a.isnum():

	print("Invalid")
elif a in l:
	print("Vowels")

else:
    
	print("Consonants")