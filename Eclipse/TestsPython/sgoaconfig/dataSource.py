'''
Created on 5 mars 2014

@author: tintanet
'''
#from xml.dom.minidom import Document
#from xml.dom.minidom import parse


class DataSourceManager(object):
    '''
    Create XML conf for sgoa project
    '''

    
    _domDocument = None
    
    def __init__(self, domDocument):
        '''
        Constructor with xml.dom.minidom.Document to manage
        '''
        self._domDocument = domDocument
    
    def getDataSourceByName(self,stringName):
        tabDataSourceElement = self._domDocument.getElementsByTagName("data-source")
        elementToReturn = None
        for elementDataSource in tabDataSourceElement:
            if elementDataSource.hasAttribute("key"):
                if elementDataSource.getAttribute("key") == stringName:
                    elementToReturn = elementDataSource
                    break
                
        return elementToReturn
    
    