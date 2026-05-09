import os
import json
import urllib.parse

def generate_configs():
    # --- Server Data ---
    servers = [
        {"name": "ParsaServer", "address": "netlify.parsashonam.sbs:444", "path": "/p4r34m", "user": "Telegram-Parsashonam"},
        {"name": "Xarheon", "address": "xarheon.run.place", "path": "/cdn2", "user": "f9b57060-989a-4d6d-bc58-53d767242968"},
        {"name": "OneSrv98", "address": "s1.onesrv98.eu.cc:444", "path": "/mine", "user": "a5c04120-8f0d-4d52-8cdd-9ffff79a777d"},
        {"name": "Flare", "address": "https://flare.diablo0.site:24855", "path": "/free", "user": "dab65f2a-48ca-4fe8-9143-06cd28f00a21"},
        {"name": "Alwinbalot", "address": "https://solar.latnashobivojod.shop:8096", "path": "/alwin", "user": "ccee709a-5766-4ced-a6ec-7b9d46cdd48d"}
    ]

    # --- Assets for SUB_new ---
    new_snis = ["kubernetes.io", "jobset.sigs.k8s.io","kwok.sigs.k8s.io"]
    new_ips = [
        "144.76.1.88", "85.10.207.48", "94.130.33.41", "95.216.69.37",
        "204.12.196.34", "94.130.70.160", "138.201.54.122",
        "142.54.178.211", "63.141.252.203"
    ]

    # --- Assets for Original SUB ---
    old_direct_snis = [
        "kubernetes.io", "letsencrypt.org", "kwok.sigs.k8s.io", "kind.sigs.k8s.io",
        "krew.sigs.k8s.io", "kueue.sigs.k8s.io", "jobset.sigs.k8s.io", "minikube.sigs.k8s.io",
        "kustomize.sigs.k8s.io", "cluster-api.sigs.k8s.io", "gateway-api.sigs.k8s.io",
        "image-builder.sigs.k8s.io", "kubectl.docs.kubernetes.io", "scheduler-plugins.sigs.k8s.io",
        "secrets-store-csi-driver.sigs.k8s.io"
    ]
    old_combo_snis = ["kubernetes.io", "letsencrypt.org", "jobset.sigs.k8s.io", "gateway-api.sigs.k8s.io", "cluster-api.sigs.k8s.io"]
    old_ips = ["50.7.87.4", "144.76.1.88", "85.10.207.48", "95.216.69.37", "94.130.13.19", "94.130.50.12", "94.130.33.41", "204.12.196.34"]

    def create_vless(user, address, sni, host, path, remark, x_host=None):
        base_path = urllib.parse.quote(path, safe='')
        params = f"encryption=none&security=tls&sni={sni}&alpn=h2%2Chttp%2F1.1&insecure=1&allowInsecure=1&type=xhttp&host={host}&path={base_path}&mode=auto"
        
        if x_host:
   #         clean_xhost = x_host.replace("https://", "").replace("http://", "")
            extra_dict = {"headers": {"x-host": x_host}}
            extra_json = json.dumps(extra_dict, separators=(',', ':'))
            params += f"&extra={urllib.parse.quote(extra_json)}"
            
        return f"vless://{user}@{address}:443?{params}#{urllib.parse.quote(remark)}"

    # 1. Process Original Sub (IR_NETLIFY_SUB.txt)
    if os.path.exists("domain.txt"):
        with open("domain.txt", "r") as f:
            host_old = f.read().strip()
        
        old_results = []
        for sni in old_direct_snis:
            old_results.append(create_vless("Telegram-Parsashonam", sni, sni, host_old, "/p4r34m", f"🌐 @IR_NETLIFY   {sni}"))
        for sni in old_combo_snis:
            for ip in old_ips:
                old_results.append(create_vless("Telegram-Parsashonam", ip, sni, host_old, "/p4r34m", f"🌐 @IR_NETLIFY  {sni}  {ip}"))
        
        with open("IR_NETLIFY_SUB.txt", "w") as f:
            f.write("\n".join(old_results))

    # 2. Process New Sub (IR_NETLIFY_SUB_new.txt)
    if os.path.exists("domain_new.txt"):
        with open("domain_new.txt", "r") as f:
            host_new = f.read().strip()
            
        new_results = []
        for srv in servers:
            # Direct SNI mode
            for sni in new_snis:
                remark = f"🌐 @IR_NETLIFY | {sni} | {srv['name']}"
                new_results.append(create_vless(srv['user'], sni, sni, host_new, srv['path'], remark, srv['address']))
            
            # IP + SNI mode
            for sni in new_snis:
                for ip in new_ips:
                    remark = f"🌐 @IR_NETLIFY | {sni} | {ip} | {srv['name']}"
                    new_results.append(create_vless(srv['user'], ip, sni, host_new, srv['path'], remark, srv['address']))

        with open("IR_NETLIFY_SUB_new.txt", "w") as f:
            f.write("\n".join(new_results))

if __name__ == "__main__":
    generate_configs()
