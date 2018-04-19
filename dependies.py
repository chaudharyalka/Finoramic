from subprocess import call
import os
import json
import re

#|| -> continue if previous command fails
#&& -> continue if preivous command succeeds


def install(name,version):
      a = (os.popen("apt-get install " + name + "="+ version + " -y && echo 1 || echo -1" ).read())
      install_status = a.rstrip()

      getStatus = (list(install_status))[-1]
      return  getStatus

def installDependies(fileName):

    file1 = open(fileName,"r")
    pattern = re.compile(r'\s+')
    anyFailedPackage = 1
    failedCase = []
    
    for package in file1:
        package = re.sub(',' , '' ,package) 
        package = re.sub(pattern , '',package)
   
        if (package != ""):
              first_half = package[:package.find('=')]
              version = package[package.find('=')+2:]
              package_status_i = (os.popen("dpkg -l " + first_half + " && echo 1 || echo -1").read())
              
              try:
                  package_status_i = int(package_status_i)
                  anyFailedPackage = -1
                  failedCase.append(first_half ,  "no packages found")
                  continue
              except:
                  package_status_i = 1


              if (package_status_i == 1):
                package_status = int (os.popen("dpkg -l " + first_half + " | grep " + version + " && echo 1 || echo -1").read() )
    
              if (package_status == -1):
                  #not installed try to install it:
                  checkVersionAvailability =  (os.popen("apt-cache madison " + first_half + " | grep " + version + " && echo 1 || echo -1").read())
                  try:
                      c = int(checkVersionAvailability)
                      # version not found
                      failedCase.append((first_half + "_" + version , "Not avaiable"))                  
                  except:
                      install_status = install(first_half,version) 
                      if (install_status == -1):
                          failedCase.append((first_half + "_" + version , "unable to install"))
                          anyFailedPackage = -1
                  
    if (anyFailedPackage == 1):
        print "Success"
    else:
        for (package,reason) in failedCase:
            print (package + " : " + reason)


fileName = "dependencies.txt"
installDependies(fileName)
