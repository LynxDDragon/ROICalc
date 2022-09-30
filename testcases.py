import unittest
from ROI import User_info

class TestCal(unittest.TestCase):

    def test_name(self):
        test_name = User_info(' ','joseph',' ',' ',' ')
        self.assertIn('joseph',test_name.name )

    def test_curr(self):
        test_curr = User_info('joseph',' ',' ',' ',' ')
        self.assertIn('joseph',test_curr.curr_user )

    def test_property(self):
        test_property = User_info(' ','','mansion',' ',' ')
        self.assertIn('mansion',test_property.property )

    def test_investment(self):
        test_investment = User_info(' ',' ',' ',' ', '1000')
        self.assertIn('1000',test_investment.investment )

    

if __name__ == '__main__':
    unittest.main()