from bs4 import BeautifulSoup
from spell import Spell

def parse_spell_list(f):
    soup = BeautifulSoup(f, 'html.parser')
    spells = soup.find_all('div', attrs={'data-id' : True})
    return spells

def create_spell(spell_div):
    spell = Spell()
    spell.id = spell_div['data-id']
    spell.school = spell_div['data-school']
    spell.caster = spell_div['data-caster']
    spell.level = spell_div.find('button', {'class' : 'level'}).text
    spell.name = spell_div.find('div', {'class' : 'name'}).text
    spell.materials = spell_div.find('dd', {'class' : 'materials'}).text
    spell.range = spell_div.find('dd', {'class' : 'range'}).text
    spell.aoe = spell_div.find('dd', {'class' : 'aoe'}).text
    spell.casting_time = spell_div.find('dd', {'class' : 'castingTime'}).text
    spell.duration = spell_div.find('dd', {'class' : 'duration'}).text
    spell.save = spell_div.find('dd', {'class' : 'save'}).text
    spell.damage = spell_div.find('dd', {'class' : 'damage'}).text
    spell.description = spell_div.find('div', {'class' : 'description-content'}).text
    spell.residue = spell_div.find('dl', {'class' : 'label'}).text.split()[1] if len(spell_div.find('dl', {'class' : 'label'}).text.split())>1 else ""
    spell.source = spell_div.find_all('dl', {'class' : 'bot'})[1].text[7:].strip() 
    spell.somatic_comp = bool(spell_div.find('div', {'class' : 'somatic'}))
    spell.verbal_comp = bool(spell_div.find('div', {'class' : 'verbal'}))
    spell.material_comp = bool(spell_div.find('div', {'class' : 'material'}))
    return spell