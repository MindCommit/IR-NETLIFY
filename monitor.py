import os, requests

ACTIVE_F = "active_domains.txt"
FAILED_F = "failed_domains.txt"
CURRENT_F = "domain.txt"

def is_healthy(domain):
    # پاکسازی نام دامنه از کاراکترهای اضافه مثل 
    clean_domain = domain.split(' ')[-1].strip()
    if not clean_domain: return False
    
    url = f"https://{clean_domain}"
    try:
        # اضافه کردن هدر برای جلوگیری از مسدود شدن توسط فایروال
        headers = {'User-Agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=headers, timeout=10)
        
        # تشخیص دقیق مشابه تستر خودتان
        if "Site not found" in r.text or r.status_code == 404:
            return False
            
        return r.status_code == 200
    except: 
        return False

def run():
    current = ""
    if os.path.exists(CURRENT_F):
        with open(CURRENT_F, "r") as f: 
            current = f.read().strip()
    
    # اگر دامنه فعلی خراب بود یا خالی بود
    if not current or not is_healthy(current):
        print(f"⚠️ Domain {current} is down or invalid!")
        if current:
            with open(FAILED_F, "a") as f: 
                f.write(current + "\n")
        
        if os.path.exists(ACTIVE_F):
            with open(ACTIVE_F, "r") as f:
                pool = [l.strip() for l in f if l.strip()]
            
            new_found = False
            while pool:
                candidate = pool.pop(0)
                print(f"🔍 Checking candidate: {candidate}")
                if is_healthy(candidate):
                    # استخراج دامنه خالص برای ذخیره
                    new_domain = candidate.split(' ')[-1].strip()
                    with open(CURRENT_F, "w") as f: 
                        f.write(new_domain)
                    print(f"✅ Successfully switched to: {new_domain}")
                    new_found = True
                    break
                else:
                    with open(FAILED_F, "a") as f: 
                        f.write(candidate + "\n")
            
            # بروزرسانی لیست دامنه‌های فعال
            with open(ACTIVE_F, "w") as f: 
                f.write("\n".join(pool))
        else:
            print("❌ No active domains left in pool!")

if __name__ == "__main__":
    run()
