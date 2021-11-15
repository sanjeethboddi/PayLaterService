class User:
    def __init__(self, username, email, credit_limit):
        self.__username = username
        self.__email = email
        self.__credit_limit = credit_limit
    
    def get_email(self):
        return self.__email
    
    def get_credit_limit(self):
        return self.__credit_limit

    def get_username(self):
        return self.__username
    
    def __str__(self):
        return self.__username+"("+str(self.__credit_limit)+")"