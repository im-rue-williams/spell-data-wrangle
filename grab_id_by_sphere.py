import urllib.request
from bs4 import BeautifulSoup

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

url = 'https://regalgoblins.com/spells.php?sphere=' + spheres[1]

with urllib.request.urlopen(url) as response:
    html = response.read()


print(html)