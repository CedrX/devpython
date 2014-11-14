import sgoaconfig.sgoavalues as svalues


valueTest = svalues.sgoaValue("urlBase","jdbc:oracle:thin:@jumbo:10001:fdoc")
print "Name: %s Valeur: %s" %(valueTest.getName(),valueTest.getValue())

