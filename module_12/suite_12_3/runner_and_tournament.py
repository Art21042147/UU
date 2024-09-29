class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        times = {participant.name: self.full_distance / participant.speed
                 for participant in self.participants}

        time_result = sorted(times.items(), key=lambda item: item[1])

        finishers = {i + 1: participant[0] for i, participant in enumerate(time_result)}

        return finishers
