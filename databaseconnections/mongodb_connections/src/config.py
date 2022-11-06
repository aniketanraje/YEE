from urllib import parse 

password = input("Enter the password:")

connection_string  = ("mongodb+srv://sherlockbhosale:" +  parse.quote(password) + "@sherlockbhosale.vu1l9mg.mongodb.net/?retryWrites=true&w=majority")
