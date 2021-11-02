from scapy.all import *

SYNACK = 0x12
RSTACK = 0x14

def check_host(ip):
    pass

# def scan_port(target, port):
def scan_port(host, dst_port):

    # src_port = RandShort()
    # conf.verb
    # syn_ack_pck = sr1(IP(dst=target)/TCP(sport=src_port, dport=port, flags="S"), timeout=3, verbose=0)
    # pkt_flags = syn_ack_pck.getlayer(TCP).flags
    # if pkt_flags == SYNACK:
    #     return True
    # else:
    #     return False
    # rst_pck = IP(dst=target)/TCP(sport=src_port, dport=port, flags="R")
    # send(rst_pck)
    src_port = random.randint(1025, 65534)
    resp = sr1(
        IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags="S"), timeout=1,
        verbose=0,
    )
    if resp is None:
        print(f"{host}:{dst_port} is filtered (silently dropped).")

    elif (resp.haslayer(TCP)):
        if (resp.getlayer(TCP).flags == 0x12):
            send_rst = sr(
                IP(dst=host) / TCP(sport=src_port, dport=dst_port, flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{host}:{dst_port} is open.")

        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{host}:{dst_port} is closed.")

    elif (resp.haslayer(ICMP)):
        if (
                int(resp.getlayer(ICMP).type) == 3 and
                int(resp.getlayer(ICMP).code) in (1, 2, 3, 9, 10, 13)
        ):
            print(f"{host}:{dst_port} is filtered (silently dropped).")

target_ip = input("Enter IP:>> ")
min_port = int(input("Enter starting port:>> "))
max_port = int(input("Enter ending port:>> "))

for port in range(min_port, max_port + 1, 1):
    print(f"testing {port}...")
    status = scan_port(target_ip, port)
    if status == True:
        print(port)
        # print(f"Port {port} is open on host: {target_ip}")