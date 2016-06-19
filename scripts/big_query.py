#!/usr/bin/python
from __future__ import print_function
import os, json, requests, sys, time
from pprint import pprint

def usage():
	print("%s: ip_address ascan " % os.path.basename(sys.argv[0]) )
	print("      ip_address is the IP address of the BIG(Bluetooth Internet Gateway)")
	print("      pscan  specifies doing a passive scan")
	print("      hrate  - shows heart rate monitors")
	print("      hrate_all  - shows heart rate monitors and all it's service and characteristics")
	print("      hrate service_uuid characteristics_uuid  - Reads data from heart monitor's")
	print("            specified service_uuid and characteristics_uuid")
	
def printf(str, *args):
    print(str % args, end='')


def get_href(node):
	return node["self"]["href"]

def print_scan_node(n):
	printf ("%50s %20s %10s %5s", n["self"]["href"], n["bdaddr"], n["bdaddrType"], n["rssi"])
	ad = n["AD"]
	for a in ad:
		printf(" (%s %s) ", a["ADType"], a["ADValue"])
	printf("\n")


def print_characteristics_node(n):
	#printf ("%50s %20s %10s %5s\n", n["self"]["href"], n["uuid"], n["handle"])
	printf ("%90s %10s %10s\n", n["self"]["href"], n["uuid"],n["properties"] )

def print_characteristics_nodes(nodes):
	if not nodes:
		return
	printf ("%90s %10s %10s\n", "href", "uuid","properties")
	for n in nodes:
		print_characteristics_node(n)


def print_service_node(n):
	#printf ("%50s %20s %10s %5s\n", n["self"]["href"], n["uuid"], n["handle"])
	printf ("%60s %10s\n", n["self"]["href"], n["uuid"])

def print_service_nodes(nodes):
	printf ("%60s %10s\n", "service_href", "uuid")
	for n in nodes:
		print_service_node(n)


def print_scan_data(json_data):
	duplicate_cnt=0;
	data = json.loads(json_data)
	#pprint(data)
	prev_href=""
	nodes_t = data["nodes"]
	#pprint(nodes_t)
	nodes = sorted(nodes_t, key=get_href)
	#pprint(nodes[0])
	printf ("%50s %20s %10s %5s %20s \n", "href", "bdaddr", "bdaddrType", "rssi", "(ADType, ADValue)")
	for n in nodes:
		href = get_href(n)
		if href ==  prev_href:
			duplicate_cnt = duplicate_cnt + 1;
		else:
			duplicate_cnt = 0
			print_scan_node(n)
		prev_href = href

def print_scan_nodes(nodes):
	printf ("%50s %20s %10s %5s %20s \n", "href", "bdaddr", "bdaddrType", "rssi", "(ADType, ADValue)")
	for n in nodes:
		print_scan_node(n)


def get_scan_data(json_data):
	duplicate_cnt=0;
	data = json.loads(json_data)
	#pprint(data)
	prev_href=""
	nodes_t = data["nodes"]
	#pprint(nodes_t)
	nodes = sorted(nodes_t, key=get_href)
	nodes_r = []
	#pprint(nodes[0])
	for n in nodes:
		href = get_href(n)
		if href ==  prev_href:
			duplicate_cnt = duplicate_cnt + 1;
		else:
			nodes_r.append(n)
		prev_href = href
	#print(nodes_r)
	return nodes_r

def get_services_data(json_data):
	duplicate_cnt=0;
	data = json.loads(json_data)
	#pprint(data)
	prev_href=""
	nodes_t = data["services"]
	#pprint(nodes_t)
	nodes = sorted(nodes_t, key=get_href)
	nodes_r = []
	#pprint(nodes[0])
	for n in nodes:
		href = get_href(n)
		if href ==  prev_href:
			duplicate_cnt = duplicate_cnt + 1;
		else:
			nodes_r.append(n)
		prev_href = href
	#print(nodes_r)
	return nodes_r

def get_charectristics_data(json_data):
	duplicate_cnt=0;
	data = json.loads(json_data)
	#pprint(data)
	prev_href=""
	nodes_t = data["characteristics"]
	#pprint(nodes_t)
	nodes = sorted(nodes_t, key=get_href)
	nodes_r = []
	#pprint(nodes[0])
	for n in nodes:
		href = get_href(n)
		if href ==  prev_href:
			duplicate_cnt = duplicate_cnt + 1;
		else:
			nodes_r.append(n)
		prev_href = href
	#print(nodes_r)
	return nodes_r

def get_nodes_with_uuid(nodes, uuid):
	nodes_r = []
	for n in nodes:
		if n["uuid"] == uuid:
			nodes_r.append(n)
	return nodes_r


def get_characteristics_nodes_with_uuid(nodes, uuid):
	nodes_r = []
	for n in nodes:
		if n["uuid"] == uuid:
			nodes_r.append(n)
	return nodes_r


def get_heart_rate_nodes(nodes):
	nodes_r = []
	for n in nodes:
		ad = n["AD"]
		for a in ad:
			if "180D" in a["ADValue"]:
				nodes_r.append(n)
	return nodes_r


def http_operation(url, op="get"):
	#printf("url=%s op=%s\n", url, op)
	try:
		if op == "put":
			#printf("Doing put:\n")
			r = requests.put(url)
		else:
			r = requests.get(url)
	except requests.exceptions.Timeout:
		printf("ERROR: request=%s Timeout", r.status_code, url)
	except requests.exceptions.TooManyRedirects:
		printf("ERROR: BADURL request=%s ", url)
	except requests.exceptions.RequestException as e:
		printf("ERROR: Possibly specified wrong url=%s\n", url)
		#printf("Exception=%s\n", e)
		printf("Here ##############\n")
		return None
	#print(r.text)
	return r.text

def wiced_get_active_scan_data(ipaddr):
	url='http://%s/gap/nodes?active=1' % (ipaddr)
	return http_operation(url)

def wiced_get_passive_scan_data(ipaddr):
	url='http://%s/gap/nodes?passive=1' % (ipaddr)
	return http_operation(url)

def wiced_connect_handle(url_handle):
	url='%s?connect=1' % (url_handle)
	r = http_operation(url,"put")
	return r
	#print(r)

def wiced_discover_handle(url_handle):
	url_handle = url_handle.replace("gap","gatt")
	url='%s/services?primary=1' % (url_handle)
	r = http_operation(url)
	return r
	#print(r)

def wiced_discover_characteristics_handle(url_handle):
	url='%s/characteristics' % (url_handle)
	r = http_operation(url)
	return r

def wiced_cnode_notify_indicate(url_handle):
	url='%s?notify=1' % (url_handle)
	r = http_operation(url)
	url='%s?indicate=1' % (url_handle)
	r = http_operation(url)
	return r

def wiced_cnode_get_value(url_handle):
	url='%s/value?notify=1&event=1' % (url_handle)
	r = http_operation(url)
	print(r)
	url='%s/value?indicate=1&event=1' % (url_handle)
	r = http_operation(url)
	print(r)
	return r


def test_print_active_scan_data():
	json_data = open("active_scan.log").read()
	print_active_scan_data(json_data)


if (len(sys.argv) < 3) :
    usage()
    sys.exit(0)

if (sys.argv[2] == "ascan"):
	wiced_get_active_scan_data(sys.argv[1])
elif (sys.argv[2] == "pscan"):
	json_text= wiced_get_passive_scan_data(sys.argv[1])
	nodes = get_scan_data(json_text)
	print_scan_nodes(nodes)
	print("===== Heart Rate Mointors ======")
	nodesh = get_heart_rate_nodes(nodes)
	print_scan_nodes(nodesh)
elif (sys.argv[2] == "hrate"):
	json_text= wiced_get_passive_scan_data(sys.argv[1])
	nodes = get_scan_data(json_text)
	print("\t\t\t\t\t\t\t ===== Heart Rate Mointors ======             ")
	nodesh = get_heart_rate_nodes(nodes)
	print_scan_nodes(nodesh)
elif (sys.argv[2] == "hrate_all"):
	json_text= wiced_get_passive_scan_data(sys.argv[1])
	nodes = get_scan_data(json_text)
	print("\t\t\t\t\t\t\t ===== Heart Rate Mointors ======             ")
	nodesh = get_heart_rate_nodes(nodes)
	print_scan_nodes(nodesh)
	time.sleep(2)
	for n in nodesh:
		r = wiced_connect_handle(n["self"]["href"])
		#print(r)
		services_text = wiced_discover_handle(n["self"]["href"])
		services_nodes = get_services_data(services_text)
		#pprint(services_nodes)
		print_service_nodes(services_nodes)
		for s in services_nodes:
			characteristics_text = wiced_discover_characteristics_handle(s["self"]["href"])
			#print(characteristics_text)
			characteristics_nodes = get_charectristics_data(characteristics_text)
			printf("characteristics for=%s uuid=%s\n", s["self"]["href"], s["uuid"])
			print_characteristics_nodes(characteristics_nodes)
elif (sys.argv[2] == "hrate_get"):
	if (len(sys.argv) < 5) :
		usage()
		sys.exit(0)
	service_uuid = sys.argv[3]
	char_uuid = sys.argv[4]
	json_text= wiced_get_passive_scan_data(sys.argv[1])
	nodes = get_scan_data(json_text)
	nodesh = get_heart_rate_nodes(nodes)
	for n in nodesh:
		r = wiced_connect_handle(n["self"]["href"])
		#print(r)
		stext = wiced_discover_handle(n["self"]["href"])
		snodes = get_services_data(stext)	
		snodes_uuid = get_nodes_with_uuid(snodes, service_uuid)
		for s in snodes:
			characteristics_text = wiced_discover_characteristics_handle(s["self"]["href"])
			#print(characteristics_text)
			cnodes = get_charectristics_data(characteristics_text)
			cnodes_uuid = get_nodes_with_uuid(cnodes, char_uuid)
			print_characteristics_nodes(cnodes_uuid)
			for c in cnodes_uuid:
				wiced_cnode_notify_indicate(c["self"]["href"])
				#for i in range(20):
				#	wiced_cnode_get_value(c["self"]["href"])
				#	time.sleep(1)
else:
	usage()


