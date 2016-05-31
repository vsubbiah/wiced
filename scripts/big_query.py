#!/usr/bin/python
from __future__ import print_function
import os, json, requests, sys
from pprint import pprint

def usage():
   print("%s: ip_address ascan " % os.path.basename(sys.argv[0]) )
   print("      ip_address is the IP address of the BIG(Bluetooth Internet Gateway)")
   print("      ascan  specifies doing an active scan")

def printf(str, *args):
    print(str % args, end='')


def get_href(node):
	return node["self"]["href"]

def print_active_scan_data(json_data):
	duplicate_cnt=0;
	data = json.loads(json_data)
	pprint(data)
	prev_href=""
	nodes_t = data["nodes"]
	nodes = sorted(nodes_t, key=get_href)
	printf ("%50s %20s %10s %5s %20s \n", "href", "bdaddr", "bdaddrType", "rssi", "(ADType, ADValue)")
	for n in nodes:
		href = get_href(n)
		if href ==  prev_href:
			duplicate_cnt = duplicate_cnt + 1;
		else:
			printf ("%50s %20s %10s %5s", n["self"]["href"], n["bdaddr"], n["bdaddrType"], n["rssi"])
			duplicate_cnt = 0
			ad = n["AD"]
			for a in ad:
				printf(" (%s %s) ", a["ADType"], a["ADValue"])
			printf("\n")
		prev_href = href
		

def wiced_get_active_scan_data(ipaddr):
	url='http://%s/gap/nodes?active=1' % (ipaddr)
	try:
		r = requests.get(url)
	except requests.exceptions.Timeout:
		printf("ERROR: request=%s Timeout", r.status_code, url)
	except requests.exceptions.TooManyRedirects:
		printf("ERROR: BADURL request=%s ", url)
	except requests.exceptions.RequestException as e:
		printf("ERROR: Possibly specified wrong IP=%s\n", ipaddr)
		printf("Exception=%s\n", e)
		return
	print_active_scan_data(r.text)

def test_print_active_scan_data():
	json_data = open("active_scan.log").read()
	print_active_scan_data(json_data)


if (len(sys.argv) < 3) :
    usage()
    sys.exit(0)

if (sys.argv[2] == "ascan"):
	wiced_get_active_scan_data(sys.argv[1])
else:
	usage()


