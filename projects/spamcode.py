import pyautogui
import time

msg = input("What is the message you would like to spam? ")
spamcount = int(input("How many times? "))

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Spam Delivery Inbound")

for i in range(spamcount):
	pyautogui.write(msg + '\n')
