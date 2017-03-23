class Mtb:
    def __init__(self):
        ''' Constructor for this class. '''
        self.brands = ['Giant', 'Trek', 'Santa Cruz']

    def printbrands(self):
        print('Printing brands of the Mtb class')
        for member in self.brands:
            print('\t%s ' % brand)