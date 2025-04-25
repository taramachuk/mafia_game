import netifaces as ni

def find_ip() -> str:
    hotspot_ip = ''

    interfaces = ni.interfaces()
    print("Available interfaces:", interfaces)

    for iface in interfaces:
        try:
            netia = "{1D86853C-6162-4A36-A424-00B994BC2B13}"
            local = "{1F3FDF89-60DA-4EE4-B725-B2B3215D2CA8}"
            hotspot_name = "ap_br_wlan2"
            addrs = ni.ifaddresses(iface)
            if ni.AF_INET in addrs:
                print(f"Interface {iface} IP:", addrs[ni.AF_INET][0]['addr'])
            
            if iface == hotspot_name:
                hotspot_ip = addrs[ni.AF_INET][0]['addr']
                print("HOTSPOT IP :", hotspot_ip)
            
            # for laptop
            # if iface == local:
            #     print(iface)
            #     print(f"Interface {iface} MAFIA IP:", addrs[ni.AF_INET][0]['addr'])

        except Exception as e:
            print(f"Error on interface {iface}:", e)
        
    return hotspot_ip
