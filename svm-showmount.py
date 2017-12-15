"""CLI-GET-JUNCTION-PATH Ver1.0 18SEP2017 by Littlehawk."""


import sys
import paramiko
import re

no_of_args = len(sys.argv)
if no_of_args != 5:
    print ("Example: svm-showmount.py [Cluster Mgmt IP] [Username] [Password] [SVM Name]")
    sys.exit(1)

Cluster_IP = sys.argv[1]
Cluster_user = sys.argv[2]
Cluster_pass = sys.argv[3]
svm_name = sys.argv[4]

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(Cluster_IP, username=Cluster_user, password=Cluster_pass)
# Exec cli command to get junction path.
stdin, stdout, stderr = client.exec_command("volume show -vserver " + svm_name + " -fields junction-path")
# Split lines in to list data
Vols_details = stdout.read().splitlines()
# Remove 3 first line from list
del Vols_details[0:3]
# Remove 2 last line from list
del Vols_details[len(Vols_details)-2:len(Vols_details)]
# Display All junction-path
for details in Vols_details:
    junc_path = details.split()
    if (junc_path[2] != "-") and (re.match("\/vol*\w+[//]", junc_path[2])):
        print junc_path[2]
# End of script
