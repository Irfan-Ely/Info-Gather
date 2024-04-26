import subprocess
import sys
import os
def subdomain_enumeration(target):
    command = f"sublist3r -d {target} -o subdomains.txt"
    subdomain_result=subprocess.run(command, shell=True)
    return subdomain_result    
    
def get_ip_with_ping(target):
    result = subprocess.run(["ping", "-c", "1", target], capture_output=True)
    lines = result.stdout.decode().splitlines()
    for line in lines:
        if "from" in line:
            _ip=line.split()[4]
            print(f"IP address of {target}: {_ip}")
            
        
def port_scan_and_service_identification(target):
    nmap_command = f"nmap {target} "
    output = subprocess.run(nmap_command, shell=True, capture_output=True, text=True)
    print(output.stdout)
     
     
def dig_lookup(target, type="mx"):
    command = f"dig {target} {type}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
    	print(result.stdout)
    else:
        print(f"Error: {result.stderr}")
        
def nikto_scanner(target):
    command = f"nikto -h {target}"
    os.system(command)
                
                
def traceroute(target):
	command = f"traceroute {target}"
	result = subprocess.run(command, shell=True, capture_output=True, text=True)
	if result.returncode == 0:
		print(result.stdout)
	else:
		print(f"Error: {result.stderr}")
        

if len(sys.argv)<2:

	print("Invalid : \n\n> Python3 Info-Gathering.py <target>")
	print(".......................................")
else:
	target=sys.argv[1]
	print("\n\nInit.....\n\n")
	get_ip_with_ping(target)
	print("==================================================")
	print("Subdomains :")
	subdomain_enumeration(target)
	print("==================================================")
	print("Port's and Services : ")
	port_scan_and_service_identification(target)
	print("==================================================")
	print("DNS Lookup : ")
	dig_lookup(target)
	print("==================================================")
	print("TraceRoute : ")
	traceroute(target)
	print("==================================================")
	print("Server Vulnerability Scan  : ")
	nikto_scanner(target)
	print("==================================================")
	
