# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import re

configchoices = '/home/tintanet/Programmation/kconfig/.config'
filetemplate = '/applis/sgoa/home/etc/conf/fdpConf.xml'
fileoutput = '/home/tintanet/Programmation/resultConf.xml'

#translations = { 'DS': { 'balise':'data-source',
#                          'qualificatifAttr': 'key',
#                        },
#                  'PROP': {'balise':'set-property',
#                           'qualificatifAttr':'name',
#                           'valeurAttr':'value'},
#                  'VAL': {'balise':'values',
#                          'qualificatifAttr':'name', 
#                          'valeurAttr':'value'}
#                }

translations = {   'DS'   : 'data-source',
                   'PROP' : 'set-property',
                   'VAL'  : 'values'
                   }

descbalise = {'data-source'  : {'qualificatifAttr' : 'key'},
              'set-property' : {'qualificatifAttr': 'name','valeurAttr': 'value'},
              'values'       : {'qualificatifAttr':'name','valeurAttr':'value'}
              }

def setSgoaElementAttribute(ElmtXml,nameAttr,value):
    '''
        change la valeur de l'attribut dans l'élement ElmtXml de type Element (ElementTree)
    '''
    ElmtXml.set(nameAttr,value)
    return ElmtXml

def getbyXpath(rootTree,Xpath):
    return rootTree.find(Xpath)


def transformVarToXpath(stringName):
        xpathString='.//'
        tabindex = []
        tabchaine = []
        for clefs in translations.keys():
            value = stringName.find(clefs)
            if value != -1:
                tabindex.append(value)
        tabindex.sort()
        for i in range(0,len(tabindex)):
            if i == len(tabindex)-1:
                tabchaine.append(stringName[tabindex[i]:])
            else:
                tabchaine.append(stringName[tabindex[i]:tabindex[i+1]-1])
        for chaine in tabchaine:
            for clefs in translations.keys():
                if clefs in chaine:
                    #xpathString += translations[clefs]['balise']+'[@' \
                    # + translations[clefs]['qualificatifAttr'] + '="' \
                    # + chaine.replace(clefs,'') + '"]/'
                     
                    xpathString += translations[clefs] + '[@' \
                        + descbalise[translations[clefs]]['qualificatifAttr'] + '="' \
                        + chaine.replace(clefs,'') + '"]/'
                           
        #print tabchaine
        return xpathString[:-1]

# main

elmtTreebase = ET.parse(filetemplate)
rootTree = elmtTreebase.find('./')
elmtToChange = None
with open(configchoices, 'r') as configchoice:
    for line in configchoice:
        if re.match('CONFIG_', line):
            locationVar = (line.split('=')[0]).replace('CONFIG_','')
            valueToSet = (line.split('=')[1]).replace('"','').replace('\n','')
            xpathToAccess = transformVarToXpath(locationVar)
            #print "elmtToChange = getbyXpath(rootTree,%s)" %(xpathToAccess)
            elmtToChange = getbyXpath(rootTree,xpathToAccess)
            if elmtToChange != None:
                for clef in descbalise:
                    #print 'if re.match("%s","%s")' %(clef,xpathToAccess)
                    if re.search(clef,xpathToAccess.split('/').pop()):
                       # print "attrToChange = descbalise[%s][valeurAttr]" %clef
                        attrToChange = descbalise[clef]['valeurAttr']
                        #print "elmtToChange = setSgoaElementAttribute(elmtToChange,%s,%s)" %(attrToChange,valueToSet)
                        elmtToChange = setSgoaElementAttribute(elmtToChange,attrToChange,valueToSet)

elmtTreebase.write(fileoutput,
                   xml_declaration=True,
                   encoding="utf-8",
                   method='xml')
                   
#TODO : Ajouter une sortie console précisant que le fichier de configuration a été généré            
    
           
            
                    