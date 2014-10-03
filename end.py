import os

# remove all the rules
os.system('/sbin/iptables -F ACCOUNTING_INCOMING')
os.system('/sbin/iptables -F ACCOUNTING_OUTGOING')
# delete the rules
os.system('/sbin/iptables -D FORWARD -j ACCOUNTING_INCOMING')
os.system('/sbin/iptables -D FORWARD -j ACCOUNTING_OUTGOING')
os.system('/sbin/iptables -D FORWARD -j UPNP')
# delete the chain
os.system('/sbin/iptables -X ACCOUNTING_INCOMING')
os.system('/sbin/iptables -X ACCOUNTING_OUTGOING')
os.system('/sbin/iptables -X UPNP')