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
        print(f"Current domain {current} failed. Searching for a new one...")
        if current:
            with open(FAILED_FILE, "a") as f:
                f.write(current + "\n")
        

        if os.path.exists(ACTIVE_FILE):
            with open(ACTIVE_FILE, "r") as f:
                pool = [line.strip() for line in f if line.strip()]
            
            found_healthy = False
            while pool:
                candidate = pool.pop(0) 
                print(f"Testing: {candidate}...")
                
                if verify_domain(candidate):
                    with open(CURRENT_FILE, "w") as f:
                        f.write(candidate)
                    found_healthy = True
                    print(f"Success! New healthy domain found: {candidate}")
                    break 
                else:
                    print(f"Candidate {candidate} also failed. Moving to failed list.")
                    with open(FAILED_FILE, "a") as f:
                        f.write(candidate + "\n")
            
            
            with open(ACTIVE_FILE, "w") as f:
                f.write("\n".join(pool))
                
            if not found_healthy:
                print("Alert: All domains in active_domains.txt are broken!")
    else:
        print(f"Domain {current} is healthy. No action needed.")

if __name__ == "__main__":
    main()
