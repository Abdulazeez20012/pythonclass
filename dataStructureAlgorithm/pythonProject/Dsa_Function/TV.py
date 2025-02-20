class TV:
    def __init__(self):
        self.power_status = False
        self.volume = 0
        self.channel = 1
    def is_switched_off(self):
        self.power_status = True

    def turn_on(self):
        self.power_status = True

    def turn_off(self):
        self.power_status = False

    def increase_volume(self):
        if self.power_status and self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.power_status and self.volume > 0:
            self.volume -= 1

    def change_channel(self, new_channel):
        if self.power_status:
            if new_channel < 1 :
                raise ValueError("Channel number must be greater than 0")
            if self.power_status:
             if  self.channel > 100:
                raise ValueError("channel cannot be greater than 100")
            self.channel = new_channel

    def mute(self):
        if self.power_status:
            self.volume = 0

    def unmute(self):
        if self.power_status:
            self.volume = 1

    def remain_instate(self):
        if self.power_status:
            self.volume = 1