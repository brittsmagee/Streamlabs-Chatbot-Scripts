import clr
import sys
import json
import os
import ctypes
import codecs

ScriptName = "Steal Minigame"
Website = "http://www.github.com/Bare7a/Streamlabs-Chatbot-Scripts"
Description = "Steal Minigame for Streamlabs Bot"
Creator = "Bare7a"
Version = "1.2.8"

configFile = "config.json"
settings = {}

def ScriptToggled(state):
	return

def Init():
	global settings

	path = os.path.dirname(__file__)
	try:
		with codecs.open(os.path.join(path, configFile), encoding='utf-8-sig', mode='r') as file:
			settings = json.load(file, encoding='utf-8-sig')
      
def Execute(data):
	if data.IsChatMessage() and data.GetParam(0).lower()
               outputMessage = ""
    if 
				"$victim" = Parent.GetDisplayName("$targetid")
      return

def ReloadSettings(jsonData):
	Init()
	return

def OpenReadMe():
	location = os.path.join(os.path.dirname(__file__), "README.txt")
	os.startfile(location)
	return

def Tick():
	return
