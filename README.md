# Network Port Scanner

This is a Python command-line tool that scans open ports on network devices on the local subnet. The tool utilizes a multi-threaded approach to improve the scanning speed.

Usage:

To use this tool, open a command prompt in the same directory as the portscanner.py file and run the following command:


	python portscanner.py
  
The tool will prompt the user to enter the IP address of the host to be scanned.

Dependencies:

This tool requires Python 3.x and the following modules:

socket,
concurrent.futures,
Configuration


The following parameter can be configured in the netscan.py file:

n_threads: The number of threads (concurrent processes) that will be created to scan the host's ports. More threads means faster results but requires more resources.


License:
This tool is licensed under the MIT License. Feel free to modify and distribute it as needed.



