from datetime import datetime


class Stats:
    def __init__(self, command, id):
        self.command = command
        self.response = None
        self.id = id

        self.start_time = datetime.now()
        self.end_time = None
        self.duration = None

    def add_response(self, response):
        self.response = response
        self.end_time = datetime.now()
        self.duration = self.get_duration()
        self.print_stats()

    def get_duration(self):
        diff = self.end_time - self.start_time
        return diff.total_seconds()

    def print_stats(self):
        print('\nLog id: %s' % self.id)
        print('Command: %s' % self.command)
        print('Response: %s' % self.response)

    def got_response(self):
        if self.response is None:
            return False
        else:
            return True

    def return_stats(self):
        log = ''
        log += '\nid: %s\n' % self.id
        log += 'command: %s\n' % self.command
        log += 'response: %s\n' % self.response
        log += 'start time: %s\n' % self.start_time
        log += 'end_time: %s\n' % self.end_time
        log += 'duration: %s\n' % self.duration
        return log
