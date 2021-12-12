import datetime
from __future__ import annotations


# stors names and date of event
class ChronEvent:
    def __init__(self, datetime: datetime.datetime, name: str):
        self.datetime = datetime
        self.name = name

    def __str__(self):
        return f"CE - {self.datetime}: {self.name}"


# stors events names
class Chronicle:
    def __init__(self, name: str):
        self.events = []
        self.name = name

    def add(self, chrone_event: ChronEvent):
        '''
        add events in events list
        '''
        self.events.append(chrone_event)
        self.events.sort(key=lambda event: event.datetime)

    def combine(self, other_chronicle: Chronicle):
        '''
        add other cronicle list in current list
        '''
        self.events += other_chronicle.events

    def print(self):
        print(f"Хроника {self.name}:")
        for event in self.events:
            print(f'{event}')


# stors chronicles and events
class Documents:
    def __init__(self):
        self.chronicles = []
        self.events = []

    def attach(self, event, chronicle=None):
        self.events.append(event)
        if chronicle is not None:
            chronicle.add(event)
            self.chronicles.append(chronicle)


# stors identical events
class ChronIdentity:
    def __init__(self, chronicles: tuple):
        self.chronicles = chronicles

    @property
    def name(self):
        return self.chronicles[0].name


def verify(identity1: ChronIdentity, identity2: ChronIdentity, chronicle1: Chronicle, chronicle2: Chronicle):
    chroni = []
    for ident in (identity1, identity2):
        for chronic in (chronicle1, chronicle2):
            for i, name in enumerate(chronic):
                if name == ident.name:
                    chroni.append(i)
                    break

    if len(chroni) != 4:
        print('N/A')
    else:
        if ((chroni[0] >= chroni[2]) and (chroni[1] >= chroni[3])) or ((chroni[0] < chroni[2]) and (chroni[1] < chroni[3])):
            print('Ok')
        else:
            print('Not ok')
