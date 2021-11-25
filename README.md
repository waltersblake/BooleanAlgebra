# BooleanAlgebra
## A Python class with overloaded operators to mimic functionality from mathematical boolean algebra
### The operators used are:
1. The **+** binary operator returns the maximum of the two operands
2. The __*__ binary operator returns the minimum of the two operands
3. The **~** unary operator returns the complement of the operand
4. The **==** equality operator, works pretty much as expected by comparing the two values held by the object instances
## Examples
### Basic
```python
from bool_alg import BoolAlg
x = BoolAlg(0)
y = BoolAlg(1)
result = x + y
print(result.value) # 1
```
### Commutative Axiom
```python
from bool_alg import BoolAlg
x = BoolAlg(0)
y = BoolAlg(1)
print(x + y == y + x) # True
print(x * y == y * x) # True
```
### Associative Axiom
```python
from bool_alg import BoolAlg
x = BoolAlg(0)
y = BoolAlg(1)
z = BoolAlg(1)
print((x + y) + z == x + (y + z)) # True
print((x * y) * z == x * (y * z)) # True
```
### de Morgan's Law
```python
from bool_alg import BoolAlg
x = BoolAlg(0)
y = BoolAlg(1)
print(~(x + y) == ~x * ~y) # True
print(~(x * y) == ~x + ~y) # True
```
