import socket 
def get_Host_name_IP():
	try:
		host_name = socket.gethostname()
		host_ip = socket.gethostbyname(host_name)
		print('Hostname : ' ,host_name)
		print("IP : ", Host_ip)

	except: 
		print('Unable to get Hostname IP')

get_Host_name_IP()