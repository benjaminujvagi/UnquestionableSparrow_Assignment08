class my_class(object):
    pass

    def __init__(self, name, position, touchdowns=0):
        self._name = name
        self._position = position
        self._touchdowns = touchdowns

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def touchdowns(self):
        return self._touchdowns

    @touchdowns.setter
    def touchdowns(self, value):
        if value >= 0:
            self._touchdowns = value
        else:
            raise ValueError("Points can't be negative")

    def score_touchdown(self):
        self._touchdowns += 1

    def __str__(self):
        return f"Player(name={self._name}, position={self._position}, touchdowns={self._goals})"

    def __repr__(self):
        return f"Player(name={self._name}, position={self._position}, touchdowns={self._goals})"


