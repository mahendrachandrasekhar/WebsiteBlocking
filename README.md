# WebsiteBlocking
 - This piece of code is a simple program to block sites during a particular time of the day on a windows machine.
 - The config.yaml contains the times of the day the websites should be blocked
 - The websites to be blocked are in the list
 - The code needs to run as administrator.
 - It will read the config every 20 seconds and based on the updated timings, and updated websites, it will add/remove lines from the hosts file.
 - **Note:** You need to change the code to point to your actual hosts file (typically under C:\Windows\System32\drivers\etc)
 - You will need to install python to run this program.
 - To execute the program run:
 **`python.exe WebsiteBlocking.py`** 
