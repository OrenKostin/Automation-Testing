import unittest
from tests.home.test_login import TestLogin
from tests.lego.test_lego_star_wars import TestLegoStarWars

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestLegoStarWars)

build_verification_test = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(build_verification_test)
