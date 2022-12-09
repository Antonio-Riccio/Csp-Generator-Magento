# Python
import argparse
import os

def createCsp(args):
    print(args)

    if (not os.path.exists('etc')):
        os.mkdir('etc')

    #csp_whitelist.xml
    if (args.fileLog=="default"):
        csp_whitelistVarFile = '''<?xml version="1.0"?>
<csp_whitelist xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Csp/etc/csp_whitelist.xsd">
    <policies>
        <policy id="script-src">
            <values>
                <value id="addthis.com" type="host">*.addthis.com</value>
                <value id="ajaxgoogleapis" type="host">*.googleapis.com</value>
                <value id="cloudflare" type="host">*.cloudflare.com</value>
                <value id="fontawesome" type="host">*.fontawesome.com</value>
                <value id="google" type="host">*.google.com</value>
                <value id="google-analytics" type="host">*.google-analytics.com</value>
                <value id="googletagmanager.com" type="host">googletagmanager.com</value>
                <value id="graph-facebook" type="host">graph.facebook.com</value>
                <value id="gstatic" type="host">*.gstatic.com</value>
                <value id="addthis.moatads.com" type="host">*.moatads.com</value>
                <value id="trustpilot" type="host">*.trustpilot.com</value>
                <value id="vimeo" type="host">*.vimeo.com</value>
                <value id="widgets-pinterest" type="host">widgets.pinterest.com</value>
            </values>
        </policy>
        <policy id="style-src">
            <values>
                <value id="cloudflare" type="host">*.cloudflare.com</value>
                <value id="fontawesome" type="host">*.fontawesome.com</value>
                <value id="googleapis" type="host">*.googleapis.com</value>
                <value id="gstatic" type="host">*.gstatic.com</value>
                <value id="twitter.com" type="host">*.twitter.com</value>
            </values>
        </policy>
        <policy id="img-src">
            <values>
                <value id="cloudflare" type="host">*.cloudflare.com</value>
                <value id="data" type="host">data:</value>
                <value id="google-analytics" type="host">*.google-analytics.com</value>
                <value id="paypal" type="host">*.paypal.com</value>
                <value id="twitter.com" type="host">*.twitter.com</value>
                <value id="vimeocdn" type="host">*.vimeocdn.com</value>
            </values>
        </policy>
        <policy id="connect-src">
            <values>
                <value id="cloudflare" type="host">*.cloudflare.com</value>
                <value id="paypal" type="host">*.paypal.com</value>
                <value id="twitter.com" type="host">*.twitter.com</value>
            </values>
        </policy>
        <policy id="font-src">
            <values>
                <value id="cloudflare" type="host">*.cloudflare.com</value>
                <value id="fontawesome" type="host">*.fontawesome.com</value>
                <value id="fontawesomecdn" type="host">*.bootstrapcdn.com</value>
                <value id="googleapis" type="host">*.googleapis.com</value>
                <value id="gstatic" type="host">*.gstatic.com</value>
                <value id="twitter.com" type="host">*.twitter.com</value>
            </values>
        </policy>
        <policy id="frame-src">
            <values>
                <value id="addthis.com" type="host">*.addthis.com</value>
                <value id="google.com" type="host">*.google.com</value>
                <value id="trustpilot" type="host">*.trustpilot.com</value>
                <value id="twitter.com" type="host">*.twitter.com</value>
                <value id="vimeo" type="host">*.vimeo.com</value>
            </values>
        </policy>
    </policies>
</csp_whitelist>
'''

        f = open("etc/csp_whitelist.xml", "w")
        f.write(csp_whitelistVarFile)
        f.close()
    else:
        initCsp_Whitelist = '''<?xml version="1.0"?>
<csp_whitelist xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Csp/etc/csp_whitelist.xsd">
    <policies>
'''
    
        policyScriptStart = '''        <policy id="script-src">
            <values>
'''
        policyStyleStart = '''        <policy id="style-src">
            <values>
'''
        policyImgStart = '''        <policy id="img-src">
            <values>
'''
        policyConnectStart = '''        <policy id="connect-src">
            <values>
'''
        policyFontStart = '''        <policy id="font-src">
            <values>
'''
        policyFrameStart = '''        <policy id="frame-src">
            <values>
'''
        policyStop = '''            </values>
        </policy>
'''
        endCsp_Whitelist = '''    </policies>
</csp_whitelist>
'''
        
        defaultSrc = []
        baseUrl = []
        childSrc = []
        connectSrc = []
        fontSrc = []
        formAction = []	
        frameAncestors = []
        imgSrc = []
        manifestSrc = []
        mediaSrc = []
        objectSrc = []
        scriptSrc = []
        styleSrc = []

        f = open(args.fileLog,"r")
        lines = f.readlines()

        for line in lines:
            if ('[Report Only]' in line):
                http=0
                exit = False
                while exit == False:
                    http=http+1
                    if (line[http]=='h'):
                        if (
                            line[http+1] == 't' and 
                            line[http+2] == 't' and 
                            line[http+3] == 'p' and 
                            line[http+4] == 's' 
                        ):
                            exit = True
                
                end=http + 4
                exit = False
                while exit == False:
                    end=end+1
                    if  (
                        line[end]=='c'     and 
                        line[end+1] == 'o' and 
                        line[end+2] == 'm' 
                        ):
                        end = end + 3
                        exit = True
                    elif(line[end]=='i' and line[end+1] == 't'):
                        end = end + 2
                        exit = True

                if("Refused to load the script" in line):
                    scriptSrc.append(line[http:end])
                elif("Refused to load the stylesheet" in line):
                    styleSrc.append(line[http:end])
                elif("Refused to load the font" in line):
                    fontSrc.append(line[http:end])
                elif("Refused to frame" in line):
                    frameAncestors.append(line[http:end])
                elif("Refused to connect" in line):
                    connectSrc.append(line[http:end])
                elif("Refused to load the image" in line):
                    imgSrc.append(line[http:end])


        f = open("etc/csp_whitelist.xml", "w")
        f.write(initCsp_Whitelist)

        idHost = 0

        if (scriptSrc!=[]):
            f.write(policyScriptStart)
            for host in scriptSrc:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)


        if (styleSrc!=[]):
            f.write(policyStyleStart)
            for host in styleSrc:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)

        
        if (fontSrc!=[]):
            f.write(policyFontStart)
            for host in fontSrc:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)


        if (frameAncestors!=[]):
            f.write(policyFrameStart)
            for host in frameAncestors:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)


        if (connectSrc!=[]):
            f.write(policyConnectStart)
            for host in connectSrc:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)


        if (imgSrc!=[]):
            f.write(policyImgStart)
            for host in imgSrc:
                f.write("                <value id="+str(idHost)+" type='host'>"+host+"</value>\n")
                idHost = idHost +1
            f.write(policyStop)

        f.write(endCsp_Whitelist)

        f.close()

    #config.xml
    moduleVarFile = '''<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:module:Magento_Store:etc/config.xsd">
    <default>
        <csp>
            <policies>
                <storefront>
                    <frame-ancestors>
                        <inline>'''+str(args.trt)+'''</inline>
                    </frame-ancestors>
                </storefront>
                <admin>
                    <frame-ancestors>
                        <inline>'''+str(args.tra)   +'''</inline>
                    </frame-ancestors>
                </admin>
            </policies>
        </csp>
    </default>
</config>
'''

    f = open("etc/config.xml", "w")
    f.write(moduleVarFile)
    f.close()


    #module.xml
    moduleVarFile = '''<config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="urn:magento:framework:Module/etc/module.xsd">
    <module name="'''+ args.nameModule + '''" setup_version="'''+args.version+'''"/>
</config>
'''

    f = open("etc/module.xml", "w")
    f.write(moduleVarFile)
    f.close()


    #registration.php
    registrationVarFile = '''<?php
use Magento\Framework\Component\ComponentRegistrar;
ComponentRegistrar::register(ComponentRegistrar::MODULE, ' '''+args.nameModule+''' ', __DIR__);
'''

    f = open("registration.php", "w")
    f.write(registrationVarFile)
    f.close()


    #composer.json
    composerVarFile = '''{
  "name": "csp/module-csp",
  "version": "'''+args.version+'''",
  "description": "This module handle CSP policies",
  "type": "magento2-module",
  "require": {
    "../../../../vendor/magento/framework": "*",
    "../../../../vendor/magento/module-csp": "100.3.*"
  },
  "license": [
    "Proprietary"
  ],
  "autoload": {
    "files": [
      "registration.php"
    ],
    "psr-4": {
      "Ev\\CSP\\": ""
    }
  }
}
'''

    f = open("composer.json", "w")
    f.write(composerVarFile)
    f.close()

    return 0


if __name__ == "__main__":
    exitVar = False

    print( "Start CSP script ...")

    parser = argparse.ArgumentParser(description="CspGeneretor")
    parser.add_argument('--nameModule',  type=str, help="Name Module CSP")
    parser.add_argument('--fileLog',     type=str, help="Path file Log")
    parser.add_argument('--version',     type=str, help="Version Module")
    parser.add_argument('--setId',       type=int, help="Id value")
    parser.add_argument('--trt',         type=int, help="Type report storefront")
    parser.add_argument('--tra',         type=int, help="Type report admin")
    args = parser.parse_args()
    
    if (args.nameModule==None):
        args.nameModule = "csp_magento"
        #print ("Insert the module name")        
        #exitVar = True

    if (args.fileLog==None):
        args.fileLog = "errorClearTest.log"

    if (args.setId==None):
        args.setId = 0

    if (args.trt==None):
        args.trt = 0

    if (args.tra==None):
        args.tra = 0


    if (args.version==None):
        args.version = "1.0.0"
        
    if (exitVar==False):
        csp = createCsp(args)
        exit(csp)