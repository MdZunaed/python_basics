import re

txt = "The rain in Spain"
x = re.findall("[a-m]", txt)
print(x)


# findall	- Returns a list containing all matches
# search	- Returns a Match object if there is a match anywhere in the string
# split	- Returns a list where the string has been split at each match
# sub	- Replaces one or many matches with a string


# Character	    Description	        Example	
# []	A set of characters	        "[a-m]"	
# \	    Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	    Any character (except newline character)	"he..o"	
# ^	    Starts with	                "^hello"	
# $    	Ends with	                "planet$"	
# *	    Zero or more occurrences	"he.*o"	
# +	    One or more occurrences	    "he.+o"	
# ?	    Zero or one occurrences	    "he.?o"	
# {}	Exactly the specified number of occurrences	"he.{2}o"	
# |	    Either or	                "falls|stays"	
# ()	Capture and group	 