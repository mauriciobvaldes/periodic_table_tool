def name(s):
    #Input: Name of element (string)
    """Finds information about element by atomic name.
    Returns atomic mass, atomic number and atomic symbol in a list.
    Average timecomplexity: O(1)"""

    data = {}

    with open('elemdata.txt', 'r') as file:
        for line in file:
            key, *values = line.strip().split()
            data[key] = values
    if type(s) is str:
        output=data.get(s)
        if output:
            return(output)
        else:
            raise ValueError('Element does not exist')
    else:
        raise TypeError('Input is not type string')


def mass(x):
    #Input: Atomic mass (float)
    """Finds information about element by atomic mass.
    Returns name of element, atomic number and atomic symbol in a list.
    Average timecomplexity: O(1)"""

    data = {}

    with open('elemdata.txt', 'r') as file:
        for line in file:
            *values,key= line.strip().split()
            data[float(key)] = values
    if type(x) is float:
        output=data.get(x)
        if output:
            return(output)
        else:
            raise ValueError('Element does not eixist')
    else:
        raise TypeError('Input is not type float')


def symbol(s):
    #Input: Atomic symbol (string)
    """Finds information about element by atomic symbol.
    Returns name of element, atomic mass and atomic number in a list.
    Average timecomplexity: O(1)"""

    data = {}

    with open('elemdata.txt', 'r') as file:
        for line in file:
            value1,key,value2,value3 = line.strip().split()
            data[key] = [value1,value2,value3]
    if type(s) is str:
        output=data.get(s)
        if output:
            return(output)
        else:
            raise ValueError('fel namn')
    else:
        raise TypeError('Input is not type string')


def number(n):
    #Input: Number of element (integer)
    """Finds information about element by atomic number, returns information in a list.
    Returns name of element, atomic mass and atomic symbol in a list.
    Average timecomplexity: O(1)"""

    data={}

    with open('elemdata.txt', 'r') as file:
        for line in file:
            value1,value2,key,value3=line.strip().split()
            data[int(key)] = [value1,value2,value3]
    if type(n) is int:
        output=data.get(n)
        if output:
            return(output)
        else:
            raise ValueError('Element does not exist')
    else:
        raise TypeError('Input is not type integer')


def search(d):
    #Input: atomic name (string), atomic symbol (string), atomic mass (float) or atomic number (integer)
    """Prints out information about the element specified by the input.
    Argument has to be of type integer, float or string.
    Average timecomplexity: O(1)"""
    
    if type(d)==str:
        if len(d)>2:
            print('Atomic symbol: ' + name(d)[0])
            print('Atomic number: ' + name(d)[1])
            print('Atomic mass: ' + name(d)[2] + ' u')
        else:
            print('Atomic name: ' + symbol(d)[0])
            print('Atomic number: ' + symbol(d)[1])
            print('Atomic mass: ' + symbol(d)[2] + ' u')
    elif type(d)==int:
        print('Atomic name: ' + number(d)[0])
        print('Atomic symbol: ' + number(d)[1])
        print('Atomic mass: ' + number(d)[2])
    elif type(d)==float:
        print('Atomic name: ' + mass(d)[0])
        print('Atomic symbol: ' + mass(d)[1])
        print('Atomic number: ' + mass(d)[2] + ' u')
    else:
        raise TypeError('Input is not type string, integer or float')
