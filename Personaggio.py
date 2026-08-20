import random

def genera_personaggio():
    razze = ["Aarakocra", "Aasimar", "Bugbear", "Centaur", "Changeling", "Deep Gnome", "Deva", "Dragonborn", "Drow", "Duergar", "Dwarf", "Eladrin", "Elf", "Fairies", "Firbolg", "Genasi", "Githyanki", "Githzerai", "Gnome", "Goblin", "Goliath", "Grung", "Half-Elf", "Half-Orc", "Halfling", "Harengon", "Hobgoblin", "Human", "Kalashtar", "Kenku", "Kobold", "Leonin", "Lizardfolk", "Locathah", "Loxodon", "Minotaur", "Orc", "Satyr", "Shadar-kai", "Shardmind", "Shifter", "Simic Hybrid", "Tabaxi", "Tiefling", "Tortle", "Triton", "Vedalken", "Verdan", "Warforged", "Wilden", "Yuan-Ti"]
    classi = ['Guerriero', 'Mago', 'Chierico', 'Ladro', 'Bardo', 'Druido']
    sesso = ['Maschio', 'Femmina']

    # Generiamo casualmente le caratteristiche
    forza = random.randint(8, 20)
    destrezza = random.randint(8, 20)
    costituzione = random.randint(8, 20)
    intelligenza = random.randint(8, 20)
    saggezza = random.randint(8, 20)
    carisma = random.randint(8, 20)

    # Creiamo il personaggio
    personaggio = {
        'razza': random.choice(razze),
        'classe': random.choice(classi),
        'sesso': random.choice(sesso),
        'forza': forza,
        'destrezza': destrezza,
        'costituzione': costituzione,
        'intelligenza': intelligenza,
        'saggezza': saggezza,
        'carisma': carisma
    }

    return personaggio

# Generiamo un personaggio e lo stampiamo
mio_personaggio = genera_personaggio()
print(mio_personaggio)
