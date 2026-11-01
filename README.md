Welcome to the ASM project LetJustSayManagement

I****** This is tested on Ubuntu 24.04*******

Attack Surface Management (ASM) is an automated, continuous process of identifying, classifying, monitoring, and managing the external attack surface of an organization. Unlike traditional vulnerability management, which focuses on internal systems, ASM focuses on the ever-changing external environment.

Key Goals of ASM
•	Discovery: Continuously identify internet-facing assets that may be exposed to attackers.
•	Classification: Categorize assets and understand their risk profile.
•	Monitoring: Continuously track assets for vulnerabilities, misconfigurations, and other security risks.
•	Remediation: Fix or mitigate risks to reduce the attack surface.



------Nmaps------
The goal of Nmap is used for asset Discovery. It identifies exposed services and open ports on a target system

------Osquery------ 
the goual of Osquery is used for continuous monitoring. It continuously monitors the system for changes in configurations, open ports, and running services.

------OpenVAS------
The goal of openVAS is to scan for known vulnerabilities in identified assets.



Installation 
sudo apt update


-----nmaps------
sudo apt install nmap

------Osquery------
sudo apt install Osqueryi
