import socket
import threading
import concurrent.futures
import colorama
from colorama import Fore


print_lock = threading.Lock()


colorama.init()

ip = input("Please put the ip to scane. (For example; 192.168.1.1): ")

def scan(ip, port):
    scanner =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    
    
    
    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            
            print(Fore.WHITE + f"[{port}] " + Fore.GREEN + "Opened")
    
    except:
        pass

    
with concurrent.futures.ThreadPoolExecutor(max_workers = 1000) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port +1 )
            
        

    
    
        