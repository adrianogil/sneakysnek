import time
import enum


class MouseEvents(enum.Enum):
    CLICK = "CLICK"
    MOVE = "MOVE"
    SCROLL = "SCROLL"


class MouseEvent:

    def __init__(self, event, button=None, direction=None, velocity=None, x=None, y=None):
        self.event = event
        self.button = button
        self.direction = direction
        self.velocity = velocity
        self.x = x
        self.y = y
        self.timestamp = time.time()

    def to_json(self):
        return {
            "event_type": "MouseEvent",
            "event_name": self.event.name,
            "button": self.button,
            "direction": self.direction,
            "velocity": self.velocity,
            "x": self.x,
            "y": self.y,
            "timestamp": self.timestamp
        }

    def __str__(self):
        return f"MouseEvent.{self.event.name} - {self.button} - {self.direction} - {self.velocity} - {self.x} - {self.y} - {self.timestamp}"
