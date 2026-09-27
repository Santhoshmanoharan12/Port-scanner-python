
import socket 
from services import get_service_name
from reporter import save_as_csv, print_report, save_as_json


def scan():
    """ get hostname and IP address
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print(f"HOSTNAME: {hostname}")
    print(f"IP ADDRESS: {ip_addr}")
    """


    print("\n------++--++--  Simple Port Scanner  ---++--++------")
    print("\033[1;36mBuild By -> @Santhosh ???\033[0m")


    status = ""
    results = []
    targetHost = input("Enter the Target Host to Scan Here : ") # Replace with the target host you want to scan
    scan_start_ports = int(input("Enter the Starting Port Number to Scan Here : ")) # Replace with the starting port number you want to scan
    scan_end_ports = int(input("Enter the Ending Port Number to Scan Here : ")) # Replace with the ending port number you want to scan
    for targetPort in range(scan_start_ports, scan_end_ports + 1):
        sockTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sockTCP.settimeout(1)  # Set a timeout of 1 second for the connection attempt
        service_name = get_service_name(targetPort)
        try:
            sockTCP.connect((targetHost, targetPort))
            status = "Open"

        except socket.timeout:
            status = "Timeout"
           
        except ConnectionRefusedError:
            status = "Closed"           

        except Exception as e:
            return(f"Error ----> {e}")

        finally:
            sockTCP.close()

        service_name = get_service_name(targetPort)
        results.append({
            "host": targetHost,
            "port": targetPort,
            "status": status,
            "service": service_name
        })

    return results



if __name__ == "__main__":
    scan_res = scan()
    print_report(scan_res)
    save_as_json(scan_res)
    save_as_csv(scan_res)
