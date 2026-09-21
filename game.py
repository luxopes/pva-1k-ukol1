import random as r

rand = r.randint(1, 100)
user_raw = input("Typni si cislo od 0 do 100: ")

user = int(user_raw)

if rand < user:
	print("Moc velke!")
elif rand > user:
	print("Moc male!")
elif rand == user:
	print("Super, mas bod")
else:
	print("Chyba! Zkuste to znovu")

print(f"Cislo bylo {rand}")
