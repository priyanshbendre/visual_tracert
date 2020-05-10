
import os #tracert OS command
import re #ip address from tracert file
import ipinfo #ip to geolocation API call
import gmplot #render route on gmaps

def parse_ip_add():
	ip_content = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", input_str) # re to find all ips
	ip_list = [] #list of all IP addresses
	for x in ip_content:
		if x not in ip_list:
			ip_list.append(x)
	return ip_list


def print_map(latitude,longitude):
	gmap3 = gmplot.GoogleMapPlotter(latitude[0],longitude[0], 5) #map open location and zoom level

	gmap3.scatter(latitude,longitude, '#FF0000',size = 75, marker = False )
	gmap3.plot(latitude,longitude, 'cornflowerblue', edge_width = 3.0)
	gmap3.draw("output_packet_route.html")
	print("Map generated!")


if __name__ == '__main__':
	# New Tracert command OS
	print("Traceroute running. This could take several minutes. Please wait...")
	stream = os.popen("traceroute google.com")
	output = stream.read()
	save_to_file = open("terminal_output.txt","w+")
	save_to_file.write(output)
	save_to_file.seek(0)
	input_str = save_to_file.read()


	# Hide below code segment if running OS tracert
	# input_from_file = open("terminal_output.txt")
	# input_str = input_from_file.read()


	ip_list = parse_ip_add()


	access_token = "API_ACCESS_TOKEN_HERE"
	handler = ipinfo.getHandler(access_token)
	latitude = []
	longitude =[]
	for x in ip_list:
		details = handler.getDetails(x)
		try:
			details.bogon
		except Exception as e:
			# IP to location Name
			# print(details.city)
			# IP to lat, lon
			latitude.append(float(details.latitude))
			longitude.append(float(details.longitude))


	print_map(latitude,longitude)


	# input_from_file.close()
	save_to_file.close()