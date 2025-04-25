# dns_server.py
from dnslib import DNSRecord, QTYPE, RR, A
from dnslib.server import DNSServer, DNSHandler, BaseResolver, DNSLogger

# from dnslib.server import DNSServer
# from dnslib import A, RR, QTYPE, DNSRecord, DNSLogger, BaseResolver
# class MafiaResolver(BaseResolver):
#     def __init__(self, ip):
#         self.ip = ip
#
#     def resolve(self, request, handler):
#         reply = request.reply()
#         qname = request.q.qname
#         qtype = QTYPE[request.q.qtype]
#
#         print(f"Query: {qname} ({qtype})")
#         
#         if str(qname).endswith("mafia.local."):
#             reply.add_answer(RR(qname, QTYPE.A, rdata=A(self.ip), ttl=60))
#         return reply
#
# def start_dns(hotspot_ip: str):
#     # hotspot_ip = "192.168.137.1"
#     resolver = MafiaResolver(hotspot_ip)
#     logger = DNSLogger(prefix=False)
#     server = DNSServer(resolver, port=8000, address="0.0.0.0", logger=logger)
#
# # Replace with your hotspot IP
#     print(f"Starting DNS server for mafia.local → {hotspot_ip}")
#     server.start()


# Custom DNS resolver
class MafiaResolver(BaseResolver):
    def __init__(self, ip):
        self.ip = ip

    # def resolve(self, request, handler):
    #     reply = request.reply()
    #     qname = request.q.qname
    #     if str(qname).endswith("mafia.local."):
    #         reply.add_answer(RR(qname, QTYPE.A, rdata=A(self.ip), ttl=60))
    #     return reply
    def resolve(self, request, handler):
        reply = request.reply()
        qname = request.q.qname
        print(f"Received request for: {qname}")  # Add logging here
        if str(qname).endswith("mafia.local."):
            reply.add_answer(RR(qname, QTYPE.A, rdata=A(self.ip), ttl=60))
        return reply

# Start DNS in a thread
def start_dns(ip):
    resolver = MafiaResolver(ip)
    dns_server = DNSServer(resolver, port=8053, address="0.0.0.0", logger=DNSLogger())
    print(f"Starting DNS server for mafia.local → {ip}")
    dns_server.start()
