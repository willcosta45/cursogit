#mitupla=("enzo",16,4,2000)
#nombre, dia, mes, agno=mitupla
#print(nombre)
#print(dia)
#print(mes)
#print(agno)

#name = "Ada Lovelace"
#print(name.upper())
#print(name.lower())

#print ("\t\nhello world","\t\nhello chicos","\t\nvamos cenar")
#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles[0].title())

#bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#message = "My first bicycle was a " + bicycles[0].title() + "."
#print(message)


#friends= ['Carlos', 'Isis', 'Fauzer', 'Berta', 'guillermo', 'Pablo']
#friends.insert(6,'ana')
#friends.insert(0,'conchi')
#friends.append('pepe')
#invitacion= 'hoy cena en casa ' + friends[5].title() + "." 
#print("Here is the original list:")
#print(friends)

#print("\nHere is the sorted list:")
#print(sorted(friends))

#print("\nHere is the original list again:")
#print(friends)

#print(len(friends))



#partido= ['willian','Enzo','junior','kostas']
#for escalados in partido:
 #print(escalados.title() + ',listo para jugar')
 #print('vamos ganar el partido,' + escalados.title() + ".\n")
#print('muchas gracias chicos,jugamos muy bien')

#motorcycles = ['honda', 'yamaha', 'suzuki']
#first_owned = motorcycles.pop(0)
#print('The first motorcycle I owned was a ' + first_owned.title() + '.')

#number=list(range(2,20,2))
#print(number)
#squares = []

#for value in range(1,11):
 #    square = value**2
  #   squares.append(square)
#print(squares)

#players = ['charles', 'martina', 'michael', 'florence', 'eli']
#print("Here are the first three players on my team:")
#for player in players[:3]:
  #  print(player.title())

#my_foods = ['pizza', 'falafel', 'carrot cake']

#friend_foods = my_foods[:]
#my_foods.append('conoli')
#friend_foods.append('ice cream')
#print("My favorite foods are:")
#print(my_foods)
#print("\nMy friend's favorite foods are:")
#print(friend_foods)



#my_pizza =['queso','jamon','tomate frito','rucula']
#friends_pizza=my_pizza[:]
#friends_pizza.append('parmesano')
#my_pizza.append('aceitunas')
#print('mi pizza es la mejor')
#print(my_pizza)
#print('nueva ingridientes')
#print(friends_pizza)
#print(len(my_pizza))

#dimensions = (200, 50)
#print("Original dimensions:")
#for dimension in dimensions:
 #print(dimension)

#dimensions = (400, 100)
#print("Modified dimensions:")
#for dimension in dimensions:
 #print(dimension)

#car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
#print(car == 'audi')

#pizza='peperoni'
#print("Si la pizza=='peperoni'voy comer mucho")
#print(pizza=='peperoni')
#print("Y si la pizza=='anchoa'no me acerco a ella!!")
#print(pizza=='anchoa')

#age= 12
#if age < 4:
    #print('sera admitido gratis')
#elif age < 18:
     # print('Your adminsion costa is 5$')
#else:
    #print('Your adminsion costa is 10$')


#age = 12
#if age < 4:
 # price = 0
#elif age < 18:
 # price = 5
#elif age < 65:
  #price = 10
#else:
 # price = 5
#print("Your admission cost is $" + str(price) + ".")



#alien_colors = ['green','yellow' or 'red']
#if 'green'in alien_colors:
  #print('win 5 points')
#if 'yellow' in alien_colors:
  #print('win 10 points')
#if 'red' in alien_colors:
 # print('20 points')


#available_toppings = ['mushrooms', 'olives', 'green peppers',
#'pepperoni', 'pineapple', 'extra cheese']
#requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#for requested_topping in requested_toppings:
    #if requested_topping in available_toppings:  
       # print("Adding " + requested_topping + ".")
    #else:
      #print("Sorry, we don't have " + requested_topping + ".")
#print("\nFinished making your pizza!")

#user =['Fauzer','Ana','Admin','Carlos','Isis']
#if 'Admin' in user:
  #print('would you like to see a status report?')
#else:
 # print('Hello, thank you for loging again')
  
#DICIONARIO
#alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
#if alien_0['speed'] == 'slow':
 #   x_increment = 1
#elif alien_0['speed'] == 'medium':
 #   x_increment = 2
#else:
# This must be a fast alien.
 #   x_increment = 3
# The new position is the old position plus the increment.
#alien_0['x_position'] = alien_0['x_position'] + x_increment
#print("New x-position: " + str(alien_0['x_position']))



#favorite_languages = {
#'jen': 'python',
#'sarah': 'c',
#'edward': 'ruby',
#'phil': 'python',
#}
#for languages in set(favorite_languages.values()):
#  print(languages.title())

#Make an empty list for storing aliens.
#aliens = []
# Make 30 green aliens.
#for alien_number in range(333):
 # new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
 # aliens.append(new_alien)
# Show the first 5 aliens:
#for alien in aliens[:5]:
 # print(alien)
#print("...")
  # Show how many aliens have been created.
#print("Total number of aliens: " + str(len(aliens)))

#Input and while loops

#number = input('quero saber si el numero es even or odd:')
#number=int(number)
#if number %2 == 0:
 # print('\nEl numero ' +str(number) + 'es even')
#else:
 # print('\nEl numero ' +str(number) + 'es odd')

#cuenta_numbers = 1
#while cuenta_numbers <= 10:
   #print(cuenta_numbers)
  # cuenta_numbers+=1

#prompt = '\nDime algo, y yo te repito de vuelta:'
#prompt += '\nClicar en enter para "salir" del programa.'
#message=''
#while message != "salir":
   # message=input(prompt)
   # print(message)


def describe_pet(tipo_animal,nombre_animal):
  print('\n Yo tengo un ' + tipo_animal + '.')
  print('Mi ' + tipo_animal + ' se llama  ' + nombre_animal.title()+ ',')
describe_pet(tipo_animal='gato', nombre_animal='Tobias')
#describe_pet('perro', 'tobias')
#describe_pet('gato', 'firulas')


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()
muscian = get_formatted_name('jimi', 'hendrix')
print(muscian)


def build_person(first_name, last_name, age=''):
  """Return a dictionary of information about a person."""
  person = {'first': first_name, 'last': last_name}
  if age:
    person['age'] = age
  return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)





def build_profile(first, last, **user_info):
  profile = {}
  profile['first_name']=first
  profile['last_name']=last
  for key, value in user_info.items():
      profile[key]=value
  return profile
user_profile = build_profile('albert','einstein', location = 'princeton', field = 'physics')
print(user_profile)



def name_city(nombre_ciudad , nombre_pais):
  print('mi ciudad es ' + nombre_ciudad + '.')
  print('Mi pais es ' + nombre_pais + '.')
ciudad = name_city('Madrid', 'Espanha')
print(ciudad)


def make_album(artista,titulo):
  cantante={'Arlindo': artista, 'meu ligar':titulo}
  return(cantante)
musica = make_album('favela ', 'verao ')
print(musica)


def greet_users(names):

  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = "Hello, " + name.title() + "!"
    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)




class Dog():

   """A simple attempt to model a dog."""
   def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age
   def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(self.name.title() + " is now sitting.")
   def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(self.name.title() + " rolled over!")

