import os

# create the chains (these only need to happen once)
os.system('/sbin/iptables -N ACCOUNTING_INCOMING')
os.system('/sbin/iptables -N ACCOUNTING_OUTGOING')
os.system('/sbin/iptables -N UPNP')
# send all FORWARD packets to accounting
os.system('/sbin/iptables -I FORWARD -j ACCOUNTING_INCOMING')
os.system('/sbin/iptables -I FORWARD -j ACCOUNTING_OUTGOING')
os.system('/sbin/iptables -A FORWARD -j UPNP')