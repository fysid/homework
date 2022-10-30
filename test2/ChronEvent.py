import datetime


# stors names and date of event
class ChronEvent:
    def __init__(self, date_time: datetime.datetime, name: str):
        self.datetime = date_time
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
        self.events.sort(key=lambda event: event.date_time)

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
        self.required = []
        self.prevents = []

    @property
    def name(self):
        return self.chronicles[0].name

    def require(self, req: ChronIdentity):
        '''
        add requirement identity event for current 
        '''
        self.required.append(req)

    def prevent(self, prev: ChronIdentity):
        '''
        add prevent identity event for current 
        '''
        self.prevents.append(prev)


class Chronology:
    def __init__(self, chronic: Chronicle, identity: ChronIdentity):
        self.chronic = chronic
        self.identity = identity

    def verify(self):
        ''''
        verifying events which wrong with current event
        '''
        # check on existence requirement identity event
        reqcheck = [0] * len(self.identity.required)
        for i, identevents in enumerate(self.identity.required):
            for eachevent in identevents:
                for chronicevents in self.chronic:
                    if eachevent == chronicevents:
                        reqcheck[i] += 1
        # check on existence prevent event
        prevcheck = [0] * len(self.identity.prevents)
        for i, prevent in enumerate(self.identity.prevents):
            for eachevent in prevent:
                for chronicevents in self.chronic:
                    if eachevent == chronicevents:
                        prevcheck[i] += 1
        needevents = []
        # get requirements events
        for i, value in enumerate(reqcheck):
            if value == 0:
                needevents.append(self.identity.required[i])
        errorevents = []
        # get prevents events
        for i, value in enumerate(prevcheck):
            if value > 0:
                errorevents.append(self.identity.prevents[i])
        # check on summury error events
        if len(needevents) + len(errorevents) == 0:
            return True
        # print requirements events
        if len(needevents) > 0:
            print(f"For event {self.identity[0]} we need: ", end='')
            for events in needevents:
                print(events[0], end='')
        # print prevent events
        if len(errorevents) > 0:
            if(errorevents) > 1:
                print(f"event {self.identity[0]} block next events", end='')
            else:
                print(f"event {self.identity[0]} block next event", end='')
            for events in errorevents:
                print(events[0], end='')


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
