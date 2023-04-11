# Prologue: 
# Name : Numa Noorin
# 
# Description: This program asks user's full name and description. Prints the name and users description accorind to their input.
# and then converts the input into html format. 


# Date: 7/2/2022

from unittest import result
import codecs
import webbrowser

name = input("Enter your full name: ")
print("Hello", name + "!")

describe = input("Enter a sentence that describes you: ")
print(describe)

# to open/create a new html file in the write mode
f = open('Unit6NoorinN.html', 'w')

# the html code which will go in the file Unit6NoorinN.html
html_template = """<html>

<body>
 
<h2>Name</h2>

<p>Describe</p>

</body>
</html>
"""

# open html file 
webbrowser.open('Unit6NoorinN.html')

# writing the code into the file
f.write(html_template)

# close the file
f.close()

#viewing html files below code creates a codecs.streamreaderwriter object.
file = codecs.open("Unit6NoorinN.html", 'r', "utf-8")

#using the method below to view the html 
print(file.read())



