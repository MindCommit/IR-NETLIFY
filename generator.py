import os
import json
import urllib.parse
import random


def create_vless(user, address, sni, host, path, remark, x_host=None):
    base_path = urllib.parse.quote(path, safe="")
    
    extra_data = {
        "xPaddingBytes": "1-1",
        "xPaddingObfsMode": True,
        "scMaxEachPostBytes": "1000000",
        "xPaddingKey": "iran",
        "xPaddingHeader": "iran",
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
        {"name": "Xarheon", "address": "https://xarheon.run.place", "path": "/cdn2", "user": "f9b57060-989a-4d6d-bc58-53d767242968"},
        {"name": "BEHNAM", "address": "https://s1.onesrv98.eu.cc:444", "path": "/mine", "user": "a5c04120-8f0d-4d52-8cdd-9ffff79a777d"},
        {"name": "Saman 1", "address": "http://pa.sam4.lol:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Alwinbalot", "address": "http://46.8.229.114:444", "path": "/balot", "user": "%40IR_NETLIFY"},
        {"name": "Mostafa", "address": "http://1.gymnation.ir:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Farshid", "address": "http://aa.websooj.site:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "mohsen", "address": "http://cdn.lindasannp.com:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Ali", "address": "http://185.181.208.92:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "shabgard", "address": "http://cdn.lindasannp.com:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Saman 2", "address": "https://ppp.sam4.lol:30903", "path": "/asekhi", "user": "132f0ba3-ebbe-4153-84ff-63161b841ed8"},
        {"name": "Pouya", "address": "http://76.13.14.51:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Masoud", "address": "http://104.234.135.93:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Navid", "address": "https://irnetlify.navtechz.com:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "AbolUp", "address": "http://sub.abolup.online:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Hossein", "address": "http://str.fiathusen.homes:444", "path": "/IR_NETLIFY", "user": "598cbaec-00f6-4d84-8644-b35fdcec6904"},
        {"name": "DarkSoul", "address": "http://89.22.236.213:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
        {"name": "Meshke", "address": "https://meshke.imissher.shop:444", "path": "/meshke", "user": "6ff4e855-cb98-47aa-901c-b787c898b6bb"},
        {"name": "Rahgozar", "address": "https://s1.rahgozar.tr:444", "path": "/xhttp444", "user": "c18d7142-3adc-491a-a0af-518a67d21c19"},
        {"name": "Dante", "address": "http://212.74.39.210:444", "path": "/IR_NETLIFY", "user": "%40IR_NETLIFY"},
    ]

    new_snis = ["kubernetes.io", "kueue.sigs.k8s.io", "vuejs.org"]
    new_ips = ["144.76.1.88", "95.216.69.37", "94.130.13.19", "94.130.70.160", "63.141.252.203", "142.54.178.211", "138.201.54.122"]

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
