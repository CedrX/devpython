import xml.etree.ElementTree as ET

elmtTreebase = ET.parse('/applis/sgoa/home/etc/conf/fdpConf.xml')

rootTree = elmtTreebase.find('./')
print type(rootTree)

dataSourceCommunTree = rootTree.find('.//data-source[@key="commun"]')
property_bdd_connexion = dataSourceCommunTree.find('./set-property[@name="bdd_connexion"]')
value_urlbase = property_bdd_connexion.find('./values[@name="urlBase"]')
value_urlbase.set('value','jdbc:postgresql://localhost:54320/sgoa')

elmtTreebase.write("/home/tintanet/Programmation/resultConf.xml",
                   xml_declaration=True,
                   encoding="utf-8",
                   method='xml')


