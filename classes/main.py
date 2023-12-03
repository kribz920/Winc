# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line
class player():
    def __init__(self, name, speed, endurance, accuracy):
        if endurance or accuracy or speed < 0 or endurance or accuracy or speed > 1:
            raise ValueError("Must be between 0 - 1")
