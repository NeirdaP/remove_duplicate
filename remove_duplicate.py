import os
import sys

def main(directory, searched_string):
	file_list = os.listdir(directory)
	removable_files = create_removable_files_list(file_list, searched_string)
	delete_files(directory, removable_files)	

def create_removable_files_list(file_list, searched_string):
	filtered_list=[]

	for file_name in file_list:
		if searched_string in file_name:
			filtered_list.append(file_name)

	return filtered_list

def delete_files(directory, removable_files):
	for file_name in removable_files:
			removable_file_path = os.path.join(directory, file_name)
			print("About to remove :", removable_file_path)
			os.remove(removable_file_path)
		
	print("Removed.")


if __name__ == '__main__':
	#/Users/adripatriz/Documents/Photo/2023-08-08
	#-to-remove

	ERROR_MESSAGE = """Error : Two Arguments are needed. The first one should be an
	absolute path to the directory containing the files to remove.
	The second one should be a string to identify the files to remove."""

	if len(sys.argv) < 3:
		print(ERROR_MESSAGE)
		exit()
	
	main(sys.argv[1], sys.argv[2])


