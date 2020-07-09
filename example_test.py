import periodictool

H = ['Hydrogen', 'H', 1, 1.0080]

def example_1():
    print(periodictool.name(H[0]))
    print(periodictool.symbol(H[1]))
    print(periodictool.number(H[2]))
    print(periodictool.mass(H[3]))
    #Output: ['H', '1', '1.0080']
    #        ['Hydrogen', '1', '1.0080']
    #        ['Hydrogen', 'H', '1.0080']
    #        ['Hydrogen', 'H', '1']
def exmple_2():
    for i in range(3):
        periodictool.search(H[i])
    #Output:
    #    Atomic symbol: H
    #    Atomic number: 1
    #    Atomic mass: 1.0080

    #    Atomic name: Hydrogen
    #    Atomic number: 1
    #    Atomic mass: 1.0080

    #    Atomic name: Hydrogen
    #    Atomic symbol: H
    #    Atomic mass: 1.0080
