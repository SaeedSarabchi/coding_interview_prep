import time
from Queue import Queue


class Animal:
    def __init__(self, type, name):
        self.name = name
        self.time_stamp = None
        self.type = type

    def __str__(self):
        return '{}-{}-{}'.format(self.name, self.type, self.time_stamp)


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        animal.time_stamp = time.time()
        if animal.type == "dog":
            self.dog_queue.add(animal)
        if animal.type == "cat":
            self.cat_queue.add(animal)

    def dequeue_any(self):
        if self.dog_queue.is_empty():
            return self.cat_queue.remove()
        if self.cat_queue.is_empty():
            return self.dog_queue.remove()
        if self.dog_queue.peek().time_stamp < self.cat_queue.peek().time_stamp:
            return self.dog_queue.remove()
        else:
            return self.cat_queue.remove()

    def dequeue_dog(self):
        return self.dog_queue.remove()

    def dequeue_cat(self):
        return self.cat_queue.remove()


animal_shelter = AnimalShelter()
animal_1 = Animal("dog", "dog1")
animal_2 = Animal("dog", "dog2")
animal_3 = Animal("cat", "cat1")
animal_4 = Animal("cat", "cat2")
animal_shelter.enqueue(animal_1)
time.sleep(1)
animal_shelter.enqueue(animal_2)
time.sleep(1)
animal_shelter.enqueue(animal_3)
time.sleep(1)
animal_shelter.enqueue(animal_4)
print(animal_shelter.dequeue_dog())
print(animal_shelter.dequeue_cat())
print(animal_shelter.dequeue_any())
print(animal_shelter.dequeue_any())