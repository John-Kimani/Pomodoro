from . import db


class User:
    '''
    Class to define user
    '''
    def __init__(self,id,username,firstName,lastName,email,password):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password

            
        