# function defintion 

def function():
    pass

# function call
function()   


def main():

    # information about Joel 
    my_favourite_things = {
        'Full_name': 'Joel Bahati',
        'Student_ID': 10276278,
        'Pizza_toppings': [
            'Bacon',
            'Pineapples',
            'Chicken'
        ],
        'Movies': [
            {
                'Title': 'Limitless',
                'Genre': 'Thriller/Action'
            },
            {
                'Title': 'Snowden',
                'Genre': 'Thriller/Drama'
            }
        ]

    

    }

    # Adding another movie to the data structure
    new_movie = {'Title': 'The Matrix', 'Genre': 'Sci-fi/Action'}
    my_favourite_things['Movies'].append(new_movie)

# Adding pizza toppings with another function 
def adding_toppings(my_favourite_things, more_toppings):

    more_toppings = ('mushrooms', 'olives', 'peppers')
    list(more_toppings)
    my_favourite_things['Pizza_toppings'].append(more_toppings)
    
    # sorting items in alphabetical order
    my_favourite_things['Pizza_toppings'].list.sort()
    
    # converting items to lower case 
    lower_case_toppings = my_favourite_things['Pizza_toppings']
    for i in range(len(lower_case_toppings)):
        lower_case_toppings[i].lower()

# function call 
main()

# printing student name and ID 
def student_name_ID(my_favourite_things):
    full_name = my_favourite_things.get('Full_name')
    first_name = list(my_favourite_things.keys())[0] 
    ID = my_favourite_things.get('Student_ID')

    print ('My name is',full_name,',but you can call me Sir', first_name,'.')

    print ('My student ID is', ID,'.' )

main()

def favourite_toppings(my_favourite_things): 
    for t in my_favourite_things['Pizza toppings']:
        print (f"- {t}")

print()        

# printing comma seperated values
def genre_seperated_values(my_favourite_things):
    genre = my_favourite_things['Movies'].get('Genre')

    print('I like to watch', genre, sep=',' 'movies.')

main() 



def movie_seperated_values(my_favourite_things): 
    movies = my_favourite_things['Movies'].get('Titles')

    print('Some of my favourite movie titles are', movies, sep=',')

main()      

    



    
    
       







