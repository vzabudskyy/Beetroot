"""
Task 3

TV controller

Create a simple prototype of a TV controller in Python. It’ll use the following commands:

first_channel() - turns on the first channel from the list.
last_channel() - turns on the last channel from the list.
turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
current_channel() - returns the name of the current channel.
is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or 'name'
exists in the list, or "No" - in the other case.


The default channel turned on before all commands is №1.

Your task is to create the TVController class and methods described above.

```

CHANNELS = ["BBC", "Discovery", "TV1000"]

 class TVController:

pass

 controller = TVController(CHANNELS)

controller.first_channel() == "BBC"

controller.last_channel() == "TV1000"

controller.turn_channel(1) == "BBC"

controller.next_channel() == "Discovery"

controller.previous_channel() == "BBC"

controller.current_channel() == "BBC"

controller.is_exist(4) == "No"

controller.is_exist("BBC") == "Yes"

```
"""


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.temp_channel = channels[0]

    def first_channel(self):
        self.temp_channel = 0
        return self.channels[self.temp_channel]

    def last_channel(self):
        self.temp_channel = -1
        return self.channels[self.temp_channel]

    def turn_channel(self, channel_number):
        self.temp_channel = channel_number-1
        return self.channels[self.temp_channel]

    def next_channel(self):
        self.temp_channel = (self.temp_channel + 1) % len(self.channels)
        return self.channels[self.temp_channel]

    def previous_channel(self):
        self.temp_channel = (self.temp_channel - 1) % len(self.channels)
        return self.channels[self.temp_channel]

    def current_channel(self):
        return self.channels[self.temp_channel]

    def is_exist(self, channel):
        if (type(channel) == int and (channel - 1) < len(self.channels)) or channel in self.channels:
            return "Yes"
        else:
            return "No"


if __name__ == "__main__":
    CHANNELS = ["BBC", "Discovery", "TV1000"]
    controller = TVController(CHANNELS)
    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("BBC") == "Yes"
