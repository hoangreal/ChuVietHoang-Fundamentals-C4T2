def accept_login(users,username,password):
	# We will use statement "in" in order to check whether the key exists in dict or not
	if username in users and users[username]==password:
		return True
	else:
		return False

users = {
"user1" : "password1",
"user2" : "password2",
"user3" : "password3"
}
username = input("Enter your username: ")
password = input("Enter your password: ")
if accept_login(users, username, password)==True :
	print("login successful!")
else :
	print("login failed...")

