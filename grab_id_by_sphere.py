import urllib.request
from utility import *

spheres = [
    'Animal', 
    'Astral', 
    'Chaos', 
    'Charm', 
    'Combat', 
    'Creation', 
    'Divination', 
    'Elemental air', 
    'Elemental earth', 
    'Elemental fire', 
    'Elemental water',
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
sphere_ids = {}
url = 'https://regalgoblins.com/spells.php?sphere='

with urllib.request.urlopen(url + spheres[1]) as response:
    html = response.read()

sphere_ids[spheres[1]] = []
spell_list = parse_spell_list(html)
spellbook = [] 
for spell_div in spell_list:
    spellbook.append(create_spell(spell_div))
for spell in spellbook:
    sphere_ids[spheres[1]].append(spell.id)

print(sphere_ids)