#ура! мой первый unittest и он работает

import Anket

def test_first():
   
    assert(Anket.first('http://suninjuly.github.io/registration1.html'),"Congratulations! You have successfully registered!")

def test_second():        
    assert(Anket.first('http://suninjuly.github.io/registration2.html'),"Congratulations! You have successfully registered!")
        

if __name__=='__mane__':
    unittest.main()
