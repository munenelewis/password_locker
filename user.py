class User:
    """
    class that generates instances of user
    """
 
    def __init__(self,first_name, last_name,password):
  
        """
        helps in defining properties of a method
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    user_list = []#Empty contact list


    def save_user(self):
        """
        save_user saves contact object into contact_list"""

        User.user_list.append(self)