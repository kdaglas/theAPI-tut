"""  Object classes for the customer model """

all_customers = []

class Customer():

    """ constructor to initialise all params """

    def __init__(self, customerId, username, emailaddress, contact, password):
        self.customerId = customerId
        self.username = username
        self.emailaddress = emailaddress
        self.contact = contact
        self.password = password


    def register_customer(self):

        # method that gets the order class and makes it a dictionary

        customer = {
            'customerId' : self.customerId,
            'username' : self.username,
            'emailaddress' : self.emailaddress,
            'contact' : self.contact,
            'password' : self.password
        }

        all_customers.append(customer)
        return customer

    def get_all_customers(self):

        # method that gets all the customers who have registered

        if all_customers:
            return all_customers
        return {'There is an error': 'No customers Found'}

    @classmethod
    def login(cls, username, password):

        # method that gets all the customers who have registered

        for customer in all_customers:
            if customer.get('username') == username and customer.get('password'):
                return customer
        return {'There is an error': 'No customers Found'}
        
