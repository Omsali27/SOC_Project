import os

BLOCKED_IP_FILE = os.path.expanduser("~/SOC_Project/logs/blocked_ips.log")

def block_ip(ip):

    # Read existing blocked IPs
    if os.path.exists(BLOCKED_IP_FILE):
        with open(BLOCKED_IP_FILE, "r") as f:
            blocked_ips = f.read().splitlines()
    else:
        blocked_ips = []

    # Block only if not already blocked
    if ip not in blocked_ips:

        # Save only IP (not message)
        with open(BLOCKED_IP_FILE, "a") as f:
            f.write(ip + "\n")

        print(f"[RESPONSE] Blocked IP: {ip}")

    else:
        print(f"[INFO] IP already blocked: {ip}")


# Run program
if __name__ == "__main__":
    ip = input("Enter IP to block: ").strip()
    block_ip(ip)

