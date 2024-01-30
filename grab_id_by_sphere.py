from utility import *

spheres = [
    'Animal', 
    'Astral', 
    'Chaos', 
    'Charm', 
    'Combat', 
    'Creation', 
    'Divination', 
    'Elemental%20Air', 
    'Elemental%20Earth', 
    'Elemental%20Fire', 
    'Elemental%20Water',
    'Guardian',
    'Healing',
    'Law',
    'Necromantic',
    'Numbers',
    'Plant',
    'Protection',
    'Summoning',
    'Sun',
    'Thought',
    'Time',
    'Travelers',
    'War',
    'Wards',
    'Weather'
]
sphere_ids ={}
for category in spheres:
   sphere_ids[category] = get_spell_ids(category) 

print(sphere_ids)