import socket
import threading


class Tello:
    def __init__(self):
        self.local_ip = ''
        self.local_port = 8889
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind((self.local_ip, self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = '192.168.10.1'
        self.tello_port = 8889
        self.tello_adderss = (self.tello_ip, self.tello_port)

    def send_command(self, command):
        print('sending command: %s to %s' % (command, self.tello_ip))
        return self.socket.sendto(command.encode('utf-8'), self.tello_adderss)

    def _receive_thread(self):
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print('from %s: %s' % (ip, self.response))
            except socket.error as exc:
                print("Caught exception socket.error : %s" % exc)

    def on_close(self):
        pass
        # for ip in self.tello_ip_list:
        #     self.socket.sendto('land'.encode('utf-8'), (ip, 8889))
        # self.socket.close()

    def takeOff(self):
        return self.send_command("takeoff")

    def land(self):
        return self.send_command("land")

    def goUp(self, distance):
        move(self, "up", distance)

    def goDown(self, distance):
        move(self, "down", distance)

    def connectToWifi(self):
        # long press the power button for 5 seconds to reset to adhock mode
        return self.send_command("wifi BCubed_FL_2G bellabella")

    def getBattery(self):
        return self.send_command("battery?")

    def getHeight(self):
        return self.send_command("height?")

    # move in a direction a set distance
    def move(self, direction, distance):
        if 20 < distance < 500:
            return self.send_command(direction + " " + distance)
        else:
            print("Movment out-of-bounds")
