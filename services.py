

CommonPortServices = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP-Server",
    68: "DHCP-Client",
    69: "TFTP",
    80: "HTTP",
    88: "Kerberos",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "RPC",
    137: "NetBIOS-Name",
    138: "NetBIOS-Datagram",
    139: "NetBIOS-Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP-Trap",
    179: "BGP",
    194: "IRC",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    500: "ISAKMP/IKE",
    514: "Syslog",
    587: "SMTP-Submission",
    636: "LDAPS",
    873: "Rsync",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1194: "OpenVPN",
    1433: "MSSQL",
    1521: "Oracle-DB",
    1723: "PPTP",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5060: "SIP",
    5432: "PostgreSQL",
    5672: "RabbitMQ",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Proxy/Alt",
    8443: "HTTPS-Alt",
    9000: "SonarQube/PHP-FPM",
    9200: "Elasticsearch",
    27017: "MongoDB",
}

def get_service_name(port : int) -> str:

    return CommonPortServices.get(port, "Unknown Service")


if __name__ == "__main__":
    get_service_name()

