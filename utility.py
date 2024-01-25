from bs4 import BeautifulSoup

def grab_spell_list(f):
    soup = BeautifulSoup(f, 'html.parser')
    spells = soup.find_all('div', attrs={'data-id' : True})
    return spells
