#ура! мой первый unittest и он работает
import unittest
import Anket

class test_Anket(unittest.TestCase):
    def test_first(self):
   
        self.assertEqual(Anket.first('http://suninjuly.github.io/registration1.html'),"Congratulations! You have successfully registered!")
    def test_second(self):        
        self.assertNotEqual(Anket.first('http://suninjuly.github.io/registration2.html'),"Congratulations! You have successfully registered!")
        

if __name__=='__mane__':
    unittest.main()
