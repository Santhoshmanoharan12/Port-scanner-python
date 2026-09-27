import json 
import csv


def print_report(results: list):
    print("\n------------       Scan Report    ------------")
    for res in results:
        print(f"{res['host']}:{res['port']} -> {res['status']} ({res['service']})")


def save_as_json(results: list, filename="scan_report.json"):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)
    print(f"Report saved as {filename}")

def save_as_csv(results: list, filename="scan_report.csv"):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["host", "port", "status", "service"])
        writer.writeheader()
        writer.writerows(results)
    print(f"Report saved as {filename}") 

