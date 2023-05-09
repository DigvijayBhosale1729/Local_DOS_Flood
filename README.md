# Local_DOS_Flood

**Forked from an old project**

New **main.py** file has been written by ChatGPT May 3 Version

Required a lot of human prompts and refinement

No pip installs necessary, just need to download nmap for your system: **https://nmap.org**



Implemented:
* **Multiprocessing** to scan the network and launch multiple processes for the DoS attack.
* **Subprocess** module to execute nmap command and obtain a list of available IPs on the network.
* Function to get the **hostname** of the IPs that are being scanned.
* Allows the user to **select** which IP address to target by entering the ID or last three digits of the IP address.
* Allows the user to select the number of simultaneous **processes** to run for the DoS attack.
* Handles **Keyboard Interrupt** exception by terminating the running processes and joining them back.
