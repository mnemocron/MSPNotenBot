#!/usr/bin/python
#_*_ coding: utf-8 _*_

'''
@file 	msp-check.py
@author github.com/mnemocron
@date 	2018-07-09
'''

try:
	import sys
	import os
	import optparse
	import json
	from file_found import callback_new_file
except Exception as e:
	print >> sys.stderr, 'Error importing modules'
	print >> sys.stderr, e
	sys.exit(1)

# ===== ARGUMENTS =====
parser = optparse.OptionParser('program-name')
parser.add_option('-i', '--input-dir', 	dest='indir', 	type='string', 	help='directory to scan for new files')
parser.add_option('-s', '--save-file', 	dest='save', 	type='string', 	help='location of the save file with known files')
parser.add_option('-r', '--rules', 		dest='rules', 	type='string', 	help='location of the rules file (json)')

(opts, args) = parser.parse_args()

# ===== READ FILE AS LIST OF LINES =====
def load_prev_list(path):
	file_list = []
	with open(path, 'r') as file:
		for line in file:
			file_list.append(line.replace('\n', ''))
	return file_list

# ===== APPEND TO FILE =====
def append_cur_list(path, entries):
	with open(path, 'a') as file:
		for entry in entries:
			file.write(entry + '\n')

# ===== LOAD JSON TO OBJECT =====
def load_json_rules(path):
	with open(path, 'r') as conf_file:
		json_conf = json.loads(conf_file.read())
	return json_conf

# ===== MAIN =====
def main():
	if ( opts.indir is None or opts.save is None or opts.rules is None):
		parser.print_help() 
		exit(0)
	known_files = load_prev_list(opts.save)
	new_files = []
	rules = load_json_rules(opts.rules)
	for root, directories, filenames in os.walk(opts.indir):
		for filename in filenames:
			# onefile = os.path.join(root,filename)
			if(not filename in known_files):
				# print 'new file'
				callback_new_file(filename, rules)     # handle newly found file in external function
				new_files.append(filename)      # remember new files
			# else:
			#	print(filename + ' is already a known file')
	append_cur_list(opts.save, new_files)       # write new files to file

# ================
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt, e:
		print('Aborted by KeyboardInterrupt')
		exit(0)
