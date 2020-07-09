import unittest
import periodictool

def test():
    #Testing mass()
    assert periodictool.mass(1.0080) == ['Hydrogen', 'H', '1']
    assert periodictool.mass(246.0) == ['Californium', 'Cf', '98']

    #Testing number()
    assert periodictool.number(1) == ['Hydrogen', 'H', '1.0080']
    assert periodictool.number(98) == ['Californium', 'Cf', '246']

    #Testing name()
    assert periodictool.name('Hydrogen') == ['H', '1', '1.0080']
    assert periodictool.name('Californium') == ['Cf', '98','246']

    #Testing synmbol()
    assert periodictool.symbol('H') == ['Hydrogen', '1', '1.0080']
    assert periodictool.symbol('Cf') == ['Californium', '98', '246']

class test_edgecases(unittest.TestCase):
    #Testing edgecases (if the function raises errors when it's supposed to)
    def edgetest(self):
        #Testes edgecases for mass()
        with self.assertRaises(TypeError):
            periodictool.mass('1.0080')
        with self.assertRaises(ValueError):
            periodictool.mass(42.0)
        #Testes edgecases for number()
        with self.assertRaises(TypeError):
            periodictool.number(1.0)
        with self.assertRaises(ValueError):
            periodictool.number(1984)
        #Testes edgecases for name()
        with self.assertRaises(TypeError):
            periodictool.name(1.0)
        with self.assertRaises(ValueError):
            periodictool.name('1984')
        #Testes edgecases for symbol()
        with self.assertRaises(TypeError):
            periodictool.symbol(1.0)
        with self.assertRaises(ValueError):
            periodictool.symbol('1984')
        #Testes edgecases for search()
        with self.assertRaises(ValueError):
            periodictool.search('Clementinium')
            periodictool.search('Ö')
            periodictool.search(42.0)
            periodictool.search(1984)
