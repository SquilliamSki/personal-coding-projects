def user_choice():
	choice = int(input("""Please make a selection below:
(1) Password Generator 
(2) Ceaser Cipher Encrypter
(3) Die Roller
(4) Random Name Picker
(5) Smite Random God Picker
(6) Site Scraper\n """))
	if choice == 1:
		password_gen()
	elif choice == 2:
		cipher()
	elif choice == 3:
		dice_roller()
	elif choice == 4:
		name_picker()
	elif choice == 5:
		god_picker()
	elif choice == 6:
		site_scraper()
	else:
		print("Error...Please Enter a Valid Input")

def password_gen():
	import random, string
	password_length = int(input("How long would you like your password to be? "))
	password_characters = string.ascii_letters + string.digits + string.punctuation
	password = []
	for i in range(password_length):
		password.append(random.choice(password_characters))
	print("--------------------------------------------------------")
	print("You randomly generated password is: " + "".join(password))
	print("--------------------------------------------------------")

def cipher():
	input_text = input("What would you like to encode?\n")
	key_value = int(input("What key value would you like? "))
	
	def encryption(input_text,key_value):
		encoded = ""
		for i in range(len(input_text)): 
			char = input_text[i]
		if (char.isupper()):
			encoded += chr((ord(char) + key_value - 65) % 26 + 65)
		elif (char.islower()):
			encoded += chr((ord(char) + key_value - 97) % 26 + 97)
		elif (char.isdigit()):
			encoded += (int(char) + key_value) % 10
		else:
			encoded += (char)

	return encoded
	
	print("-------------------------------------")
	print(f"Original Text: {input_text}")
	print(f"Key Value: {key_value}")
	print(f"Cipher Text: {encryption(input_text,key_value)}")
	print("-------------------------------------")

def dice_roller():
	import random
	min = 1
	max = int(input("What would you like the max to be? "))

	roll_again = "Yes"
	while roll_again == "Yes" or roll_again == "y":
		print("Rolling the die...")
		print(f"The values are {random.randint(min, max)} and {random.randint(min, max)}.")
		roll_again = input("Would you liek to roll the die again? (y/n) ")

def name_picker():
	import random
	names = []
	add_more = "y"
	pre_detirm = input("Would you like to use a predetermined list of names? (y/n) ")
	if pre_detirm == "n":
		while add_more == "y":
			name_in = input("Please enter a name: ")
			names.append(name_in)
			add_more = input("Would you like to add another name? (y/n) ")
		print(f"The randomly chosen person is {random.choice(names)}.\n")
	else:
		pre_names = ["Will", "Joey", "Jason", "Darren"]
		print(f"The randomly chosen name is {random.choice(pre_names)}.\n")

def god_picker():
	import random
	Guardians = ['Ares', 'Artio', 'Athena', 'Bacchus', 'Cabrakan', 'Cerberus', 'Cthulhu', 'Fafnir', 'Ganesha', 'Geb', 'Jormungandr', 'Khepri', 'Kumbhakarna', 'Kuzenbo', 'Sobek', 'Sylvanus', 'Terra', 'Xing Tian', 'Yemoja', 'Ymir']
	Warriors = ['Achilles', 'Amaterasu', 'Bellona', 'Chaac', 'Cu Chulainn', 'Erlan Shen', 'Gilgamesh', 'Guan Yu', 'Hercules', 'Horus', 'King Arthur', 'Mulan', 'Nike', 'Odin', 'Osiris', 'Sun Wukong', 'Tyr', 'Vamana']
	Hunters = ['Ah Muzen Cab', 'Anhur', 'Apollo', 'Artemis', 'Cernunnos', 'Chernobog', 'Chiron', 'Cupid', 'Danzaburou', 'Hachman', 'Heimdallr', 'Hou Yi', 'Izanami', 'Jing Wei', 'Medusa', 'Neith', 'Rama', 'Skadi', 'Ullr', 'Xbalanque']
	Mages = ['Agni', 'Ah Puch', 'Anubis', 'Ao Kuang', 'Aphrodite', 'Baba Yaga', 'Baron Samedi', """Chang'e""", 'Chronos', 'Discordia', 'Freya', 'Hades', 'He Bo', 'Hel', 'Hera', 'Eset', 'Janus', 'Kukulklan', 'Merlin', 'Nox', 'Nu Wa', 'Olorun', 'Persephone', 'Poseidon', 'Ra', 'Raijin', 'Scylla', 'Sol', 'The Morrigan', 'Thoth', 'Tiamet', 'Vulcan', 'Zeus', 'Zhong Kui']
	Assasins = ['Arachne', 'Awilix', 'Bakasura', 'Bastet', 'Camasotz', 'Da ji', 'Fenrir', 'Hun Batz', 'Kali', 'Loki', 'Mercury', 'Ne Zha', 'Nemesis', 'Pele', 'Ratatoskr', 'Ravana', 'Serqet', 'Set', 'Susano', 'Thanatos', 'Thor', 'Tsukuyomi']
	go_again = "y"
	print("Welcome to the Smite God Randomizer")
	print(f"There are a total of {len(Guardians + Warriors + Hunters + Mages + Assasins)} Gods in the game.")
	print(f"Guardians = {len(Guardians)} | Warriors = {len(Warriors)} | Hunters = {len(Hunters)} | Mages = {len(Mages)} | Assasins = {len(Assasins)}")
	while go_again == "y":
		choice = int(input("""\nWhat role are you playing? 
			(1) Support
			(2) Carry
			(3) Mid
			(4) Solo
			(5) Jungle\n"""))
		if choice == 1:
			print(f"Your random Support God is {random.choice(Guardians + Warriors)}")
			go_again = input("Would you like to pick again? (y/n) ")
		elif choice == 2:
			print(f"Your random Carry God is {random.choice(Hunters)}")
			go_again = input("Would you like to pick again? (y/n) ")
		elif choice == 3:
			print(f"Your random Mid God is {random.choice(Mages + Hunters)}.")
			go_again = input("Would you like to pick again? (y/n) ")
		elif choice == 4:
			print(f"Your random Solo God is {random.choice(Warriors + Guardians)}.")
			go_again = input("Would you like to pick again? (y/n) ")
		elif choice == 5:
			print(f"Your random Jungle God is {random.choice(Assasins + Warriors)}.")
			go_again = input("Would you like to pick again? (y/n) ")
			
#def site_scraper():
	#import requests
	#from bs4 import BeautifulSoup
	#import random
	
	#def scrapeWikiArticle(url)
		#response = requests.get(
			#url = url,
			#)

		#soup = BeautifulSoup(response.content, "html.parser")

		#title = soup.find(id="firstHeading")
		#print(title.content)

		#alllinks = soup.find(id="bodyContent").find_all("a")
		#random.shuffle(alllinks)
		#linkToScrape = 0

		#for link in alllinks:
			#if link["href"].find("/wiki/") == -1:
				#continue

			#linkToScrape = link
			#break

		#scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape["href"])
	#scrapeWikiArticle("html://en.wikipedia.org/wiki/Web_scraping")

user_choice()
