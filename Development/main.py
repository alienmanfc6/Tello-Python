# docs https://www.ryzerobotics.com/tello/downloads

# something of note: if no commands are sent for 15 seconds the drone will land.
# we will need some sort of "keep-alive" ping. something like get battery level
# would be good since we'll want to keep tabs on that anyway

from tello import Tello

tello = Tello()

print('\r\n\r\nTello Python3 Demo.\r\n')

print('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print('end -- quit demo.\r\n')

# start SDK mode
tello.send_command("command")

while True:

    try:
        command = input("")

        if not command:
            break

        if 'end' in command:
            print('Landing and closing connection to drone...')
            tello.on_close()
            break

        # Send data
        commandResult = tello.send_command(command)
        if commandResult == "ok":
            print("OK")
        elif commandResult == "error":
            print("Error")

    except KeyboardInterrupt:
        print('\n . . .\n')
        tello.on_close()
        break
