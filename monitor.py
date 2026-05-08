import os
import requests

ACTIVE_FILE = "active_domains.txt"
FAILED_FILE = "failed_domains.txt"
CURRENT_FILE = "domain.txt"

def verify_domain(domain):
    try:
        response = requests.get(f"https://{domain.strip()}", headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        if "Site not found" in response.text or response.status_code == 404:
            return False
        return True
    except:
        return False

def main():
    if not os.path.exists(CURRENT_FILE):
        return

    with open(CURRENT_FILE, "r") as f:
        current = f.read().strip()
    
    if not current or not verify_domain(current):
        if current:
            with open(FAILED_FILE, "a") as f:
                f.write(current + "\n")
        
        if os.path.exists(ACTIVE_FILE):
            with open(ACTIVE_FILE, "r") as f:
                pool = [line.strip() for line in f if line.strip()]
            
            if pool:
                next_up = pool.pop(0)
                with open(CURRENT_FILE, "w") as f:
                    f.write(next_up)
                with open(ACTIVE_FILE, "w") as f:
                    f.write("\n".join(pool))
                print(f"Switched to: {next_up}")
            else:
                print("No more domains left!")
    else:
        print("Domain is still healthy.")

if __name__ == "__main__":
    main()
