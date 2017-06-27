import unittest
from tests.home.test_login import TestLoginPage
from tests.home.test_my_trips import TestMyTrips

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLoginPage)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestMyTrips)

smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
