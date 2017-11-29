'''
https://www.codewars.com/kata/triangular-range

Triangular numbers count the number of objects that can form an equilateral triangle. The nth triangular number forms an equilateral triangle with n dots on each side (including the vertices).
Here is a graphic example for the triangular numbers of 1 to 5:
```
n=1: triangular number: 1
*

n=2: triangular number: 3
 *
* *

n=3: triangular number: 6
  *
 * *
* * *

n=4: triangular number: 10
    *
   * *
  * * *
 * * * *
 
 n=5: triangular number: 15
      *
     * *
    * * *
   * * * *
  * * * * *
```

Your task is to implement a function ```triangular_range(start, stop)``` that <b>returns a dictionary of all numbers as keys and the belonging triangular numbers as values, where the triangular number is in the range start, stop (including start and stop)</b>.
For example, ```triangular_range(1, 3)``` should return ```{1: 1, 2: 3}``` and ```triangular_range(5, 16)``` should return ```{3: 6, 4: 10, 5: 15}```.
'''
triangular_number = lambda n: 1 if n == 1 else n + triangular_number(n-1)

def gen(start, stop):
    n = 1
    while triangular_number(n) <= start:
        n += 1
    while triangular_number(n) <= stop:
        yield (n, triangular_number(n))
        n += 1

triangular_range = lambda start, stop: dict([n for n in gen(start, stop)])


if __name__ == '__main__':
    print(triangular_range(1, 3))
    print(triangular_range(5, 16))
