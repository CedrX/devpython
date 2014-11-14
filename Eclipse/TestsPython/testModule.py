from xml.dom.minidom import Document
from xml.dom.minidom import parse
from sgoaconfig.dataSource import DataSourceManager
from sgoaconfig.properties import PropertyManager
from sgoaconfig.sgoavalues import sgoaValue


#dom1 = parse('/applis/sgoa/home/etc/conf/fdpConfPostgre.xml')


#builderXML = DataSourceManager(dom1)
#domElmt = builderXML.getDataSourceByName("commun")

valueTest = sgoaValue("urlBase","jdbc:oracle:thin:@jumbo:10001:fdoc")
dom1 = Document()
print valueTest.toDomElement()
dom1.appendChild(valueTest.toDomElement())
print dom1.toxml("utf-8")

valueTest2 = sgoaValue(None,"cedric.tintanet@inist.fr")
dom2 = Document()
dom2.appendChild(valueTest2.toDomElement())
print dom2.toxml("utf-8")


valueTest3 = sgoaValue(None,None)
dom3 = Document()
domNode = dom3.createElement("values")
domNode.setAttribute("name","urlBase")
domNode.setAttribute("value","org.postgresql.driver")
valueTest3.domElementToValue(domNode)
print "Name: %s Valeur: %s" %(valueTest3.getName(),valueTest3.getValue())










