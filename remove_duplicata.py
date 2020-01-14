import os
import sys

def main(argv=sys.argv):
	directory = argv[1]
	print("directory:", directory)
	for filename in os.listdir(directory):
		print("filename : ", filename)
		if "-2" in filename:
			print("join : ",os.path.join(directory, filename))
			os.remove(os.path.join(directory, filename))

if __name__ == '__main__':
	main()