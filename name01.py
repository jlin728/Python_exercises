students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

print "Students"
for i in range(len(students)):
    
	print (i+1), (students[i]["first_name"]), (students[i]["last_name"]), len(students[i]["first_name"]) + len(students[i]["last_name"])

#for i in students:
#	print i["first_name"] + " " + i["last_name"]
