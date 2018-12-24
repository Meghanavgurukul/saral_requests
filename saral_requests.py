import requests
# importing requests module 
URL = "http://saral.navgurukul.org/api"
# assingning the api of saral  into global variable named URL
def get(url):
	request=requests.get(url)
	return request.json()
	
# making  the request and  getting response 
courses_url= URL+"/courses"
courses_response = get(courses_url)
# adding endpoint to there url 
print ("-------------------------Welcome to SARAL------------------------")
courses_id_list= list()
# taking a empty list so that all  the couses id get into it 
index=0

while index<len(courses_response["availableCourses"]):
	course = courses_response["availableCourses"][index]
	course_name = course["name"]
	course_id= course["id"]
	courses_id_list.append(course_id)
	print(str(index)+"-",course_name)
# using while loop form taking out name and id index wise from available courses 	
	index+=1
# using api here -for printing the entire course  list from saral  
print("-------------------------------------------------------------------------------------------------------")	
def user_choose():

	user_input = int(input("choose the courses from saral which you want to learn "))
	user_choice  = courses_id_list[user_input]
	return user_choice

# taking  the input from the user so that they  can choose courses  which tey want  to learn 

courses = user_choose()
exercises_url = URL+"/courses/"+str(courses)+"/exercises"
response = get(exercises_url)

# adding endpoint to the url to get the exercise form saral 
sluglist= list()

def exercises_url():
	index=0

# accordinng to the user choice printing  the exercise which they want to learn 

	while index<len(response["data"]):
		exercise=response["data"][index]
		exercise_id=exercise["parentExerciseId"]

		
		if exercise_id == None:
			exercise_name=exercise["name"]
			exercise_slug=exercise["slug"]
			sluglist.append(exercise_slug)
			print(str(index)+"-",exercise_name)


		elif exercise_id != None:
			exercise_name=exercise["name"]
			exercise_slug=exercise["slug"]
			sluglist.append(exercise_slug)

			print(str(index)+"-",exercise_name)

			index1=0
			while index1<len(exercise["childExercises"]):
				child_exercise_name=exercise["childExercises"][index1]["name"]
				child_exercise_slug=exercise["childExercises"][index1]["slug"]
				sluglist.append(child_exercise_slug)

				print("\n"+str(index1)+"-",child_exercise_name)
				index1+=1

		index+=1
exercises_url()		


slug_url= URL +"/courses/"+str(courses)+"/exercise/getBySlug"

def get_slug(url,params):
	request= requests.get(url, params=params)
	return request.json()
	


slug_response=get_slug(slug_url,{'slug': sluglist[0]})

print (slug_response['content'])

# after showing the exercise to the user here printing the content of the exercise which they choice 
def slug_content():
	index3=0
	while True:
		choose_exercise= str(input("enter 'n' to go to next exercise or 'p' to go to previous exercise or to exit enter any key :- "))
		if choose_exercise == "n" and index3 < len(sluglist)-1:
			slug_response=get_slug(slug_url,{'slug': sluglist[index3+1]})
			print (slug_response['content'])
		
			index3+=1


		elif choose_exercise == "p" and index3 >0:
		
			slug_response= get_slug(slug_url,{'slug': sluglist[index3-1]})
			print (slug_response['content'])
			index3-=1



		elif choose_exercise=="n" and index3==len(sluglist)-1:
			slug_response= get_slug(slug_url,{'slug': sluglist[index3]})
			print (slug_response['content'])
			print ("NO MORE NEXT EXERCISE")


		elif choose_exercise=="p" and index3== 0:
			slug_response= get_slug(slug_url,{'slug': sluglist[index3]})
			print (slug_response['content'])
			print ("NO MORE PREVIOUS EXERCISE")

# if the user enter any key then the loop while break and else condition will be printed 
		else:
			print("---------------------You choosed exit.------------------------------------")
	
			break
slug_content()
