class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name = name
        self.speed = speed
        self.flyTime = flyTime
        self.restTime = restTime
        self.flyCount = flyTime
        self.restCount = restTime
        self.state = "fly"
        self.distance = 0
        self.points = 0
    
    def action(self):
        if self.state == "fly":
            self.travel()
        else:
            self.rest()
    
    def travel(self):
        self.distance += self.speed
        if self.flyCount == 1:
            self.flyCount = self.flyTime
            self.state = "rest"
        else:
            self.flyCount -= 1
    
    def rest(self):
        if self.restCount == 1:
            self.restCount = self.restTime
            self.state = "fly"
        else:
            self.restCount -= 1
    
    def __lt__(self, other):
         return self.points < other.points



def race(text, rounds):
    # Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
    reindeers = []
    with open(text, 'r') as file:
        descriptions = file.readlines()
    for description in descriptions:
        description = description.split(" ")
        reindeers.append(Reindeer(description[0], int(description[3]), int(description[6]), int(description[-2])))
    for _ in range(rounds):
        maxDistance = 0
        for reindeer in reindeers:
            reindeer.action()
            maxDistance = reindeer.distance if reindeer.distance > maxDistance else maxDistance
        for reindeer in reindeers:
            if reindeer.distance == maxDistance:
                reindeer.points += 1
    
    reindeers.sort()
    return reindeers[-1].points

if __name__ == "__main__":
    print(race("input.txt", 2503))