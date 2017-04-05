from jnpr.junos import Device

mydeviceslist=["172.16.249.60"]
for item in mydeviceslist:
    dev=Device(host=item, user="tiaddemo", password="OpenConfig")
    dev.open()
    dev.close()
    print ("the device "+ dev.facts["hostname"]+ " is an " + dev.facts['model'] + " running " + dev.facts["version"]+"\n")
