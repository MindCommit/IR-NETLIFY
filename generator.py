import os
import json
import urllib.parse
import random


def create_vless(user, address, sni, host, path, remark, x_host=None):
    base_path = urllib.parse.quote(path, safe="")
    
    extra_data = {
        "xPaddingBytes": "1-1",
        "scMaxEachPostBytes": "1000000",
        "headers": {}
    }
    
    if x_host:
        extra_data["headers"]["x-host"] = x_host
    
    params = (
        f"encryption=none&security=tls&sni={sni}&alpn=h2%2Chttp%2F1.1"
        f"&insecure=1&allowInsecure=1&type=xhttp&host={host}&path={base_path}&mode=auto"
    )
    
    extra_json = json.dumps(extra_data, separators=(",", ":"))
    params += f"&extra={urllib.parse.quote(extra_json)}"
    
    return f"vless://{user}@{address}:443?{params}#{urllib.parse.quote(remark)}"


def run():
    servers = [
        {"name": "ParsaServer", "address": "netlify.parsashonam.sbs:444", "path": "/p4r34m", "user": "Telegram-Parsashonam"},
        {"name": "Xarheon", "address": "https://xarheon.run.place", "path": "/cdn2", "user": "f9b57060-989a-4d6d-bc58-53d767242968"},
 #       {"name": "BEHNAM", "address": "s1.onesrv98.eu.cc:444", "path": "/mine", "user": "a5c04120-8f0d-4d52-8cdd-9ffff79a777d"},
 #       {"name": "Flare", "address": "https://flare.diablo0.site:24855", "path": "/free", "user": "dab65f2a-48ca-4fe8-9143-06cd28f00a21"},
        {"name": "Alwinbalot", "address": "https://solar.latnashobivojod.shop:443", "path": "/jhiuiu", "user": "5cefde6e-867f-452d-8667-d30b01c63050"},
        {"name": "Mostafa", "address": "http://1.gymnation.ir:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Farshid", "address": "http://aa.websooj.site:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
#        {"name": "mohsen", "address": "http://150.241.91.212:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "shabgard", "address": "http://cdn.lindasannp.com:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
#        {"name": "Pouya", "address": "http://76.13.14.51:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
#        {"name": "Masoud", "address": "http://104.234.135.93:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Navid", "address": "https://irnetlify.navtechz.com:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "AbolUp", "address": "http://sub.abolup.online:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Hossein", "address": "http://str.fiathusen.homes:444", "path": "/IR_NETLIFY", "user": "598cbaec-00f6-4d84-8644-b35fdcec6904"},
        {"name": "Saman 2", "address": "https://ppp.sam4.lol:30903", "path": "/asekhi", "user": "132f0ba3-ebbe-4153-84ff-63161b841ed8"},
        {"name": "Ali", "address": "http://185.181.208.92:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        
    ]

    new_snis = ["kubernetes.io", "kueue.sigs.k8s.io", "vuejs.org"]
    new_ips = ["144.76.1.88", "95.216.69.37", "94.130.13.19", "94.130.70.160", "63.141.252.203", "142.54.178.211", "138.201.54.122"]

    old_direct_snis = ["vuejs.org", "kubernetes.io", "letsencrypt.org", "kind.sigs.k8s.io", "kwok.sigs.k8s.io", "krew.sigs.k8s.io", "kueue.sigs.k8s.io", "jobset.sigs.k8s.io", "minikube.sigs.k8s.io", "kustomize.sigs.k8s.io", "cluster-api.sigs.k8s.io", "gateway-api.sigs.k8s.io", "image-builder.sigs.k8s.io", "kubectl.docs.kubernetes.io", "scheduler-plugins.sigs.k8s.io", "secrets-store-csi-driver.sigs.k8s.io"]
    old_combo_snis = ["vuejs.org", "kubernetes.io", "letsencrypt.org", "kind.sigs.k8s.io", "jobset.sigs.k8s.io", "cluster-api.sigs.k8s.io", "gateway-api.sigs.k8s.io"]
    old_ips = ["50.7.5.83", "144.76.1.88", "94.130.50.12", "94.130.33.41", "95.216.69.37", "94.130.13.19", "65.109.34.234", "94.130.70.160", "63.141.252.203", "142.54.178.211", "138.201.54.122"]

    if os.path.exists("domain.txt"):
        with open("domain.txt", "r") as f:
            h_old = f.read().strip()
        if h_old:
            res = [create_vless("Telegram-Parsashonam", s, s, h_old, "/p4r34m", f"🌐 @IR_NETLIFY   {s}") for s in old_direct_snis]
            chosen_old_snis = random.sample(old_combo_snis, min(len(old_combo_snis), 5))
            chosen_old_ips = random.sample(old_ips, min(len(old_ips), 10))
            res.extend([create_vless("Telegram-Parsashonam", ip, s, h_old, "/p4r34m", f"🌐 @IR_NETLIFY  {s}  {ip}") 
                        for s in chosen_old_snis for ip in chosen_old_ips])
            with open("IR_NETLIFY_SUB.txt", "w") as f:
                f.write("\n".join(res))

    if os.path.exists("domain_new.txt"):
        with open("domain_new.txt", "r") as f:
            h_new = f.read().strip()
        if h_new:
            res_new = []
            direct_servers = random.sample(servers, min(len(servers), 3))
            for srv in direct_servers:
                res_new.extend([create_vless(srv["user"], s, s, h_new, srv["path"], f"🌐 @IR_NETLIFY | {s} | {srv['name']}", srv["address"]) 
                                for s in new_snis])

            combo_servers = random.sample(servers, min(len(servers), 8))
            chosen_new_ips = random.sample(new_ips, min(len(new_ips), 5))
            for srv in combo_servers:
                res_new.extend([create_vless(srv["user"], ip, s, h_new, srv["path"], f"🌐 @IR_NETLIFY | {s} | {ip} | {srv['name']}", srv["address"]) 
                                for s in new_snis for ip in chosen_new_ips])

            with open("IR_NETLIFY_SUB_new.txt", "w") as f:
                f.write("\n".join(res_new))


if __name__ == "__main__":
    run()
