import os
def main():
	
	print(":'######:::'######:::'######:::'#######::'##:::::::'##::::'##:'########:'####::'#######::'##::: ##::'######::"
		  "'##... ##:'##... ##:'##... ##:'##.... ##: ##::::::: ##:::: ##:... ##..::. ##::'##.... ##: ###:: ##:'##... ##:"
          "##:::..:: ##:::..:: ##:::..:: ##:::: ##: ##::::::: ##:::: ##:::: ##::::: ##:: ##:::: ##: ####: ##: ##:::..::"
          "##:::::::. ######::. ######:: ##:::: ##: ##::::::: ##:::: ##:::: ##::::: ##:: ##:::: ##: ## ## ##:. ######::"
          "##::::::::..... ##::..... ##: ##:::: ##: ##::::::: ##:::: ##:::: ##::::: ##:: ##:::: ##: ##. ####::..... ##:"
          "##::: ##:'##::: ##:'##::: ##: ##:::: ##: ##::::::: ##:::: ##:::: ##::::: ##:: ##:::: ##: ##:. ###:'##::: ##:"
          ". ######::. ######::. ######::. #######:: ########:. #######::::: ##::::'####:. #######:: ##::. ##:. ######::"
          ":......::::......::::......::::.......:::........:::.......::::::..:::::....:::.......:::..::::..:::......:::")
	os.system("echo ==================================SystemTimeDate================== >> systeminfo.txt")
	os.system("date /t  >> systeminfo.txt")
	os.system("time /t >> systeminfo.txt")
	os.system("echo =========================================================================== >> systeminfo.txt")
	os.system("echo ==================================WhoIsRunningSystem======================= >> systeminfo.txt")
	os.system("whoami >> systeminfo.txt")
	os.system("echo ==================================================================== >> systeminfo.txt")
	os.system("echo ==================================SystemInformation================== >> systeminfo.txt")
	os.system("systeminfo >> systeminfo.txt")
	os.system("echo =========================================================================== >> systeminfo.txt")
	os.system(" echo ========================================NetworkDetails===================== >> networkinfo.txt")
	os.system("ipconfig /all  >> networkinfo.txt")
	os.system("echo =========================================================================== >> networkinfo.txt")
	os.system(" echo ========================================NetworkStats===================== >> networkstat.txt")
	os.system("netstat -nao   >> networkstat.txt")
	os.system("echo =========================================================================== >> networkstat.txt")
	os.system(" echo ========================================Traceroute_IP_Routes===================== >> iproutes.txt")
	os.system("route print >> iproutes.txt")
	os.system("echo =========================================================================== >> iproutes.txt")
	os.system("tracert   google.com >> iproutes.txt")
	os.system("echo =========================================================================== >> iproutes.txt")
	os.system("echo ===============================ConnectedWifiNetworkDetails================= >> networkinfo.txt")
	os.system("netsh wlan show profiles * key=clear  >> networkinfo.txt")
	os.system("echo =========================================================================== >> networkinfo.txt")
	os.system("echo =================================TasksRuninginBackgroud==================== >> tasklist.txt")
	os.system("Tasklist >> tasklist.txt")
	os.system("echo =====================================TaskListWithServices================== >> tasklist.txt")
	os.system("tasklist /svc >> tasklist.txt")
	os.system("echo ===================================TaskListWithModules===================== >> tasklist.txt")
	os.system("tasklist /m >> tasklist.txt")
	os.system("echo =========================================================================== >> tasklist.txt")
	os.system("echo ==================================UsersOnSystem============================ >> systeminfo.txt")
	os.system("net user %username% >> systeminfo.txt")
	os.system("echo =========================================================================== >> systeminfo.txt")
	os.system("echo ===============================SharedFilesOnSystem========================= >> systeminfo.txt")
	os.system("net share >> systeminfo.txt")
	os.system("echo ==================================workstationDetails======================== >> systeminfo.txt")
	os.system("net config workstation >> systeminfo.txt")
	os.system("echo =========================================================================== >> systeminfo.txt")
	os.system("echo ==================================ClipboardData================== >> clipboard.txt")
	os.system("powershell -command Get-Clipboard  >> clipboard.txt")
	os.system("echo =========================================================================== >> clipboard.txt")
	os.system("echo =====================================Dns-Information======================= >> dnsinfo.txt")
	os.system("ipconfig /displaydns >> dnsinfo.txt")
	os.system("echo =========================================================================== >> dnsinfo.txt")
	os.system("echo ===============================MacAdressSavedInSystemARPCache============== >> networkinfo.txt")
	os.system("arp -a >> networkinfo.txt")
	os.system("echo =========================================================================== >> networkinfo.txt")
    os.system("echo =====================================CmdHistory============================ >> clipboard.txt")
    os.system("doskey /history >> clipboard.txt")
	os.system("echo =========================================================================== >> clipboard.txt")



if __name__ == '__main__':
	main()