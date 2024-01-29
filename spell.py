class Spell:
    def __init__(self):
        self.id = 0
        self.level = ''
        self.name = ''
        self.school = ''
        self.verbal_comp = True
        self.somatic_comp = True
        self.material_comp = True
        self.materials =  ''
        self.range =  ''
        self.aoe =  ''
        self.casting_time =  ''
        self.duration =  ''
        self.save =  ''
        self.damage =  ''
        self.description =  ''
        self.residue = ''
        self.source = ''
        self.sphere = ''
        self.caster = ''
    
    def print_spell(self):
        print('ID: ' + self.id)
        print('NAME: ' + self.name)
        print('SCHOOL: ' + self.school)
        print('V: ' + str(self.verbal_comp))
        print('S: ' + str(self.somatic_comp))
        print('M: ' + str(self.material_comp))
        print('MATERIALS NEEDED: ' + self.materials)
        print('RANGE: ' + self.range)
        print('AOE: ' + self.aoe)
        print('CAST TIME: ' + self.casting_time)
        print('DURATION: ' + self.duration)
        print('SAVE: ' + self.save)
        print('DAMAGE: ' + self.damage)
        print('DESC: ' + self.description)
        print('LEVEL: ' + self.level)       
        print('RESIDUE: ' + self.residue)
        print('SOURCE: ' + self.source)
        print('SPHERE: ' + self.sphere)
        print('CASTER: ' + self.caster)