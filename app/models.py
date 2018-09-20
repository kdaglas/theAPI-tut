"""  Object classes for the User """


class Customer():

    """ constructor to initialise all params """

    def __init__(self, customerId, username, emailaddress, contact, password):
        self.customerId = customerId
        self.username = username
        self.emailaddress = emailaddress
        self.contact = contact
        self.password = password


class Order():

    """ constructor to initialise all params """

    def __init__(self, orderId, today, customerId, food, thetype, price, quantity, status):
        self.orderId = orderId
        self.customerId = customerId
        self.today = today
        self.food = food
        self.thetype = thetype
        self.price = price
        self.quantity = quantity
        self.status = status
        
