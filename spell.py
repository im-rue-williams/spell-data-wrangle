class Spell:
    def __init__(self, spell_item):
        self.name = spell_item['name']
        self.school = spell_item['school']
        self.verbal_comp = spell_item['verbal']
        self.somatic_comp = spell_item['somatic']
        self.material_comp = spell_item['material']
        self.materials = spell_item['materials']
        self.range = spell_item['range']
        self.aoe = spell_item['aoe']
        self.casting_time = spell_item['castingTime']
        self.duration = spell_item['duration']
        self.save = spell_item['save']
        self.damage = spell_item['damage']
        self.description = spell_item['description']
        self.aoe = spell_item['aoe']
        self.level = 0
        self.residue = 'Uncommon'
        self.source = 'PHB pg 170'
        self.sphere = 'animal'

