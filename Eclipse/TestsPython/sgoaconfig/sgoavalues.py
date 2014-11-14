# -*- coding: utf-8 -*-

from xml.dom.minidom import Document
#from xml.dom.minidom import Element
from xml.dom.minidom import Node
 
'''
Created on 5 mars 2014

@author: tintanet
'''

class sgoaValue(object):
    '''
    An object representation of <value name="toto" value="titi"/>
    '''

    _name = None
    _value = None
    
    def __init__(self, stringName,stringValue):
        '''
        Constructor
        '''
        if stringName != None:
            self._name = stringName
        if stringValue != None:
            self._value = stringValue
        
    def setName(self,newName):
        self._name = newName
  
    def getName(self):
        return self._name
    
    def setValue(self,newValue):
        self._value = newValue
        
    def getValue(self):
        return self._value
    
    def toDomElement(self):
        '''
            Transform sgoaValue Object to Node xml.dom.minidom
        '''
        dom1 = Document()
        domNode = dom1.createElement("values")
        if self.getName() != None:
            domNode.setAttribute("name",self.getName())
            domNode.setAttribute("value",self.getValue())
        elif self.getValue() !=None:
            domText = dom1.createTextNode(self.getValue())
            domNode.appendChild(domText)
        else:
            #TODO : lever une exception
            #pas d'appel de cette méthode tant que au moins une des deux dm
            #de sgoaValue n'est pas initialisée
            return None
            
        return domNode
    
    def domElementToValue(self,domElmt):
        '''
        Transform Node to sgoaValue object
        '''
        if domElmt.nodeName == "values":
            if domElmt.hasAttributes():
                nameAttribute = domElmt.getAttribute("name")
                if nameAttribute != '':
                    self.setName(nameAttribute)
                    #TODO: ajouter exception si la chaine vide renvoyée
                valueAttribute = domElmt.getAttribute("value")
                if valueAttribute != '':
                    self.setValue(valueAttribute)
                    #TODO ajouter exception si chaine vide renvoyée
            else:
                if domElmt.hasChildNodes():
                    listeChilds = domElmt.childNodes
                    #TODO: tester la longueur de liste et lever une exception si 
                    # taille de la liste > 1
                    child = listeChilds.pop(0)
                    if child.nodeType == Node.TEXT_NODE:
                        self.setValue(child.nodeValue)
                    #TODO : lever une exception si le noeud n'est pas du type TEXT_NODE
                        
                    
                
                
    