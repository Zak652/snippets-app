import logging
import argparse

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)


def put (name, snippet):
	"""
	Store a snippet with an associated name

	Return name and the snippet
	"""
	logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
	return name, snippet

def get (name):
	"""
	Returns the Snippet with a given name

	When the snippet is not found, return '404: Snippet not Found'

	Return the snippet
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	return ""

def modify (name, snippet):
	"""
	Search for the snippet associated with the name

	Make changes to or replace the snippet

	Show changes made vs original snippet

	Return the snippet
	"""
	logging.error("FIXME: Unimplemented - modify({!r}, {!r})".format(name, snippet))
	return name, snippet

def remove (name):
	"""
	Search for the name of the snippet

	Delete the name and the associated snippet

	Return confirmation message
	"""
	logging.error("FIXME: Unimplemented - remove({!r})".format(name))
	return ""

def main():
	"""Main function"""
	logging.info("Constructing parser")
	parser = argparse.ArgumentParser(description = "Store and retrive snippets of text")
	argument = parser.parse_args()

if __name__=="__main__":
	main()