# dns_server.py
from dnslib import DNSRecord, QTYPE, RR, A
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger

class MafiaResolver(BaseResolver):
    def __init__(self, ip):
        self.ip = ip

    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        qtype = QTYPE[request.q.qtype]

        print(f"Query: {qname} ({qtype})")
        
        if str(qname).endswith("mafia.local."):
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(self.ip), ttl=60))
        return reply

# Replace with your hotspot IP
hotspot_ip = "192.168.137.1"
resolver = MafiaResolver(hotspot_ip)
logger = DNSLogger(prefix=False)
server = DNSServer(resolver, port=53, address="0.0.0.0", logger=logger)

print(f"Starting DNS server for mafia.local → {hotspot_ip}")
server.start()

