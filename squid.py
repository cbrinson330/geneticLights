from random import (choice, random, randint)
import datetime
import cv2 as cv2
import numpy as np
from PIL import Image
from nanpy import (ArduinoApi, SerialManager)
from time import sleep

faceCascade = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

__all__ = ['Chromosome', 'Population']

class Chromosome:
    
    def __init__(self, gene):
        self.gene = gene
        self.fitness = 0

    def getGene(self):
        return self.gene

    def mate(self, mate):
        """
        Method used to mate the chromosome with another chromosome, 
        resulting in a new chromosome being returned.
        """
        pivot = randint(0, len(self.gene) - 1)
        gene1 = self.gene[:pivot] + mate.gene[pivot:]
        gene2 = mate.gene[:pivot] + self.gene[pivot:]
        
        return Chromosome(gene1), Chromosome(gene2)

    def mutate(self):
        """
        Method used to generate a new chromosome based on a change in a 
        random character in the gene of this chromosome.  A new chromosome 
        will be created, but this original will not be affected.
        """
        g = self.gene
        for i in range(10):
						pinNo = randint(0, 11)
						time = randint(0,19)
						val = randint(0,1)
						g[pinNo][time] = val
							
        return Chromosome(g)
        
    @staticmethod
    def gen_random():
        """
        A convenience method for generating a random chromosome with a random
        gene.
        """
        gene = []
        for x in range(12):
						pins = []
						for x in range(20):
								pins.append(randint(0,1))
						gene.append(pins)
        return Chromosome(gene)

        
class Population:
    """
    A class representing a population for a genetic algorithm simulation.
    
    A population is simply a sorted collection of chromosomes 
    (sorted by fitness) that has a convenience method for evolution.  This
    implementation of a population uses a tournament selection algorithm for
    selecting parents for crossover during each generation's evolution.
    
    Note that this object is mutable, and calls to the evolve()
    method will generate a new collection of chromosome objects.
    """
    
    _tournamentSize = 3
    
    def __init__(self, size=60, crossover=0.8, elitism=0.1, mutation=0.03):
        self.elitism = elitism
        self.mutation = mutation
        self.crossover = crossover
        self.population = []

        self.connection = SerialManager()
        self.a = ArduinoApi(connection=self.connection)
        for r in range(12):
          self.a.pinMode(r, self.a.OUTPUT)

        for i in range(size): self.population.append(Chromosome.gen_random())
        self._setFitness()
        self.population = list(sorted(self.population, key=lambda x: x.fitness))
                        
    def _tournament_selection(self):
        """
        A helper method used to select a random chromosome from the 
        population using a tournament selection algorithm.
        """
        best = choice(self.population)
        for i in range(Population._tournamentSize):
            cont = choice(self.population)
            if (cont.fitness < best.fitness): best = cont
                    
        return best

    def _selectParents(self):
        """
        A helper method used to select two parents from the population using a
        tournament selection algorithm.
        """
        return (self._tournament_selection(), self._tournament_selection())

    def _setFitness(self):
    	for i in range(23):
            for g in self.population:
                gene = g.getGene()
                for x in range(20):
                    self.a.digitalWrite(0, gene[0][x])
                    self.a.digitalWrite(1, gene[1][x])
                    self.a.digitalWrite(2, gene[2][x])
                    self.a.digitalWrite(3, gene[3][x])
                    self.a.digitalWrite(4, gene[4][x])
                    self.a.digitalWrite(5, gene[5][x])
                    self.a.digitalWrite(6, gene[6][x])
                    self.a.digitalWrite(7, gene[7][x])
                    self.a.digitalWrite(8, gene[8][x])
                    self.a.digitalWrite(9, gene[9][x])
                    self.a.digitalWrite(10, gene[10][x])
                    self.a.digitalWrite(11, gene[11][x])
                    g.fitness += self.getNumberOfFaces()
                    print(g.fitness)
                    sleep(0.5)
        
    def evolve(self):
        """
        Method to evolve the population of chromosomes.
        """
        size = len(self.population)
        idx = int(round(size * self.elitism))
        buf = self.population[:idx]
        
        while (idx < size):
            if random() <= self.crossover:
                (p1, p2) = self._selectParents()
                children = p1.mate(p2)
                for c in children:
                    if random() <= self.mutation:
                        buf.append(c.mutate())
                    else:
                        buf.append(c)
                idx += 2
            else:
                if random() <= self.mutation:
                    buf.append(self.population[idx].mutate())
                else:
                    buf.append(self.population[idx])
                idx += 1
        
        self.population = buf
        self._setFitness
        self.population = list(sorted(self.population[:size], key=lambda x: x.fitness))


    def getNumberOfFaces(self):
        ret,frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
		    gray,
		    scaleFactor=1.1,
		    minNeighbors=5, 
            minSize=(30, 30),
		    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
        )
        return len(faces)

if __name__ == "__main__":
    maxGenerations = 16384
    pop = Population(size=60, crossover=0.8, elitism=0.1, mutation=0.3)


    while True:
        #curtime = datetime.datetime.now()
        #if(curtime.day == evolutionLastRunDay):
        #    for patern in pop.population:
        #        for x in range (0, 5):
								#    b = 5
    	pop.evolve()
      #evolutionLastRunDay = curtime.day

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
