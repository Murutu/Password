class User:

    '''
    class that generates the users first name,last_name and password
    '''
    user_list = []
 
    def __init__(self,first_name,last_name,email,password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def save_user(self):

        '''
        save_user method saves user into users list
        '''
    User.user_list.append(self)

    @classmethod
    def display_user(cls):

        '''
        method that returns class user_list
        '''        

  


class Credential:
    
    '''
    class that generates new passwords and saves their information
    '''
    credential_list = []

    def __init__(self,username,email,password):

        self.username = username
        self.email = email
        self.password = password
