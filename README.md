# Local_DOS_Flood

Usage for old version:
`python local_DOS_flood.py 192.168.1.123`
Replace the IP with your target

New **main.py** file has been written by ChatGPT May 3 Version

Required a lot of human prompts and refinement

No pip installs necessary, just need to download nmap for your system: **https://nmap.org**

After installing nmap, run `python main.py` and follow instructions from there

Don't do bad stuffs, you will go jail 😜

Implemented:
* **Multiprocessing** to scan the network and launch multiple processes for the DoS attack.
* **Subprocess** module to execute nmap command and obtain a list of available IPs on the network.
* Function to get the **hostname** of the IPs that are being scanned.
* Allows the user to **select** which IP address to target by entering the ID or last three digits of the IP address.
* Allows the user to select the number of simultaneous **processes** to run for the DoS attack.
* Handles **Keyboard Interrupt** exception by terminating the running processes and joining them back.
