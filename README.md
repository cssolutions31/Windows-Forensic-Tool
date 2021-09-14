# Windows-Forensic-Tool
 Cyber forensics is an application of investigation and analysis techniques to gather and preserve evidence from particular systems.  To run an appropriate investigation to find the cause of cybercrime and cyber Criminals. To Provide justice to Victims of cybercrime.
 Cyber Forensic Investigator is the person who is responsible for the whole process of forensic investigation of cybercrime. He is the one who collects all the evidence and analyses.  
 The Objective of Cyber forensics is to perform a structured investigation and maintain a documented chain of evidence to find out exactly what happened to the device and who was responsible for it.
There are two types of data collected in Computer Forensics Persistent data and Volatile data. Persistent data is that data that is stored on a local hard drive and is preserved when the computer is OFF. Volatile data is any kind of data that is stored in memory, which will be lost when computer power or OFF. Volatile data resides in the registry’s cache and random access memory (RAM). This investigation of the volatile data is called “live forensics”.
Collecting volatile data is the first thing that every forensic investigator will do on the device that is a victim of cybercrime. But collecting volatile data one by one is a time-consuming process and time in such cases there can be time limitations due to some circumstances.so I created a script using python that collects volatile data from the system by just clicking on it. it does not require running from any ide or the system. The script is easy to use, Users can change the code according to their requirements.
This Tool creates multiple text files containing volatile information that later helps the investigators get some extra time to investigate. The list of info it will extract is as follows:
1. System Time and Date
2. User Running on System and All Users Details.
3. Data on the clipboard and Command prompt History.
4. Information About the system
5. Routing Table, Network Details, Network statistics
6. Task running on Background with their services
7. Shared files on the system and Workstation Details
8. DNS details
We will add other features with future updates on Github. If the system does not have python installed, you can use the batch script. 
