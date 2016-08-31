import os, sys

class scaner:
	"""docstring for scaner"""
	def __init__(self, os_object):
		self.os = os_object
	# current dir
	current_dir = os.getcwd()
	# pattern to find
	pattern = ".py"
	# list of founded files
	files = []

	def scanFor(self):
		for items in self.os.listdir(self.current_dir):
			if self.pattern in items:
				self.files.append(items)
		return True

	def run(self, pattern):
		self.pattern = pattern
		self.scanFor()
		return self.files

obj = scaner(os)

try:
	sys.argv[1]
except:
	print(obj.run(input("What do we scan for: ")))
else:
	print(obj.run(sys.argv[1]))
finally:
	print("Job is done!")