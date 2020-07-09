# Periodic table tool

### This program will let you search the periodic table

# Domumentation 

## package periodictool
Given an input (atomic name (string), atomic symbol (string), atomic mass (float) or atomic number(integer)), the program returns information about that specific element. 
## Examples:
<pre><code>def example_1():
    H = ['Hydrogen', 'H', 1, 1.0080]    
    print(periodictool.name(H[0]))
    print(periodictool.symbol(H[1]))
    print(periodictool.number(H[2]))
    print(periodictool.mass(H[3]))
</code></pre>

<pre><code>Output:
    ['H', '1', '1.0080']
    ['Hydrogen', '1', '1.0080']
    ['Hydrogen', 'H', '1.0080']
    ['Hydrogen', 'H', '1']
</code></pre>

<pre><code>def example_2():
    H = ['Hydrogen', 'H', 1, 1.0080]    
    for i in range(3):
        periodictool.search(H[i])
</code></pre>

<pre><code>Output:
        Atomic symbol: H
        Atomic number: 1
        Atomic mass: 1.0080

        Atomic name: Hydrogen
        Atomic number: 1
        Atomic mass: 1.0080

        Atomic name: Hydrogen
        Atomic symbol: H
        Atomic mass: 1.0080
</code></pre>

## Functions:
### name(str(s)):
Finds information about element by atomic name (string must start with capital letter).
Returns atomic mass, atomic number and atomic symbol in a list.
Average timecomplexity: O(1)
### mass(float(x)):
Finds information about element by atomic mass.
Returns name of element, atomic number and atomic symbol in a list.
Average timecomplexity: O(1)
### symbol(str(s)):
Finds information about element by atomic symbol (string must start with capital letter).
Returns name of element, atomic mass and atomic number in a list.
Average timecomplexity: O(1)
### number(int(n)):
Finds information about element by atomic number.
Returns name of element, atomic mass and atomic symbol in a list.
Average timecomplexity: O(1)
### search(d):
Prints out information about the element specified by the input (string must start with capital letter).
Argument has to be of type integer, float or string.
Average timecomplexity: O(1)

# Roadmap

* The API of this library is frozen.
* Version numbers adhere to semantic versioning.

The only accepted reason to modify the API of this package
is to handle issues that can't be resolved in any other
reasonable way.









