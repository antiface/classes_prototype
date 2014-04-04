
#shipping orders in an ecommerce store

import pdb


class Order(object):
    pdb.set_trace()
    product_packaging = 'standard'
    shipping = 'us_mail'
    
    def __init__(self, order):
        self.order = order     
    
    def address_label(self, address):
        return address
        
    def dispatch_email(self, customer_name, order_number, order_value):            
        if int(order_value) <= 0:
            raise Exception('There is an error with the order value! It should be more than $0!')                            
        email_message = 'Hi ' + customer_name + '. Your order number ' + order_number + ' for which you have been charged $' + order_value + ' has been dispatched today.'
        return email_message
    
class Overnight_shipping(Order):
    shipping = 'overnight' 
    
    #what would I use init for here?    
    
    def email_fedex(self, address, order_number):
        print "There is an outgoing package " + order_number + " for you to pick up and deliver to" + address
        
                      
class Overnight_Gift(Overnight_shipping):
    product_packaging = 'gift wrap'
    
    #what would I use init for here? 
    
    #ask Sam about how to raise an exception for a TypeError when the argument required is not inputted. 
    def gift_note(self, message):                  
        return message            
    

saturday_order = Order('hat')
sunday_order = Overnight_Gift('scarf')

print saturday_order.shipping

print sunday_order.product_packaging
print sunday_order.shipping


print sunday_order.address_label('100 avenue')
print sunday_order.dispatch_email('Jackie', 'xxx', '05')

print sunday_order.gift_note('Happy Birthday, Andy')

 


    