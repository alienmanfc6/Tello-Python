from tello import Tello
from datetime import datetime
import time

start_time = str(datetime.now())

commands = ["battery?", "delay 5", "height?"]

print("Tello booting up...")
tello = Tello()
time.sleep(2)
tello.send_command("command")
time.sleep(2)

for command in commands:
    if command != '' and command != '\n':
        command = command.rstrip()

        if command.find('delay') != -1:
            sec = float(command.partition('delay')[2])
            tello.hold(sec)
            pass
        else:
            tello.send_command(command)

# print all logs at end of program
# log = tello.get_log()
#
# for stat in log:
#     stat.print_stats()

