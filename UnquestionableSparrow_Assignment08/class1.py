class my_class(object):
    pass

    def __init__(self, name, position, touchdowns=0):
        self.name = name
        self.position = position
        self.touchdowns = touchdowns

    def score_touchdown(self):
        self.touchdowns += 1

    def __str__(self):
        return f"Player(name={self.name}, position={self.position}, touchdowns={self.touchdowns})"

    def __repr__(self):
        return f"Player(name={self.name}, position={self.position}, touchdowns={self.touchdowns})"
