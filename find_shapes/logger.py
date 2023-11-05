"""
logger.py

class Logger:
    abstract logger class

changes:
1.0     2023-11-04      created
1.0.1   2023-11-05      fix: function descriptions

public functions:
    __init__(self)      create a logger
    info(self, text)    log info

"""

from abc import ABC, abstractmethod
import os

class Logger(ABC):
    @abstractmethod
    def __init__(self, file='log.csv', append_existing=False, output_terminal=True, head=''):
        """
        Constructor for the Logger class
        Args:
            file, output file name; None to disable
            append_existing, True to append to existing file, False to start over
            output_terminal, True enables and False disable the terminal output
            head, gets written to the file when opening for the first time
        """
        self.file = file
        self.append_existing = False
        self.output_terminal = output_terminal
        self.head = head
        if self.file:
            if not append_existing:
                with open(self.file, 'w') as file:
                    if head:
                        file.write(head)

    def info(self, text, end='\n'):
        """
        Handle info level logging
        Args:
            text, what to log
            end, get appended at the end of text
        """
        if self.output_terminal:
            print(text)
        if self.file:
            with open(self.file, 'a') as file:
                file.write(text+end)

"""
class ShapeLogger:
    logger class

changes:
1.0     2023-11-04      created

public functions:
    __init__(self)      create a logger
    log_shapes(self, shapes, timestamp)     log shapes

"""


class ShapeLogger(Logger):
    def __init__(self, file='shapes.csv', append_existing=False, output_terminal=True):
        """
        Constructor for the ShapeLogger class
        Args:
            file, output file name; None to disable
            append_existing, True to append to existing file, False to start over
            output_terminal, True enables and False disable the terminal output
        """
        super().__init__(file, append_existing, output_terminal, head='timestamp, shape_kind, shape_color\n')
        self.shapes = []

    def log_shapes(self, shapes, timestamp, keep_radius=100):
        """
        Log various shapes
        Args:
            shapes, various shapes
            timestamp, well, the timestamp
            keep_radius, compares previously passed shapes with newly passed ones and the ones within that
                radius are not logged since they are assumed to have existed already
        """
        for shape in shapes:
            dist = False
            name = False
            color = False
            for existing in self.shapes:
                dist = ((existing.getCenter() - shape.getCenter()).dist() < keep_radius)
                name = (existing.getName() == shape.getName())
                color = (existing.getColor() == shape.getColor())
                if dist and name and color:
                    break
            if not (dist and name and color):
                # new shape found
                super().info(f'{timestamp}, {shape.getName()}, {shape.getColor()}')
        self.shapes = shapes


