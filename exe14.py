from sys import argv
script,user_name = argv
prompt = ">"
print ("hi %s i am %s")%(script,user_name)
print ("do like me? ")
likes = raw_input(prompt)
print("where do you live?")
lives = raw_input(prompt)
print('what kind of computer do you use?')
computer = raw_input(prompt)
print("so %r you say %r about liking me,you live in %r and you use a %r computer")%(likes,lives,computer)
