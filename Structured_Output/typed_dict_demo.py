from typing import TypedDict        # importing TypedDict

class person(TypedDict):    # specifying data types
    name:str
    age:int

new_person: person = {'name':"Ankit",'age':26}      # making another person that resonates to person class

print(new_person)