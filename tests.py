import unittest
from app import SecondOrderPolynomial

'''
    SecondOrderPolynomial class represents a second order polynomial.

    Inputs:

        ...for unfactored polynomials:
            ex. ax^2 + bx + c

            a: integer coefficient
            b: integer coefficient
            c: integer y constant

        ...factored polynomials:
            ex. (mx+j)(nx+k)

            m: integer coefficient
            n: integer coefficient
            j: integer constant
            k integer constant
'''

class TestSecondOrderPolynomial(unittest.TestCase):
    '''
    Test the SecondOrderPolynomial behaves as expected when creating, formatting,
    and calculating other properties.
    '''
    def __init__(self, *args, **kwargs):
        super(TestSecondOrderPolynomial, self).__init__(*args, **kwargs)
        self.factored_polynomial = SecondOrderPolynomial(j=1, k=1)
        self.unfactored_polynomial = SecondOrderPolynomial(a=1, b=4, c=4)

    def test_polynomial_does_not_accept_string_keys(self):
        try:
            invalid_polynomial = SecondOrderPolynomial(a='invalid_string')
            self.fail("This polynomial is not supposed to accept string for keys")

        except ValueError as e:
            self.assertTrue(isinstance(e, ValueError))

    def test_polynomial_does_not_accept_object_keys(self):
        try:
            invalid_polynomial = SecondOrderPolynomial(a={'key': 'value'})
            self.fail("This polynomial is not supposed to accept objects for keys")

        except ValueError as e:
            self.assertTrue(isinstance(e, ValueError))

    def test_factored_polynomial_is_factored(self):
        self.assertTrue(self.factored_polynomial.is_factored())

    def test_unfactored_polynomial_is_unfactored(self):
        self.assertTrue(self.unfactored_polynomial.is_unfactored())

    def test_factored_polynomial_unfactors_itself_during_init(self):
        self.assertEqual(self.factored_polynomial.unfactor(), '1x + 2x + 1x')

    def test_unfctored_polynomial_factors_itself_during_init(self):
        self.assertEqual(self.unfactored_polynomial.factor(), '(1x + 2)(1x + 2)')

    def test_graph_factored_polynomial(self):
        self.factored_polynomial.display_graph()
        graph_did_display = input("Did th graph appear? (y/n)")
        if graph_did_display in ['y', 'Y']:
            self.assertTrue(True)
        else:
            self.fail('the graph was supposed to appear.')

if __name__ == '__main__':
    unittest.main()
