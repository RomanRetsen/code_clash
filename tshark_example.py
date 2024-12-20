import pyshark

all_packets = pyshark.FileCapture('happy.pcap')
# capture = pyshark.LiveCapture(interface="wlo1")
# capture.sniff(timeout=5)
# print(cap[0])
# cap.load_packets()
# num = len(cap)
# for i in range(0, 10):
#     print(cap[i])
# for number, pkg in enumerate(cap):
#     print(f"{number} {pkg}")
i = 0
for packet in all_packets:
    if not i == 10:
        print(packet.layers)
    else:
        break
    i += 1