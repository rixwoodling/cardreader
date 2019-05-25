#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def help():
	print("The Card Reader")
	print("")

set1 = ['2','3','4','5']
set2 = ['10','J','Q','K','A']
suit = ['♠','♣','♥','♦']
card = set1+set2
random.shuffle(card)
random.shuffle(suit)

print("♠ ♣ ♥ THE GREAT AZBARIX ♣ ♥ ♦ ")
print("♦ presents his famous trick ♠")
print("♠ ♣ ♥  The Card Reader  ♣ ♥ ♦")

print("\b")

spc = "      "

print("▌▓▓▓|"),
print("press return to pick")
raw_input(spc + "a card from this deck...")

print("\b")

if card[0] == '10':
	print("▌%s%s|" % (card[0],suit[0])),
else:
	print("▌ %s%s|" % (card[0],suit[0])),
raw_input("remember this card.")


raw_input(spc + "show it to everyone")
raw_input(spc + "but dont show it to me.")
raw_input(spc + "put it back into the deck.")

print("\b")

print("▌▓▓▓|"),
raw_input("good. now what i am going to do...")
raw_input(spc + "is shuffle this deck.")
raw_input(spc + "keep thinking of your card.")
raw_input(spc + "what you are about to see")
raw_input(spc + "is real magic.")
raw_input(spc + "i will now reach into your mind")
raw_input(spc + "and select your card. ready?")

print("\b")

card[1]
if card[1] == '10':
	print("▌%s%s|" % (card[1],suit[1])),
else:
	print("▌ %s%s|" % (card[1],suit[1])),
a = 1
while a == 1:
	x = raw_input("is this your card? y/n: ")
	if x == "y":
		print("\b")
		print("vavava-VOOM!")
		print("I am the Great Azbarix!")
		print("kiss my hand.")
		a = 0
	elif x == "n":
		print("\b")
		print(spc + "YOU LYING SCUMBAG!")
		print(spc + "I am the Great Azbarix!")
		a = 0
	else:
		print("...")

