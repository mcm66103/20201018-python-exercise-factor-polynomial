import matplotlib.pyplot as plt


class SecondOrderPolynomial():
    '''
    Class to represent a second order polynomial.

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

    def __init__(self, **kwargs):
        self.a = kwargs.get('a', None)
        self.b = kwargs.get('b', None)
        self.c = kwargs.get('c', None)
        self.m = kwargs.get('m', None)
        self.n = kwargs.get('n', None)
        self.j = kwargs.get('j', None)
        self.k = kwargs.get('k', None)

        # Check each property to make to enforce correct data types.
        for item in [
            self.a,
            self.b,
            self.c,
            self.m,
            self.n,
            self.j,
            self.k
        ]:
            if isinstance(item, int) or item == None:
                pass
            else:
                raise ValueError("You may only configure your polynomial with integers")

        # Set default values.
        if self.m or self.n or self.j or self.k:
            self.set_defaults('m', 'n', 'j', 'k')
            self.unfactor()

        if self.a or self.b or self.c:
            self.set_defaults('a', 'b', 'c')
            self.factor()

    def is_factored(self):
        '''
        check type of properties to determine if polynomial is in factored state.
        '''

        if (
            isinstance(self.m, int) &
            isinstance(self.n, int)
        ):
            return True
        else:
            return False

    def is_unfactored(self):
        '''
        check type of properties to determine if polynomial is in unfactored state.
        '''

        if (
            isinstance(self.a, int) &
            isinstance(self.b, int) &
            isinstance(self.c, int)
        ):
            return True
        else:
            return False

    def unfactor(self):
        '''
        look at the factored polynomial and expand it

        (mx + j)(nx + k) -> ax^2 + bx + c
        '''
        if self.a and self.b and self.c:
            pass

        else:
            self.a = self.m * self.n
            self.b = self.m * self.k + self.n * self.k
            self.c = self.j * self.k

        return f"{self.a}x + {self.b}x + {self.c}x"

    def factor(self):
        '''
        look at the unfactored polynomial and factor it

        (mx + j)(nx + k) -> ax^2 + bx + c
        '''
        if self.m and self.j and self.n and self.k:
            pass
        else:
            factors_of_a = []
            factors_of_c = []

            for factor in get_factors(self.a):
                factors_of_a.append(factor)

            for factor in get_factors(self.c):
                factors_of_c.append(factor)

            for factor_of_a in factors_of_a:
                factor_pair_of_a = int(self.a / factor_of_a)
                for factor_of_c in factors_of_c:
                    factor_pair_of_c = int(self.c / factor_of_c)

                    if factor_of_a * factor_of_c + factor_pair_of_a * factor_pair_of_c == self.b:
                        self.m = factor_of_a
                        self.n = factor_pair_of_a
                        self.j = factor_pair_of_c
                        self.k = factor_of_c

        return f"({self.m}x + {self.j})({self.n}x + {self.k})"

    def set_defaults(self, *args):
        for arg in args:
            if getattr(self, arg) == None:
                setattr(self, arg, default_values[arg])

    def evaluate(self, x):
        a = self.a * ( x ** 2 )
        b = self.b * x
        c = self.c
        return a + b + c

    def display_graph(self):
        x_range = []
        y_range = []

        for n in range(-10, 11):
            x_range.append(n)

        for x in x_range:
            y_range.append(self.evaluate(x))

        plt.plot(x_range, y_range)
        plt.show()


default_values = {
    'a': 1,
    'b': 1,
    'c': 0,
    'm': 1,
    'n': 1,
    'j': 0,
    'k': 0
}


def get_factors(x):
    '''
    Input:

        x: int

    return a List of factors of x.
    '''
    factors = []

    for n in range(1, x+1):
        if x % n == 0:
            factors.append(n)
    return factors
