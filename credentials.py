class Credantials :
    '''class of the credentials'''
    credential_list = []
    def __init__(self, account_name,account_password):
        self.account_name = account_name
        self.account_password = account_password

    def save_credentals(self):
        """save credentials saves credentials in the credential list"""

        Credantials.credential_list.append(self)