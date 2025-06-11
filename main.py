from os import system
from colorama import Fore, Back, Style


addresses:list[list] = None
results:list = list()

with open('./ip_addresses.txt', 'r') as f:
    addresses = [line.split() for line in f.readlines()]

for elem in addresses:
    addr_info = elem[0]
    return_code = system(f"ping -c 1 {addr_info}")
    results.append(return_code)



for i in range(len(results)):
    addr_info = addresses[i]
    ip_addr = addr_info[0]
    comment = addr_info[1] if len(addr_info) > 1 else None
    res = results[i]
    color = Fore.RED if res else Fore.GREEN
        
    print(color + f"ping to {ip_addr} {'failed' if res else 'successful'}\t\t{comment if comment else ''}" + Style.RESET_ALL)