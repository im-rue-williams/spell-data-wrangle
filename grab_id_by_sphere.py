from utility import *

filter_catergories = {
   'sphere=': [
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
   ],
   'caster=': [
      'Wizard',
      "Priest"
   ],
   'school=': [
      'Abjuration',
      'Alteration',
      'Conjuration',
      'Divination',
      'Enchantment',
      'Evocation',
      'Illusion',
      'Necromancy'
   ]
}
filter_names = list(filter_catergories.keys())

# sphere_ids ={}

# for category in filter_catergories[filter_names[0]]:
#          sphere_ids[category] = get_spell_ids(category) 
# print(sphere_ids) 

caster_ids ={}
for category in filter_catergories[filter_names[1]]:
         caster_ids[category] = get_spell_ids(category) 
print(caster_ids) 

# school_ids ={}
# for category in filter_catergories[filter_names[2]]:
#          school_ids[category] = get_spell_ids(category) 
# print(school_ids) 
