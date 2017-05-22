# !/usr/bin/python
# -*-coding: utf-8-*-


diccionario = {"Acto 1":"Nueva Tristan",
				"Acto 2":"Campamento Secreto",
				"Acto 3":"Baluarte de la fortaleza Bastion",
				"Acto 4":"Jardines de la Esperanza",
				"Acto 5":"Westmarch"}
print diccionario
print diccionario["Acto 3"]
print diccionario.get("Acto 5")
print diccionario.pop("Acto 1")
