# 🔍 Net Scanner - Python TCP Network Scanner

A simple **TCP network port scanner built with Python** that checks whether TCP ports are **open, closed, or timed out** on an authorized target and saves the scan results in **JSON and CSV** formats.

This project is designed as a beginner-friendly cybersecurity project to understand how **TCP connections, sockets, ports, exception handling, and network scanning** work.

---

## 📌 Features

* TCP port scanning using Python
* IPv4 socket communication
* Configurable port range
* Connection timeout handling
* Detects:

  * `OPEN`
  * `CLOSED`
  * `TIMEOUT`
  * `ERROR`
* Common port/service identification
* JSON report generation
* CSV report generation
* Simple and modular project structure
* Uses Python standard library

---

## 💻 How It Works

The scanner attempts to establish a TCP connection with a target IP address and port.

```text
Target IP + Port
       │
       ▼
Create TCP Socket
       │
       ▼
Set Connection Timeout
       │
       ▼
Attempt TCP Connection
       │
   ┌───┴──────────────┐
   ▼                  ▼
Success             Failure
   │                  │
   ▼             ┌────┴─────────┐
 OPEN            ▼              ▼
             REFUSED         TIMEOUT
                │               │
                ▼               ▼
              CLOSED         TIMEOUT
```

### Example

```text
Target: 127.0.0.1

Port 22   → CLOSED
Port 80   → OPEN
Port 443  → OPEN
Port 3306 → CLOSED
```

> **Note:** A timeout does not necessarily mean that a port is closed. It may indicate filtering, firewall behavior, network problems, or an unreachable target.

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python 3   | Main programming language |
| `socket`   | TCP network communication |
| `json`     | JSON report generation    |
| `csv`      | CSV report generation     |
| `datetime` | Scan timestamp            |
| Git        | Version control           |

No external Python packages are required for the basic version.

---

## 📂 Project Structure

```text
Net Scanner/
│
├── __pycache__/
├── .gitignore
├── Readme.MD
├── scanner.py
├── services.py
├── reporter.py
├── scan_report.json
└── scan_report.csv
```

### `scanner.py`

Contains the main TCP scanning logic.

**Responsibilities:**

* Create TCP sockets
* Set connection timeout
* Connect to the target
* Check individual ports
* Identify connection results
* Return scan results

---

### `services.py`

Contains information about common network ports and their expected services.

Example:

| Port | Common Service |
| ---: | -------------- |
|   21 | FTP            |
|   22 | SSH            |
|   25 | SMTP           |
|   53 | DNS            |
|   80 | HTTP           |
|  443 | HTTPS          |
| 3306 | MySQL          |

> The service name is based on the commonly associated port. A port number alone does **not** prove which software is actually running.

---

### `reporter.py`

Handles the storage of scan results.

It generates:

```text
scan_report.json
scan_report.csv
```

This separates **scanning** from **report generation**, making the project easier to maintain.

---

### `scan_report.json`

Stores scan results in structured JSON format.

Example:

```json
[
    {
        "target": "127.0.0.1",
        "port": 80,
        "status": "OPEN",
        "service": "HTTP"
    },
    {
        "target": "127.0.0.1",
        "port": 22,
        "status": "CLOSED",
        "service": "SSH"
    }
]
```

---

### `scan_report.csv`

Stores the same information in a spreadsheet-friendly format.

Example:

```csv
target,port,protocol,status,service
127.0.0.1,80,TCP,OPEN,HTTP
127.0.0.1,22,TCP,CLOSED,SSH
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Open the Project

```bash
cd Net-Scanner
```

### 3. Run the Scanner

```bash
python scanner.py
```

Configure the target and port range inside `scanner.py` according to your implementation.

---

## 🧪 Safe Testing

For learning and development, use a system that you **own or have explicit permission to test**.

### Local Computer

```text
127.0.0.1
```

`127.0.0.1` is the loopback address of your own computer.

You can also use a deliberately configured cybersecurity lab or virtual machine.

### Example

```text
Target:
127.0.0.1

Port Range:
1 - 1024
```

> ⚠️ Do not scan websites, servers, or networks belonging to other people or organizations without explicit authorization.

---

## 📊 Scan Result States

| Status    | Meaning                                                |
| --------- | ------------------------------------------------------ |
| `OPEN`    | TCP connection was successfully established            |
| `CLOSED`  | Target responded that the connection was refused       |
| `TIMEOUT` | No response was received within the configured timeout |
| `ERROR`   | An unexpected socket/network error occurred            |

---

## 🔬 Core TCP Concept

The scanner uses:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

### `AF_INET`

Specifies **IPv4**.

```text
AF_INET → IPv4
```

### `SOCK_STREAM`

Specifies a stream socket, normally used for **TCP**.

```text
SOCK_STREAM → TCP
```

Therefore:

```python
socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

means:

> Create an IPv4 TCP socket.

---

## 🔄 Scanner Workflow

```text
Start
  │
  ▼
Select Target
  │
  ▼
Select Port Range
  │
  ▼
For Each Port
  │
  ▼
Create TCP Socket
  │
  ▼
Set Timeout
  │
  ▼
Attempt Connection
  │
  ├───────────────┐
  ▼               ▼
Success         Failure
  │               │
  ▼          ┌────┴───────┐
 OPEN        ▼            ▼
          REFUSED       TIMEOUT
             │            │
             ▼            ▼
           CLOSED       TIMEOUT
             │            │
             └─────┬──────┘
                   ▼
              Save Result
                   │
                   ▼
               Next Port
                   │
                   ▼
             Scan Complete
                   │
          ┌────────┴────────┐
          ▼                 ▼
      JSON Report       CSV Report
```

---

## 🎯 Learning Objectives

This project helps understand the fundamentals of:

* Computer networks
* TCP/IP
* IPv4
* TCP connections
* Network ports
* Python sockets
* Exception handling
* Timeouts
* Loops
* Functions
* File handling
* JSON
* CSV
* Basic cybersecurity
* Modular Python programming

---

## 🧩 Development Approach

The project is being developed incrementally:

1. Create TCP socket
          ↓
2. Scan one port
          ↓
3. Handle OPEN/CLOSED/TIMEOUT
          ↓
4. Scan a port range
          ↓
5. Store results
          ↓
6. Identify common services
          ↓
7. Generate JSON report
          ↓
8. Generate CSV report
          ↓
9. Improve CLI
          ↓
10. Add concurrent scanning

## 🔮 Future Improvements

Possible future versions may include:

Multi-threaded TCP scanning

Command-line arguments

Custom timeout configuration

IPv6 support

Better error classification

Scan statistics

Service detection

Logging

Multiple output formats

Input validation

Unit tests

Configuration files

Progress indicators

Local cybersecurity lab integration
## ⚠️ Legal & Ethical Use

This project is intended for educational and authorized security testing.

Only scan:

Your own computer
Your own servers
Your own network
Authorized penetration-testing environments
Cybersecurity lab machines where you have permission

Unauthorized port scanning may violate organizational policies, terms of service, or applicable laws.

The author is not responsible for misuse of this tool.

## 👨‍💻 Project Goal

The goal of this project is not just to create a port scanner, but to understand what happens underneath a network connection:

Python
  ↓
Socket API
  ↓
Operating System
  ↓
TCP/IP Stack
  ↓
Network Interface
  ↓
Target

By building the scanner from the ground up, this project demonstrates practical understanding of network programming and cybersecurity fundamentals.

## 📚 What I Learned

Through this project, I learned how to:

Create TCP sockets using Python
Work with IPv4 addresses
Connect to TCP ports
Handle connection timeouts
Handle connection-refused errors
Scan multiple ports
Organize Python code into modules
Store structured data in JSON
Export scan results to CSV
Understand basic network-service relationships
Build a small cybersecurity tool from scratch

## ⭐ Project Status

Current Status: 🚧 In Development

The basic TCP scanning and report-generation functionality is being developed incrementally.