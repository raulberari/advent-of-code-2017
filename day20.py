import operator
import re


class Particle:
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.distanceFromOrigin = abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def getVelocity(self):
        return self.velocity

    def setVelocity(self, velocity):
        self.velocity = velocity

    def getAcceleration(self):
        return self.acceleration

    def getDistanceFromOrigin(self):
        return self.distanceFromOrigin

    def moveOnce(self):
        self.velocity[0] += self.acceleration[0]
        self.velocity[1] += self.acceleration[1]
        self.velocity[2] += self.acceleration[2]
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

        self.distanceFromOrigin = abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def __str__(self):
        return (
            "Position: " + str(self.position) +
            "\nVelocity: " + str(self.velocity) +
            "\nAcceleration: " + str(self.acceleration) +
            "\nDistance from origin: " + str(self.distanceFromOrigin) +
            "\n"
        )


def printParticles():
    for particle in particles:
        print(str(particles.index(particle)) + "\n" + str(particle))


particles = []
distances = []
half = "first"

with open("day20.txt") as readFile:
    lines = readFile.readlines()
    for line in lines:
        line = re.sub(r'[=<>a-z \n]', '', line)

        args = line.split(',')

        args = [int(arg) for arg in args]
        position = [args[0], args[1], args[2]]
        velocity = [args[3], args[4], args[5]]
        acceleration = [args[6], args[7], args[8]]

        particle = Particle(position, velocity, acceleration)
        particles.append(particle)
        distances.append(particle.getDistanceFromOrigin())

    if half == "first":
        for tick in range(1000):
            for particle in particles:
                particle.moveOnce()

        closestParticle = min(particles, key=lambda particle: particle.getDistanceFromOrigin())
        print(particles.index(closestParticle))
        print(closestParticle)

    elif half == "second":
        for tick in range(100):
            for particle in particles:
                particle.moveOnce()
            positions = [particle.getPosition() for particle in particles]
            positions = [position for position in positions if positions.count(position) == 1]
            particles = [particle for particle in particles if particle.getPosition() in positions]
        print(len(particles))
