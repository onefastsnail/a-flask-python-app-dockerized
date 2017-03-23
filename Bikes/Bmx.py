class Bmx:
    def __init__(self):
        ''' Constructor for this class. '''
        self.brands = ['BSD', 'Fly Bikes', 'Fit bike co']

    def printbrands(self):
        print('Printing brands of the Bmx class')
        for member in self.brands:
            print('\t%s ' % brand)