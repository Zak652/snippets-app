import logging
import argparse
import psycopg2

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

logging.debug("Connect to PostgreSQL")
connection = psycopg2.connect (database="snippets")
logging.debug("Database connection established")


def put (name, snippet):
	"""
	Store a snippet with an associated name

	Return name and the snippet
	"""
	logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
	cursor = connection.cursor()
	command = "insert into snippets values (%s, %s)"
	cursor.execute(command, (name, snippet))
	connection.commit()
	logging.debug("snippet Stored successfully.")
	return name, snippet

def get (name):
	"""
	Returns the Snippet with a given name

	When the snippet is not found, return '404: Snippet not Found'

	Return the snippet
	"""
	logging.error("FIXME: Unimplemented - get({!r})".format(name))
	cursor = connection.cursor()
	command = "select message from snippets where keyword=%s"
	cursor.execute(command, (name,))
	message = cursor.fetchone()
	# print (message)
	logging.debug("Your snippet has been retrieved.")
	return message

def modify (name, snippet):
	"""
	Search for the snippet associated with the name

	Make changes to or replace the snippet

	Show changes made vs original snippet

	Return the snippet
	"""
	logging.error("FIXME: Unimplemented - modify({!r}, {!r})".format(name, snippet))
	cursor = connection.cursor()
	command = "update snippets set message =%s where keyword=%s"
	cursor.execute(command, (snippet, name))
	connection.commit()
	logging.debug("Your snippet has been updated")
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

	subparsers = parser.add_subparsers(dest="command", help="Available command")

	#Subparser for the put command
	logging.debug("Constructing put subparser")
	put_parser = subparsers.add_parser("put", help="Store a snippet")
	put_parser.add_argument("name", help="Name of the snippet")
	put_parser.add_argument("snippet", help="Snippet text")

	#Subparser for the get command
	logging.debug("Constructing get subparser")
	get_parser = subparsers.add_parser("get", help="Retrive a snippet of a given name")
	get_parser.add_argument("name", help="Name of the snippet")

	#Subparser for the modify command
	logging.debug("Constructing modify subparser")
	modify_parser = subparsers.add_parser("modify", help="Update a snippet of a given name")
	put_parser.add_argument("name", help="Name of the snippet")
	put_parser.add_argument("snippet", help="Snippet")


	arguments = parser.parse_args()

	#Convert parsed arguments from Mamespace to dictionary
	arguments = vars(arguments)
	command = arguments.pop("command")

	if command == "put":
		name, snippet = put(**arguments)
		print("Stored {!r} as {!r}".format(snippet, name))

	elif command == "get":
		snippet = get(**arguments)
		print("Retrieved snippet: {!r}".format(snippet))

	elif command == "modify":
		name, snippet = modify(**arguments)
		print("Updated {!r} message to {!r}".format(name, snippet))

if __name__=="__main__":
	main()