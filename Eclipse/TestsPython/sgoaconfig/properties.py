'''
Created on 5 mars 2014

@author: tintanet
'''

class PropertyManager(object):
    '''
    classdocs
    '''
    _propertyName = None
    

    def __init__(self, propertyName):
        '''
        Constructor
        '''
        self._propertyName = propertyName
        
    #def __init__(self, domElmt):
    #    self._domElmt = domElmt
        
    def getPropertyByName(self,dom_dataSourceElement,stringName):
        tabProperties = None
        propertyToReturn = None
        if dom_dataSourceElement.hasChildNodes():
            tabProperties = dom_dataSourceElement.getElementsByTagName("set-property")
            for prop in tabProperties:
                if prop.hasAttributes(stringName):
                    propertyToReturn = prop
                    break
            
        return propertyToReturn    
            
            
            
            
        
        
        