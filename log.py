import os,re,time,MySQLdb

# read all the existing data

# get the update time
update_time = time.time()
macs = {}
in_bytes = {}
out_bytes = {}

# read incoming
ignore_rows = 2;
in_data = os.popen('/sbin/iptables -L ACCOUNTING_INCOMING -n -v -x')
for in_rule in in_data.readlines():
	if (ignore_rows <= 0):
		components = re.split('\s*',in_rule)
		bytes = components[2]
		ip = components[8]
		in_bytes[ip] = bytes
		
		arp_info = os.popen('/usr/sbin/arp ' + ip)
		for arp_line in arp_info.readlines():
			arp_components = re.split('\s*',arp_line)
			mac = arp_components[2]
		
		macs[ip] = mac
		# print bytes + ' bytes from ' + ip + ' with mac address ' + mac
		# print components
	ignore_rows = ignore_rows - 1

# read outgoing
ignore_rows = 2;
out_data = os.popen('/sbin/iptables -L ACCOUNTING_OUTGOING -n -v -x')
for out_rule in out_data.readlines():
	if (ignore_rows <= 0):
		components = re.split('\s*',out_rule)
		bytes = components[2]
		ip = components[7]
		out_bytes[ip] = bytes
		
		# print bytes + ' bytes from ' + ip
		# print components
	ignore_rows = ignore_rows - 1

# store all the data
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="bandwidth_logging")
cursor = db.cursor()
for ip in macs.keys():
	sql = "INSERT INTO log (log_time, ip, mac, in_bytes, out_bytes) VALUES (FROM_UNIXTIME(%s), '%s', '%s', %s, %s)" % (update_time, ip, macs[ip], in_bytes[ip], out_bytes[ip])
	cursor.execute(sql)

# remove all the rules
os.system('/sbin/iptables -F ACCOUNTING_INCOMING')
os.system('/sbin/iptables -F ACCOUNTING_OUTGOING')

# add rules for all active MAC addresses
addresses = os.popen('/usr/sbin/arp -a | /usr/bin/awk \'$7 == "eth2" {print $2}\' | /bin/sed -e \'s/[()]//g\'')
for address in addresses.readlines():
	os.system('/sbin/iptables -A ACCOUNTING_INCOMING --dst ' + address)
	os.system('/sbin/iptables -A ACCOUNTING_OUTGOING --src ' + address)