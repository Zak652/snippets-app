import logging

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