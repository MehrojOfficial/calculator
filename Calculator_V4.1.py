"""
</>
Date: 3:33
Time: 05.16.2021
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Calculator (SFF/DFF)"
</>
"""
from tkinter import *
import math
root = Tk()
root.title("Calculator V4.1 (SFF)")
root.configure(bg='#D9E4F1')
root.geometry("350x215")
root.iconbitmap(r"data/icon.ico")
root.resizable(False,False)

# Photos
photo_1 = PhotoImage(file = "data/num1.png")
photo_2 = PhotoImage(file = "data/num2.png")
photo_3 = PhotoImage(file = "data/num3.png")
photo_4 = PhotoImage(file = "data/num4.png")
photo_5 = PhotoImage(file = "data/num5.png")
photo_6 = PhotoImage(file = "data/num6.png")
photo_7 = PhotoImage(file = "data/num7.png")
photo_8 = PhotoImage(file = "data/num8.png")
photo_9 = PhotoImage(file = "data/num9.png")
photo_0 = PhotoImage(file = "data/num0.png")
photo_dot = PhotoImage(file = "data/dot.png")
photo_plus = PhotoImage(file = "data/plus.png") 
photo_minus = PhotoImage(file = "data/minus.png") 
photo_multi = PhotoImage(file = "data/multi.png")
photo_div = PhotoImage(file = "data/div.png")
photo_equel = PhotoImage(file = "data/equel.png")
photo_clr = PhotoImage(file = "data/clear.png")
photo_row = PhotoImage(file = "data/x2.png")
photo_sqrt = PhotoImage(file = "data/sqrt.png")
photo_fclr = PhotoImage(file = "data/fclr.png")
photo_dff = PhotoImage(file = "data/dff.png")
photo_left = PhotoImage(file = "data/left.png")
photo_right= PhotoImage(file = "data/right.png")

e_result = ""

sff_mode = Frame(root)
sff_mode.grid(column = 0, row = 0)

gui = Frame(root)

display = Entry(sff_mode,borderwidth = 7,width = 30,fg = "black", bg = "#F2F7FC", font = ("Arial",15))
display.grid(column = 0, row = 1, padx = 3, pady = 3, columnspan = 5)
display.bind("<1>", lambda e: "break")

def cmdnum1(event = None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"1")

def cmdnum2(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"2")

def cmdnum3(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"3")

def cmdnum4(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"4")

def cmdnum5(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"5")

def cmdnum6(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"6")

def cmdnum7(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"7")

def cmdnum8(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"8")

def cmdnum9(event=None):
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"9")

def cmdnum0(event=None):
	list1 = []
	test1 = display.get()
	e_value = len(list1) - 1
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_list1 = len(list1) - 1
	if len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif len(display.get()) < 28:
		display.insert(len(display.get())+1,"0")

def cmdsign_dot(event=None):
	list1 = []
	test1 = display.get()
	e_value = len(list1) - 1
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_list1 = len(list1) - 1
	if list1[0] == '+' or list1[0] == '' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif list1[0] != '.' and list1[0] != '' and len(display.get()) < 28:
		display.insert(len(display.get())+1,".")

def cmdsign_plus(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if list1[0] == '+' or list1[0] == '' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "+":
		global e_result
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," + ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "-":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," + ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "*":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," + ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "/":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," + ")
		e_result = ""
	elif list1[0] != '+' and list1[0] != '' and len(display.get()) < 28:
		display.insert(len(display.get())+1," + ")

def cmdsign_minus(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if list1[0] == '+' or list1[0] == '' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "+":
		global e_result
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," - ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "-":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," - ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "*":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," - ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "/":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," - ")
		e_result = ""
	elif list1[0] != '-' and list1[0] != '' and len(display.get()) < 28:
		display.insert(len(display.get())+1," - ")

def cmdsign_multilpy(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if list1[0] == '+' or list1[0] == '' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "+":
		global e_result
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," * ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "-":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," * ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "*":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," * ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "/":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," * ")   
		e_result = ""
	elif list1[0] != '*' and list1[0] != '' and len(display.get()) < 28:
		display.insert(len(display.get())+1," * ")

def cmdsign_devide(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if list1[0] == '+' or list1[0] == '' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 28:
		display.insert(len(display.get())+1,"")
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "+":
		global e_result
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," / ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "-":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," / ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '+' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "*":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," / ")
		e_result = ""
	elif e_value + 1 == 3 and list1[0] != '' and list1[0] != '' and len(display.get()) < 28 and list1[1] == "/":
		e_result = e_result + display.get()
		e_result = eval(e_result)
		display.delete(first = 0, last = 999)
		display.insert(len(display.get())+1,e_result)
		display.insert(len(display.get())+1," / ")
		e_result = ""
	elif list1[0] != '/' and list1[0] != '' and len(display.get()) < 28:
		display.insert(len(display.get())+1," / ")

def cmdsign_equel(event=None):
	global e_result
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		if xxss == "":
			pass
		else:
			list1.insert(0,xxss)
	e_value = len(list1) - 1
	e_result = str(e_result) + (display.get())
	if list1[0] == "+" or list1[0] == "-" or list1[0] == "/" or list1[0] == "*" or list1[0].endswith(".") == True:
		pass
	else:
		e_result = eval(e_result)
	e_result = str(e_result)
	if str(e_result).endswith(".0"):
		e_result = str(e_result).rstrip(".0")
	else:
		e_result = e_result
	display.delete(first = 0, last = 999)
	display.insert(0,e_result)
	e_result = ""

def cmdsign_clear(event=None):
	list1 = []
	test1 = display.get()
	e_value = len(list1) - 1
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_list1 = len(list1) - 1
	if list1[0] == '+' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0] == '':
		display.delete(first = len(display.get()) - 1, last = len(display.get()))
		display.delete(first = len(display.get()) - 1, last = len(display.get()))
		display.delete(first = len(display.get()) - 1, last = len(display.get()))
	else:
		display.delete(first = len(display.get()) - 1, last = len(display.get()))

def cmdsign_row(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if len(list1) == 1:
		e_result = float(list1[0])**2
		if str(e_result).endswith(".0"):
			e_result = str(e_result)
			e_result = e_result.rstrip(".0")
		else:
			e_result = e_result
	elif list1[0] != '+' or list1[0] != '-' or list1[0] != '*' or list1[0] != '/' or list1[0] != '.' or list1[0] != '':
		e_result = display.get()
	display.delete(first = 0, last = 999)
	display.insert(0,e_result)

def cmdsign_sqrt(event=None):
	list1 = []
	test1 = display.get()
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_value = len(list1) - 1
	if len(list1) == 1:
		e_result = math.sqrt(float(list1[0]))
		if str(e_result).endswith(".0"):
			e_result = str(e_result)
			e_result = e_result.rstrip(".0")
		else:
			e_result = e_result
	elif list1[0] != '+' or list1[0] != '-' or list1[0] != '*' or list1[0] != '/' or list1[0] != '.' or list1[0] != '':
		e_result = display.get()
	display.delete(first = 0, last = 999)
	display.insert(0,e_result)

def cmdsign_fclear(event=None):
	list1 = []
	test1 = display.get()
	e_value = len(list1) - 1
	for xxss in(test1.split(" ")):
		list1.insert(0,xxss)
	e_list1 = len(list1) - 1
	display.delete(first = 0, last = 999)

def quit(event = None):
	root.quit()

def cmdback_page(event = None):
	gui.grid_forget()
	sff_mode.grid(column = 0, row = 0)
	root.title("Calculator V4.1 (SFF)")
	root.configure(bg='#D9E4F1')
	root.geometry("350x215")
	root.iconbitmap(r"data/icon.ico")
	root.resizable(False,False)

def cmdnext_page(event = None):
	sff_mode.grid_forget()
	gui.grid(column = 0, row = 0)
	root.title("Calculator V4.1 (DFF)")
	root.configure(bg='#D9E4F1')
	root.geometry("400x215")
	root.resizable(False,False)
	root.iconbitmap(r"data/icon.ico")
	e_result = ""
	display = Entry(gui,borderwidth = 5,width = 35,fg = "black", bg = "#F2F7FC", font = ("Arial",15))
	display.grid(column = 0, row = 0, padx = 3, pady = 3, columnspan = 5)
	display.bind("<1>", lambda e: "break")

	test = Label(gui, width = 29,borderwidth = 3,fg = "black", bg = "#E9F0F8")

	def cmddnum1(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"1")

	def cmddnum2(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"2")

	def cmddnum3(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"3")

	def cmddnum4(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"4")

	def cmddnum5(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"5")

	def cmddnum6(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"6")

	def cmddnum7(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"7")

	def cmddnum8(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"8")

	def cmddnum9(event=None):
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"9")

	def cmddnum0(event=None):
		list1 = []
		test1 = display.get()
		e_value = len(list1) - 1
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
			e_list1 = len(list1) - 1
		if len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif len(display.get()) < 34:
			display.insert(len(display.get())+1,"0")
	def cmddsign_dot(event=None):
		list1 = []
		test1 = display.get()
		e_value = len(list1) - 1
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_list1 = len(list1) - 1
		if list1[0] == '+' or list1[0] == '' or list1[0] == "(" or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif list1[0] != '.' and list1[0] != '' and len(display.get()) < 34:
			display.insert(len(display.get())+1,".")

	def cmdsign_plus(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_value = len(list1) - 1
		if list1[0] == '+' or list1[0] == '' or list1[0] == "(" or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif list1[0] != '+' and list1[0] != '' and len(display.get()) < 34:
			display.insert(len(display.get())+1," + ")

	def cmdsign_minus(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
			e_value = len(list1) - 1
		if list1[0] == '+' or list1[0] == '' or list1[0] == "(" or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif list1[0] != '-' and list1[0] != '' and len(display.get()) < 34:
			display.insert(len(display.get())+1," - ")

	def cmdsign_multilpy(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_value = len(list1) - 1
		if list1[0] == '+' or list1[0] == '' or list1[0] == "(" or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif list1[0] != '*' and list1[0] != '' and len(display.get()) < 34:
			display.insert(len(display.get())+1," * ")

	def cmdsign_devide(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_value = len(list1) - 1
		if list1[0] == '+' or list1[0] == '' or list1[0] == "(" or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0].endswith(".") == True or len(display.get()) >= 34:
			display.insert(len(display.get())+1,"")
		elif list1[0] != '/' and list1[0] != '' and len(display.get()) < 34:
			display.insert(len(display.get())+1," / ")

	def cmdsign_equel(event=None):
		global e_result
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			if xxss == "":
				pass
			else:
				list1.insert(0,xxss)
		e_result = str(e_result) + (display.get())
		if list1[0] == "+" or list1[0] == "-" or list1[0] == "/" or list1[0] == "*" or list1[0].endswith(".") == True or list1[0].endswith("(") == True:
			pass
		else:
			ba = display.get().count("(")
			ca = display.get().count(")")
			if ba == ca:
				e_result = str(e_result)
				e_result = eval(e_result)
			else:
				pass
		if str(e_result).endswith(".0"):
			e_result = str(e_result).rstrip(".0")
		else:
			e_result = e_result
		test.configure(text = e_result)
		display.delete(first = 0, last = 999)
		display.insert(0,e_result)
		e_result = ""

	def cmdsign_clear(event=None):
		list1 = []
		test1 = display.get()
		e_value = len(list1) - 1
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
			e_list1 = len(list1) - 1
		if list1[0] == '+' or list1[0] == '-' or list1[0] == '*' or list1[0] == '/' or list1[0] == '':
			display.delete(first = len(display.get()) - 1, last = len(display.get()))
			display.delete(first = len(display.get()) - 1, last = len(display.get()))
			display.delete(first = len(display.get()) - 1, last = len(display.get()))
		else:
			display.delete(first = len(display.get()) - 1, last = len(display.get()))

	def cmdsign_row(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_value = len(list1) - 1
		if len(list1) == 1:
			e_result = float(list1[0])**2
			if str(e_result).endswith(".0"):
				e_result = str(e_result)
				e_result = e_result.rstrip(".0")
			else:
				e_result = e_result
		elif list1[0] != '+' or list1[0] != '-' or list1[0] != '*' or list1[0] != '/' or list1[0] != '.' or list1[0] != '':
			e_result = display.get()
		display.delete(first = 0, last = 999)
		display.insert(0,e_result)

	def cmdsign_sqrt(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_value = len(list1) - 1
		if len(list1) == 1:
			e_result = math.sqrt(float(list1[0]))
			if str(e_result).endswith(".0"):
				e_result = str(e_result)
				e_result = e_result.rstrip(".0")
			else:
				e_result = e_result
		elif list1[0] != '+' or list1[0] != '-' or list1[0] != '*' or list1[0] != '/' or list1[0] != '.' or list1[0] != '':
			e_result = display.get()
		display.delete(first = 0, last = 999)
		display.insert(0,e_result)

	def cmdsign_fclear(event=None):
		list1 = []
		test1 = display.get()
		e_value = len(list1) - 1
		for xxss in(test1.split(" ")):
			list1.insert(0,xxss)
		e_list1 = len(list1) - 1
		display.delete(first = 0, last = 999)

	def cmdqavs_left(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			if xxss == "":
				pass
			else:
				list1.insert(0,xxss)
		e_value = len(list1) - 1

		if len(display.get()) >= 34:
			pass

		else:
			if len(display.get()) <= 34:
				if len(list1) >= 1:
					if list1[0] == "+" or list1[0] == "-" or list1[0] == "*" or list1[0] == "/" or list1[0].endswith("("):
						display.insert(len(display.get())+1,"(")
					else:
						pass
				elif len(list1) == 0:
					display.insert(len(display.get())+1,"(")
			else:
				pass

	def cmdqavs_right(event=None):
		list1 = []
		test1 = display.get()
		for xxss in(test1.split(" ")):
			if xxss == "":
				pass
			else:
				list1.insert(0,xxss)
		e_value = len(display.get()) - 1
		a = "(" in display.get()

		if len(display.get()) >= 34:
			pass
			
		elif len(display.get()) <= 34:
			if len(list1) >= 1: 
				if list1[0] != "+" and list1[0] != "-" and list1[0] != "*" and list1[0] != "/" and list1[0].endswith(".") == False and list1[0].endswith("(") == False and a == True:
					display.insert(len(display.get())+1,")")
				else:
					pass
			else:
				pass

	root.bind('<Escape>',quit)
	root.bind('<Return>',cmdsign_equel)
	root.bind('1',cmddnum1)
	root.bind('2',cmddnum2)
	root.bind('3',cmddnum3)
	root.bind('4',cmddnum4)
	root.bind('5',cmddnum5)
	root.bind('6',cmddnum6)
	root.bind('7',cmddnum7)
	root.bind('8',cmddnum8)
	root.bind('9',cmddnum9)
	root.bind('0',cmddnum0)
	root.bind('.',cmddsign_dot)
	root.bind('+',cmdsign_plus)
	root.bind('-',cmdsign_minus)
	root.bind('*',cmdsign_multilpy)
	root.bind('/',cmdsign_devide)
	root.bind('(',cmdqavs_left)
	root.bind(')',cmdqavs_right)
	root.bind("<BackSpace>",cmdsign_clear)
	root.bind("<Delete>",cmdsign_fclear)

	num_1 = Button(gui, image = photo_1, command = cmddnum1, borderwidth = 3,fg = "#1E395B", bg = '#E9F0F8')
	num_1.grid(column = 0, row = 3, padx = 3, pady = 3)
	num_1.config( height = 20, width = 60 )

	num_2 = Button(gui, image = photo_2, command = cmddnum2, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_2.grid(column = 1, row = 3, padx = 3, pady = 3)
	num_2.config( height = 20, width = 60)

	num_3 = Button(gui, image = photo_3, command = cmddnum3, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_3.grid(column = 2, row = 3, padx = 3, pady = 3)
	num_3.config( height = 20, width = 60)

	num_4 = Button(gui,image = photo_4, command = cmddnum4, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_4.grid(column = 0, row = 2, padx = 3, pady = 3)
	num_4.config(height = 20, width = 60)

	num_5 = Button(gui,image = photo_5, command = cmddnum5, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_5.grid(column = 1, row = 2, padx = 3, pady = 3)
	num_5.config(height = 20, width = 60)

	num_6 = Button(gui,image = photo_6, command = cmddnum6, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_6.grid(column = 2, row = 2, padx = 3, pady = 3)
	num_6.config(height = 20, width = 60)

	num_7 = Button(gui,image = photo_7, command = cmddnum7, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_7.grid(column = 0, row = 1, padx = 3, pady = 3)
	num_7.config(height = 20, width = 60)

	num_8 = Button(gui,image = photo_8, command = cmddnum8, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_8.grid(column = 1, row = 1, padx = 3, pady = 3)
	num_8.config(height = 20, width = 60)

	num_9 = Button(gui,image = photo_9, command = cmddnum9, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_9.grid(column = 2, row = 1, padx = 3, pady = 3)
	num_9.config(height = 20, width = 60)

	num_0 = Button(gui,image = photo_0, command = cmddnum0, width = 20, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
	num_0.grid(column = 0 ,row = 4, padx = 3, pady = 3, columnspan = 2)
	num_0.config(height = 20, width = 140)

	sign_comma = Button(gui,image = photo_dot, command = cmddsign_dot, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
	sign_comma.grid(column = 2 ,row = 4, padx = 3, pady = 3)
	sign_comma.config(height = 20, width = 60)

	sign_plus = Button(gui, image = photo_plus, command = cmdsign_plus, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
	sign_plus.grid(column = 4 ,row = 3, padx = 3, pady = 3)
	sign_plus.config( height = 20, width = 60)

	sign_minus = Button(gui, image = photo_minus, command = cmdsign_minus, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
	sign_minus.grid(column = 3 ,row = 3, padx = 3, pady = 3)
	sign_minus.config( height = 20, width = 60 )

	sign_multiply = Button(gui, image = photo_multi, command = cmdsign_multilpy, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
	sign_multiply.grid(column = 3 ,row = 2, padx = 3, pady = 3)
	sign_multiply.config( height = 20, width = 60 )

	sign_devide = Button(gui, image = photo_div, command = cmdsign_devide, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
	sign_devide.grid(column = 4 ,row = 2, padx = 3, pady = 3)
	sign_devide.config( height = 20, width = 60 )

	sign_equel = Button(gui, image = photo_equel, command = cmdsign_equel, width = 18, borderwidth = 3,fg = "#1E395B", bg = "#E9F0F8")
	sign_equel.grid(column = 0 ,row = 5, padx = 3, pady = 3, columnspan = 3)
	sign_equel.config(height = 20, width = 220, highlightbackground = "#1E395B")

	sign_clear = Button(gui,image = photo_clr,command = cmdsign_clear,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
	sign_clear.grid(column = 3 ,row = 5, padx = 3, pady = 3)
	sign_clear.config(height = 20, width = 60 )

	sign_row = Button(gui,image = photo_row,command = cmdsign_row,compound = LEFT,width = 7, borderwidth = 3)
	sign_row.grid(column = 4 ,row = 1, padx = 3, pady = 3)
	sign_row.config(height = 20, width = 60 )

	sign_sqrt = Button(gui,image = photo_sqrt,command = cmdsign_sqrt,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
	sign_sqrt.grid(column = 3 ,row = 1, padx = 3, pady = 3)
	sign_sqrt.config(height = 20, width = 60)

	sign_fclear = Button(gui,image = photo_fclr,command = cmdsign_fclear,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
	sign_fclear.grid(column = 4,row = 5, padx = 3, pady = 3)
	sign_fclear.config(height = 20, width = 60)

	qavs_left = Button(gui,image = photo_left,command = cmdqavs_left,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
	qavs_left.grid(column = 3,row = 4, padx = 3, pady = 3)
	qavs_left.config(height = 20, width = 60)

	qavs_right = Button(gui,image = photo_right,command = cmdqavs_right,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
	qavs_right.grid(column = 4,row = 4, padx = 3, pady = 3)
	qavs_right.config(height = 20, width = 60)

# Grid
num_1 = Button(sff_mode, image = photo_1, command = cmdnum1, borderwidth = 3,fg = "#1E395B", bg = '#E9F0F8')
num_1.grid(column = 0, row = 4, padx = 3, pady = 3)
num_1.config( height = 20, width = 50 )

num_2 = Button(sff_mode, image = photo_2, command = cmdnum2, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_2.grid(column = 1, row = 4, padx = 3, pady = 3)
num_2.config( height = 20, width = 50)

num_3 = Button(sff_mode, image = photo_3, command = cmdnum3, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_3.grid(column = 2, row = 4, padx = 3, pady = 3)
num_3.config( height = 20, width = 50)

num_4 = Button(sff_mode,image = photo_4, command = cmdnum4, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_4.grid(column = 0, row = 3, padx = 3, pady = 3)
num_4.config(height = 20, width = 50)

num_5 = Button(sff_mode,image = photo_5, command = cmdnum5, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_5.grid(column = 1, row = 3, padx = 3, pady = 3)
num_5.config(height = 20, width = 50)

num_6 = Button(sff_mode,image = photo_6, command = cmdnum6, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_6.grid(column = 2, row = 3, padx = 3, pady = 3)
num_6.config(height = 20, width = 50)

num_7 = Button(sff_mode,image = photo_7, command = cmdnum7, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_7.grid(column = 0, row = 2, padx = 3, pady = 3)
num_7.config(height = 20, width = 50)

num_8 = Button(sff_mode,image = photo_8, command = cmdnum8, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_8.grid(column = 1, row = 2, padx = 3, pady = 3)
num_8.config(height = 20, width = 50)

num_9 = Button(sff_mode,image = photo_9, command = cmdnum9, width = 7, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_9.grid(column = 2, row = 2, padx = 3, pady = 3)
num_9.config(height = 20, width = 50)

num_0 = Button(sff_mode,image = photo_0, command = cmdnum0, width = 20, borderwidth = 3,    fg = "#1E395B", bg = "#E9F0F8")
num_0.grid(column = 0 ,row = 5, padx = 3, pady = 3, columnspan = 2)
num_0.config(height = 20, width = 120)

sign_comma = Button(sff_mode,image = photo_dot, command = cmdsign_dot, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
sign_comma.grid(column = 2 ,row = 5, padx = 3, pady = 3)
sign_comma.config(height = 20, width = 50)

sign_plus = Button(sff_mode, image = photo_plus, command = cmdsign_plus, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
sign_plus.grid(column = 4 ,row = 4, padx = 3, pady = 3)
sign_plus.config( height = 20, width = 50)

sign_minus = Button(sff_mode, image = photo_minus, command = cmdsign_minus, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
sign_minus.grid(column = 3 ,row = 4, padx = 3, pady = 3)
sign_minus.config( height = 20, width = 50 )

sign_multiply = Button(sff_mode, image = photo_multi, command = cmdsign_multilpy, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
sign_multiply.grid(column = 3 ,row = 3, padx = 3, pady = 3)
sign_multiply.config( height = 20, width = 50 )

sign_devide = Button(sff_mode, image = photo_div, command = cmdsign_devide, width = 7, borderwidth = 3,   fg = "#1E395B", bg = "#E9F0F8")
sign_devide.grid(column = 4 ,row = 3, padx = 3, pady = 3)
sign_devide.config( height = 20, width = 50 )

sign_equel = Button(sff_mode, image = photo_equel, command = cmdsign_equel, width = 18, borderwidth = 3,fg = "#1E395B", bg = "#E9F0F8")
sign_equel.grid(column = 0 ,row = 6, padx = 3, pady = 3, columnspan = 3)
sign_equel.config(height = 20, width = 190, highlightbackground = "#1E395B")

sign_clear = Button(sff_mode,image = photo_clr,command = cmdsign_clear,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
sign_clear.grid(column = 3 ,row = 5, padx = 3, pady = 3)
sign_clear.config(height = 20, width = 50 )

sign_row = Button(sff_mode,image = photo_row,command = cmdsign_row,compound = LEFT,width = 7, borderwidth = 3)
sign_row.grid(column = 4 ,row = 2, padx = 3, pady = 3)
sign_row.config(height = 20, width = 50 )

sign_sqrt = Button(sff_mode,image = photo_sqrt,command = cmdsign_sqrt,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
sign_sqrt.grid(column = 3 ,row = 2, padx = 3, pady = 3)
sign_sqrt.config(height = 20, width = 50)

sign_fclear = Button(sff_mode,image = photo_fclr,command = cmdsign_fclear,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
sign_fclear.grid(column = 4,row = 5, padx = 3, pady = 3)
sign_fclear.config(height = 20, width = 50)

sign_next_page = Button(sff_mode,image = photo_dff,command = cmdnext_page,width = 7, borderwidth = 3,fg = "#1E395B",bg = "#E9F0F8")
sign_next_page.grid(column = 3,row = 6, padx = 3, pady = 3, columnspan = 2)
sign_next_page.config(height = 20, width = 118)

# Bind
root.bind('<Escape>',quit)
root.bind('<Return>',cmdsign_equel)
root.bind('1',cmdnum1)
root.bind('2',cmdnum2)
root.bind('3',cmdnum3)
root.bind('4',cmdnum4)
root.bind('5',cmdnum5)
root.bind('6',cmdnum6)
root.bind('7',cmdnum7)
root.bind('8',cmdnum8)
root.bind('9',cmdnum9)
root.bind('0',cmdnum0)
root.bind('.',cmdsign_dot)
root.bind('+',cmdsign_plus)
root.bind('-',cmdsign_minus)
root.bind('*',cmdsign_multilpy)
root.bind('/',cmdsign_devide)
root.bind("<BackSpace>",cmdsign_clear)
root.bind("<Delete>",cmdsign_fclear)
root.bind("<Control-Key-X>",cmdnext_page)
root.bind("<Control-Key-x>",cmdnext_page)
root.bind("<Control-Key-Z>",cmdback_page)
root.bind("<Control-Key-z>",cmdback_page)

root.mainloop()
