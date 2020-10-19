# A Well Tested Second Order Polynomial in Python


## What is a 2nd order polynomial?

[learn more](https://en.wikipedia.org/wiki/Quadratic_function)

## Running the test suite
install the requirements.

```bash
pip install -r requirements.txt
```

run the test suite.
```bash
python tests.py
```

## Examining the Class
Hop in to a python shell to explore the `SecondOrderPolynomial`.

Factoring a polynomial with our `SecondOrderPolynomial` Class.
```python
>>> from app import SecondOrderPolynomial
>>> p = SecondOrderPolynomial(a=-1, b=7, c=-12)
>>> p.factor()
'(1x + -3)(-1x + 4)'
```

Unfactoring a polynomial with our `SecondOrderPolynomial` Class.
```python
>>> q = SecondOrderPolynomial(m=2, n=3, j=1, k=2)
>>> q.unfactor()
'6x + 10x + 2x'
```

Graphing a polynomial with our `SecondOrderPolynomial` Class.
```python
>>> q.display_graph()
```

There are a few interesting code snippets I want to draw you attention to.

```
  def set_defaults(self, *args):
    for arg in args:
        if getattr(self, arg) == None:
            setattr(self, arg, default_values[arg])
```

It is called with string parameters.

```
self.set_defaults('m', 'n', 'j', 'k')
```

Our `set_defaults()` method loops through the arguments and uses `getattr()` and
`setattr()` to get and set property names based on the string it is passed. I learned
why these methods are so useful during this project.
