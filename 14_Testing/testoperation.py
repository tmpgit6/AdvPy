import unittest 
import operation 

class TestOperation(unittest.TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)
        
        self.checker = operation.Operation() 
        self.a1 = 10
        self.b1 = 20 

        self.a2 = "Apfel"
        self.b2 = True

    def test_add(self):
        # Pos Cases
        result = self.checker.add(self.a1, self.b1 )
        self.assertEqual(result, 30)
        
        # Neg Cases
        with self.assertRaises(ValueError) as context:
            result = self.checker.add(self.a2, self.b2 )
        
        self.assertEqual(str(context.exception), "Value should be int or float")


if __name__ == "__main__":
    unittest.main()