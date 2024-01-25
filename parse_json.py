import json
from spell import Spell

file = open('sample.json')

spells = json.load(file)

spell_list = []

for i in spells['spells']:
    spell_item = Spell(i)
    spell_list.append(spell_item)

file.close

for i in spell_list:
    print(i.school)