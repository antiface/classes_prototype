import unittest
import pdb

from classes_prototype import Order, Overnight_shipping, Overnight_Gift


class ClassesPrototypeTests(unittest.TestCase):
  
    def test_classes_proto_shipping(self):
        pdb.set_trace()
        abc_order = Overnight_Gift('abc')
        xyz_order = Overnight_shipping('xyz')
        self.assertEqual(abc_order.shipping, xyz_order.shipping)
        
    def test_classes_proto_packaging(self):
        bcd_order = Order('bcd')
        yza_order = Overnight_shipping('yza')
        self.assertEqual(bcd_order.product_packaging, yza_order.product_packaging)
        
    #this test passes when it should fail. A dollar value of 13 doesn't raise an Exception.   
    def test_classes_proto_exception(self):        
        self.assertRaises(Exception, Order.dispatch_email, 'Jackie', 'xxx', '13')
        
    
        
        