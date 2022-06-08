# Randomisation
import random
randam_int = random.randint(1, 10)
print(randam_int)
radom_float = random.random()
print(radom_float)

# Lists
# list is a data structure and it stores the data in []..like array
states_of_India = ['AP', 'UP', 'TN', 'KA', 'TS']
print(states_of_India[4])
print(states_of_India[-1])
states_of_India[0] = 'Andrapradhesh'
print(states_of_India)
states_of_India.append('Delhi')
print(states_of_India)
states_of_India.extend(['Hello', 'Raghu', 'Ramaiaha', 'Andrapradhesh'])
print(states_of_India)
print(states_of_India.count('Andrapradhesh'))


# list advanced
fruits = ['strwberries', 'nectarines',
          'Apples', 'Peaches', 'Cherries', 'Pears']
Vegetables = ['Spinach', 'kale', 'Tomotos', 'celery']
dirty_dozen = [fruits, Vegetables]
print(dirty_dozen)
