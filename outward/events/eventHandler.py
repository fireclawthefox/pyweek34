import random
import csv
import os
from events.eventBase import EventBase

class EventHandler:
    def __init__(self):
        self.registered_events = []

        csv_file = os.path.join(base.main_dir, "events", "events.csv")
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.registered_events.append(EventBase(row))
        # time until the next event happens
        self.next_event_time = 0
        self.set_next_event_time()

        # current time of the event manager, to check if a new event should happen
        self.current_time = 0

    def set_next_event_time(self):
        # every few minutes an event will happen
        self.next_event_time = random.uniform(2*60, 5*60)

    def check_events(self, economy_stats_list):
        dt = globalClock.get_dt()
        self.current_time += dt

        if self.current_time >= self.next_event_time:
            event = random.choice(self.registered_events)
            event.do(economy_stats_list)
            self.set_next_event_time()
            self.current_time = 0
