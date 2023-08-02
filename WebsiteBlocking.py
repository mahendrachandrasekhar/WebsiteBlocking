from datetime import datetime
import shutil
import time
## pip3 install pyyaml
import yaml

#hosts_file = "C:/Windows/System32/drivers/etc/hosts"
#hosts_file_new = "C:/Windows/System32/drivers/etc/hosts_new"
hosts_file = "C://users//mahendra//hosts"
hosts_file_backup = "C://users//mahendra//hosts_bak"
redirect="127.0.0.1"

base_cfg = 'config.yaml'
delete_line = False
sites_blocked = False
sites_unblocked = False

while True:
    new_content = []
    #Read the configurations
    config = yaml.safe_load(open(base_cfg, "r"))
    start_hour = config['start_hour']
    end_hour = config['end_hour']
    blocked_sites = config['blocked_sites']
    
    #Read the hosts file
    with open(hosts_file,"r") as reader:
        content = reader.read()
        for line in content.splitlines():
            if line.strip().startswith("#"):
                new_content.append(line)
            elif len(line.strip()) == 0:
                new_content.append(line)
            else:
                #Strip out the lines containing the website list we want.. Depending on the time we will either add it or remove it.
                if line.split()[1] in blocked_sites:
                    delete_line = True
                else:
                    new_content.append(line)
      
    if datetime.now().hour > start_hour and datetime.now().hour < end_hour:
        if not sites_blocked:
            #Take a backup first
            shutil.copyfile(hosts_file, hosts_file_backup)
            with open(hosts_file, 'w') as writer:
                for line in new_content:
    	            writer.write(line+'\n')
                for site in blocked_sites:
                    writer.write(redirect+' '+site+'\n')
                sites_blocked = True
                sites_unblocked = False
    else:
        if delete_line and not sites_unblocked:
            #Take a backup first
            shutil.copyfile(hosts_file, hosts_file_backup)
            with open(hosts_file, 'w') as writer:
                for line in new_content:
    	            writer.write(line+'\n')
                sites_blocked = False
                sites_unblocked = True
    
    time.sleep(20)
    print("Process Active: Sites have been blocked" if sites_blocked else "Process Active: Sites have been unblocked..Enjoy" )