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
        return cls.user_list       

  


class Credential:
    
    '''
    class that generates new passwords and saves their information
    '''
    credential_list = []

    def __init__(self,username,email,password):

        self.username = username
        self.email = email
        self.password = password

    def save_credential(self):

        '''
        save_user method saves user into credentials list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        method that deletes saved credentials
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in a email and returns a credential that matches that email.
        
        Args:
            email: email to find 
        Returns:
            Credential of person that matches the email.
            '''
            
        for credential in cls.credential_list:
            if credential.email == email:
                return credential

    @classmethod
    def credential_exists(cls,email):
        '''
        Method that checks if a credential exists from the credential list.

        Args:
            email: email to search if it exists
        Returns:
            Boolean: True or False depending if the credential exists
        '''

        for credential in cls.credential_list:
            if credential.email == email:
                return True
            return False

    @classmethod
    def display_credentials(cls):

         '''
        method that returns class credential_list
         '''
         return cls.credential_list                        



