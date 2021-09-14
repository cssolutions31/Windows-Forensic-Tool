    
@echo OFF 
    echo ==================================SystemTimeDate================== >> systeminfo.txt
	date /t  >> systeminfo.txt
	time /t >> systeminfo.txt
	echo =========================================================================== >> systeminfo.txt
	echo ==================================WhoIsRunningSystem======================= >> systeminfo.txt
	whoami >> systeminfo.txt
	echo ==================================================================== >> systeminfo.txt
	echo ==================================SystemInformation================== >> systeminfo.txt
	systeminfo >> systeminfo.txt
	echo =========================================================================== >> systeminfo.txt
	echo ========================================NetworkDetails===================== >> networkinfo.txt
	ipconfig /all  >> networkinfo.txt
	echo =========================================================================== >> networkinfo.txt
	echo ========================================NetworkStats===================== >> networkstat.txt
	netstat -nao   >> networkstat.txt
	echo =========================================================================== >> networkstat.txt
	echo ========================================Traceroute_IP_Routes===================== >> iproutes.txt
	route print >> iproutes.txt
	echo =========================================================================== >> iproutes.txt
	tracert   google.com >> iproutes.txt
	echo =========================================================================== >> iproutes.txt
	echo ===============================ConnectedWifiNetworkDetails================= >> networkinfo.txt
	netsh wlan show profiles * key=clear  >> networkinfo.txt
	echo =========================================================================== >> networkinfo.txt
	echo =================================TasksRuninginBackgroud==================== >> tasklist.txt
	Tasklist >> tasklist.txt
	echo =====================================TaskListWithServices================== >> tasklist.txt
	tasklist /svc >> tasklist.txt
	echo ===================================TaskListWithModules===================== >> tasklist.txt
	tasklist /m >> tasklist.txt
	echo =========================================================================== >> tasklist.txt
	echo ==================================UsersOnSystem============================ >> systeminfo.txt
	net user %username% >> systeminfo.txt
	echo =========================================================================== >> systeminfo.txt
	echo ===============================SharedFilesOnSystem========================= >> systeminfo.txt
	net share >> systeminfo.txt
	echo ==================================workstationDetails======================== >> systeminfo.txt
	net config workstation >> systeminfo.txt
	echo =========================================================================== >> systeminfo.txt
	echo ==================================ClipboardData================== >> clipboard.txt
	powershell -command Get-Clipboard  >> clipboard.txt
	echo =========================================================================== >> clipboard.txt
	echo =====================================Dns-Information======================= >> dnsinfo.txt
	ipconfig /displaydns >> dnsinfo.txt
	echo =========================================================================== >> dnsinfo.txt
	echo ===============================MacAdressSavedInSystemARPCache============== >> networkinfo.txt
	arp -a >> networkinfo.txt
	echo =========================================================================== >> networkinfo.txt
    echo =====================================CmdHistory============================ >> clipboard.txt
    doskey /history >> clipboard.txt
	echo =========================================================================== >> clipboard.txt