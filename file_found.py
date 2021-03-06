#!/usr/bin/python
#_*_ coding: utf-8 _*_

'''
@file 	file_found.py
@author github.com/mnemocron
@date 	2018-07-09
'''

try:
	import sys
	import os
except Exception as e:
	print >> sys.stderr, 'Error importing modules'
	print >> sys.stderr, e
	sys.exit(1)

def callback_new_file(path, rules):
	try:
		modul = path.split('_')[0]
		klasse = path.split('_')[1]
		for rule in rules:
			if (rule['modul'].lower() in modul.lower()):
				# matching Klasse
				if ( rule['klasse'].lower() in path.lower() or 'alle' in path.lower() ):
					print('file: ' + path + ' matches the rule: \"' + rule['modul'] + '\" / \"' + rule['klasse'] + '\"')
					callback_send_file(path, rule)

	except Exception, e:
		print ('oops! ' + path)
		print (e)


def callback_send_file(path, rule):

	message = str('Neue MSP Noten hochgeladen:\n'
	+ 'Klasse : ' + rule['klasse'] + '\n'
	+ 'Modul : ' + rule['modul'] + '\n'
	+ 'Datei : ' + path)
	
	message = message.replace('"', '\\"').encode('utf-8')

	print message
	os.system('telegram-bot -u \"' + rule['telegram'] +  '\"" -t \"' + message + '\"')
	
	if('YOUR NAME' in rule['telegram']):
		os.system('echo -e \"Subject: Neue MSP Noten hochgeladen\n' + message + '\n\nLiebe Gruess\nRasPi von Simon\" | ssmtp somebody@recipent.com')
		

