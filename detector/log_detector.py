import time
import os
import re

# File paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "../logs/system.log")
ALERT_FILE = os.path.join(BASE_DIR, "../logs/alerts.log")
BLOCKED_IP_FILE = os.path.join(BASE_DIR, "../logs/blocked_ips.log")

# Extract IP from log
def extract_ip(log_line):
    ip_pattern = r'(?:\d{1,3}\.){3}\d{1,3}'
    match = re.search(ip_pattern, log_line)
    if match:
        return match.group()
    return None

# Write alert
def write_alert(alert_message):
    with open(ALERT_FILE, "a") as f:
        f.write(alert_message + "\n")

# Block IP automatically
def block_ip(ip):

    if ip is None:
        return

    if os.path.exists(BLOCKED_IP_FILE):
        with open(BLOCKED_IP_FILE, "r") as f:
            blocked_ips = f.read().splitlines()
    else:
        blocked_ips = []

    if ip not in blocked_ips:

        # Save to blocked IP log
        with open(BLOCKED_IP_FILE, "a") as f:
            f.write(ip + "\n")

        # Block using firewall
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

        print(f"[AUTO RESPONSE] Blocked IP in firewall: {ip}")

# Monitor logs
def monitor_logs():

    print("🛡️ SOC Detection & Auto-Response Started...")

    with open(LOG_FILE, "r") as file:

        file.seek(0, os.SEEK_END)

        while True:

            line = file.readline()

            if not line:
                time.sleep(1)
                continue

            line = line.strip()

            attacker_ip = extract_ip(line)

            if "FAILED_LOGIN" in line:

                alert = f"[ALERT] Failed Login from IP: {attacker_ip}"
                print(alert)

                write_alert(alert)

                block_ip(attacker_ip)

            elif "PORT_SCAN" in line:

                alert = f"[ALERT] Port Scan from IP: {attacker_ip}"
                print(alert)

                write_alert(alert)

                block_ip(attacker_ip)

            elif "MALWARE" in line:

                alert = f"[ALERT] Malware Activity from IP: {attacker_ip}"
                print(alert)

                write_alert(alert)

                block_ip(attacker_ip)

monitor_logs()

