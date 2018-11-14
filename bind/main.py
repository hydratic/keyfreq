def main(path_to_log, path_to_keys):
	# check to ensure that the key monitor is running
	err = 1
	res = get_status()
	if res == true:
		err = 0
	if res == false:
		print("keyfreq is not running!")
		
	# load keybinds
	keys = open(path_to_keys)
	
	# read through keybinds
	loop = 1
	while loop == 1:
		# TODO
	
	# load log
	log = open(path_to_log)
