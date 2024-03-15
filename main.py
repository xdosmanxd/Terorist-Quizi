import os
import json
import random
import requests
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
from io import BytesIO

with open("data.json", "r") as file:
	data = json.load(file)



orgut_listesi = [
"TİKB",
"TEVHİD-SELAM KUDÜS ORDUSU",
"TKP-ML Konferans",
"MLSPB",
"EL KAİDE",
"MLKP",
"TKP/ML",
"DHKP/C",
"DEAŞ",
"THKP/C",
"DKP/BÖG",
"DEVRİMCİ KARARGAH",
"FETÖ/PDY",
"MKP",
"HTŞ",
"PKK/KCK",
"İSLAMİ HAREKET ÖRGÜTÜ",
"TKEP/L",
"HİZBULLAH",
"Sivil"
]

wrong = 0
right = 0

def Civil_Question():
	r = requests.get("https://thispersondoesnotexist.com", headers={'User-Agent': 'My User Agent 1.0'}).content
	image = BytesIO(r)
	true_answer = "Sivil"
	answers = []
	for i in orgut_listesi:
		if i not in answers and len(answers) != 4 and i != true_answer:
			answers.append(i)
	random.shuffle(answers)
	return (image, answers, true_answer)
def Question():
	question = random.choice(data)
	true_answer = question["TOrgutAdi"]
	image_link = "https://www.terorarananlar.pol.tr" + question["GorselURL"][0]
	answers = []
	for i in orgut_listesi:
		if i not in answers and len(answers) != 4 and i != true_answer:
			answers.append(i)
	random.shuffle(answers)

	response = requests.get(image_link, verify=False)
	image = BytesIO(response.content)

	return (image, answers, true_answer)	
def Wrong():
	global wrong
	try:
		tkinter.messagebox.showinfo("Cevap", f"Yanlış cevap\nDoğrusu {true_answer} olacaktı.")
	except:
		tkinter.messagebox.showinfo("Cevap", f"Yanlış cevap\nDoğrusu {true_answer1} olacaktı.")
	wrong += 1
	update_question()
def Right():
	global right
	tkinter.messagebox.showinfo("Cevap", "Doğru cevap")
	right +=1
	update_question()

def update_question():
    global true_answer
    civil_or_not = random.randint(0, 4)
    if civil_or_not != 0:
        image, answers, true_answer = Question()
    if civil_or_not == 0:
        image, answers, true_answer = Civil_Question()	

    img = ImageTk.PhotoImage(Image.open(image).resize((800, 600)))
    label.config(image=img)
    label.image = img

    random.shuffle(answers)
    for i, button in enumerate(buttons):
        button.config(text=answers[i])
    button4.config(text=true_answer)

    label1.config(text=f"Yanlışlar: {wrong}")
    label2.config(text=f"Doğrular: {right}")

def main():
	global root, label, label1, label2, buttons, button4, true_answer1
	root = tk.Tk()
	root.title("Terörist Quiz")
	civil_or_not = random.randint(0, 4)
	if civil_or_not != 0:
		image, answers, true_answer1 = Question()
	if civil_or_not == 0:
		image, answers, true_answer1 = Civil_Question()	
	canvas = tk.Canvas(root, width=1000, height=750, bg="white")
	canvas.pack()

	bottomframe = tk.Frame(root)
	bottomframe.pack(side="bottom")

	frame = tk.Frame(root, bg="black", width=800, height=600)
	frame.place(relx=0.1)
	first_img = Image.open(image)
	first_img = first_img.resize((800, 600))
	img = ImageTk.PhotoImage(first_img)
	label = tk.Label(frame, image=img)
	label.pack()

	buttons = []

	button1 = tk.Button(bottomframe, text=answers[0], pady=20, padx=40, command=Wrong)
	button2 = tk.Button(bottomframe, text=answers[1], pady=20, padx=40, command=Wrong)
	button3 = tk.Button(bottomframe, text=answers[2], pady=20, padx=40, command=Wrong)
	button4 = tk.Button(bottomframe, text=true_answer1, pady=20, padx=40, command=Right)

	label1 = tk.Label(root, text=f"Yanlışlar: {right}")
	label1.pack()

	label2 = tk.Label(root, text=f"Doğrular: {wrong}")
	label2.pack()

	buttons.extend([button1, button2, button3, button4])
	random.shuffle(buttons)

	for i in buttons:
		i.pack(side="left")

	root.mainloop()
if __name__ == "__main__":
	main()
