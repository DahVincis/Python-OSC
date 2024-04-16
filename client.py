from pythonosc import udp_client

X32_IP_ADDRESS = '192.168.56.1'  # IP address of X32 mixer
X32_OSC_PORT = 10023

client = udp_client.SimpleUDPClient(X32_IP_ADDRESS, X32_OSC_PORT)

client.send_message('/xinfo', None)
client.send_message('/ch/01/eq/2/q', [0.5])