# Class/Assignment: CS3080 Final Project
# Names: Ben Martin, Jisop Lee
# Description: This program manages all method calls the Discord bot will use.
#

import re
import requests
import random

# create_card_db(input_file) gathers card data from the input file and returns a list of card dictionaries
# in the following form:
#
#   card = {
#       "name": "String"
#       "id": Integer
#       "rarity": "String"
#       "type": "String"
#       "passcode": Integer
#   }


def create_card_db(input_file):

    # Initialize structures
    set_list = []

    # Open file and load data
    with open(input_file, 'r') as reader:

        # Iterate until there are no lines remaining
        while True:

            # Obtain the first line
            first_line = reader.readline()
            if not first_line:
                break

            # First line should be BP01-EN(ID)\t(Name)\t(Rarity)\n
            first_line_regex = re.compile(r'BP01-EN([0-9]{3})\t"(.+)"\t(\w+)\n')

            # Obtain attributes
            card_id = int(re.sub(first_line_regex, r'\1', first_line))
            card_name = re.sub(first_line_regex, r'\2', first_line)
            card_rarity = re.sub(first_line_regex, r'\3', first_line)

            # Generate string URL for API
            card_words = card_name.split(' ')
            card_url = ''
            count = 0
            for word in card_words:

                card_url += word
                if count != len(card_words) - 1:
                    card_url += '%20'

                count += 1

            # Send request to API
            response = requests.get('https://db.ygoprodeck.com/api/v7/cardinfo.php?name=' + card_url)

            # Obtain attribute
            # passcode_regex = re.compile(r'(.*)"id":(\d+)(.*)')
            passcode_regex = re.compile(r'{"data":\[{"id":(\d+)(.*)')
            # card_passcode = re.sub(passcode_regex, r'\2', response.text)
            card_passcode = re.sub(passcode_regex, r'\1', response.text)

            # Obtain the second line
            second_line = reader.readline()

            # Second line should be Starfoil Rare\t(Type)\n
            second_line_regex = re.compile(r'Starfoil Rare\t(.+)\n?')

            # Obtain attribute
            card_type = re.sub(second_line_regex, r'\1', second_line)

            # Initialize card
            card = {
                "name": card_name,
                "id": card_id,
                "rarity": card_rarity,
                "type": card_type,
                "passcode": card_passcode
            }

            # Append to set list
            set_list.append(card)

    # Close file and return list
    reader.close()
    return set_list

# bp_epic_dawn is the list generated by create_card_db('BP_Epic_Dawn.txt').
# Some changes are manually hard-coded to match


def bp_epic_dawn():

    obtained_list = [{'name': 'Witch of the Black Forest', 'id': 1, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '78010363'},
     {'name': 'Cyber Jar', 'id': 2, 'rarity': 'Rare', 'type': 'Flip monster', 'passcode': '34124316'},
     {'name': 'Jinzo', 'id': 3, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '77585513'},
     {'name': 'Injection Fairy Lily', 'id': 4, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '79575620'},
     {'name': 'Dark Dust Spirit', 'id': 5, 'rarity': 'Rare', 'type': 'Spirit monster', 'passcode': '89111398'},
     {'name': 'Skull Archfiend of Lightning', 'id': 6, 'rarity': 'Rare', 'type': 'Effect Monster',
      'passcode': '61370518'},
     {'name': 'Dark Magician of Chaos', 'id': 7, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '40737112'},
     {'name': 'Blowback Dragon', 'id': 8, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '25551951'},
     {'name': 'Mobius the Frost Monarch', 'id': 9, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '4929256'},
     {'name': 'Fox Fire', 'id': 10, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '88753985'},
     {'name': 'Ancient Gear Golem', 'id': 11, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '83104731'},
     {'name': 'Treeborn Frog', 'id': 12, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '12538374'},
     {'name': 'Super Conductor Tyranno', 'id': 13, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '85520851'},
     {'name': 'Gorz the Emissary of Darkness', 'id': 14, 'rarity': 'Rare', 'type': 'Effect Monster',
      'passcode': '44330098'},
     {'name': 'Raiza the Storm Monarch', 'id': 15, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '73125233'},
     {'name': 'White Night Dragon', 'id': 16, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '79473793'},
     {'name': 'Deep Diver', 'id': 17, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '17559367'},
     {'name': 'Caius the Shadow Monarch', 'id': 18, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '9748752'},
     {'name': 'Krebons', 'id': 19, 'rarity': 'Rare', 'type': 'Effect Tuner monster', 'passcode': '59575539'},
     {'name': 'Tragoedia', 'id': 20, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '98777036'},
     {'name': 'Obelisk the Tormentor', 'id': 21, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '10000000'},
     {'name': 'Machina Fortress', 'id': 22, 'rarity': 'Rare', 'type': 'Effect Monster', 'passcode': '5556499'},
     {'name': 'Tour Guide From the Underworld', 'id': 23, 'rarity': 'Rare', 'type': 'Effect Monster',
      'passcode': '10802915'},
     {'name': 'Number 39: Utopia', 'id': 24, 'rarity': 'Rare', 'type': 'Effect Xyz Monster', 'passcode': '84013237'},
     {'name': 'Gachi Gachi Gantetsu', 'id': 25, 'rarity': 'Rare', 'type': 'Effect Xyz Monster', 'passcode': '10002346'},
     {'name': 'Grenosaurus', 'id': 26, 'rarity': 'Rare', 'type': 'Effect Xyz Monster', 'passcode': '47506081'},
     {'name': 'Number 17: Leviathan Dragon', 'id': 27, 'rarity': 'Rare', 'type': 'Effect Xyz Monster',
      'passcode': '69610924'},
     {'name': 'Wind-Up Zenmaister', 'id': 28, 'rarity': 'Rare', 'type': 'Effect Xyz Monster', 'passcode': '68597372'},
     {'name': 'Tiras, Keeper of Genesis', 'id': 29, 'rarity': 'Rare', 'type': 'Effect Xyz Monster',
      'passcode': '31386180'},
     {'name': 'Adreus, Keeper of Armageddon', 'id': 30, 'rarity': 'Rare', 'type': 'Effect Xyz Monster',
      'passcode': '94119480'},
     {'name': 'Gem-Knight Pearl', 'id': 31, 'rarity': 'Rare', 'type': 'Xyz Monster', 'passcode': '71594310'},
     {'name': 'Raigeki', 'id': 32, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '12580477'},
     {'name': 'Swords of Revealing Light', 'id': 33, 'rarity': 'Rare', 'type': 'Normal Spell Card',
      'passcode': '72302403'},
     {'name': 'Pot of Greed', 'id': 34, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '55144522'},
     {'name': "Harpie's Feather Duster", 'id': 35, 'rarity': 'Rare', 'type': 'Normal Spell Card',
      'passcode': '18144507'},
     {'name': 'Graceful Charity', 'id': 36, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '79571449'},
     {'name': 'Change of Heart', 'id': 37, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '4031928'},
     {'name': 'Heavy Storm', 'id': 38, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '19613556'},
     {'name': 'Snatch Steal', 'id': 39, 'rarity': 'Rare', 'type': 'Equip Spell Card', 'passcode': '45986603'},
     {'name': 'Premature Burial', 'id': 40, 'rarity': 'Rare', 'type': 'Equip Spell Card', 'passcode': '70828912'},
     {'name': 'Soul Exchange', 'id': 41, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '68005187'},
     {'name': 'Scapegoat', 'id': 42, 'rarity': 'Rare', 'type': 'Quick-Play Spell Card', 'passcode': '73915051'},
     {'name': 'United We Stand', 'id': 43, 'rarity': 'Rare', 'type': 'Equip Spell Card', 'passcode': '56747793'},
     {'name': 'Creature Swap', 'id': 44, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '31036355'},
     {'name': 'Burden of the Mighty', 'id': 45, 'rarity': 'Rare', 'type': 'Continuous Spell Card',
      'passcode': '44947065'},
     {'name': 'Pot of Duality', 'id': 46, 'rarity': 'Rare', 'type': 'Normal Spell Card', 'passcode': '98645731'},
     {'name': 'Solemn Judgment', 'id': 47, 'rarity': 'Rare', 'type': 'Counter Trap Card', 'passcode': '41420027'},
     {'name': 'Mirror Force', 'id': 48, 'rarity': 'Rare', 'type': 'Normal Trap Card', 'passcode': '44095762'},
     {'name': 'Call of the Haunted', 'id': 49, 'rarity': 'Rare', 'type': 'Continuous Trap Card',
      'passcode': '97077563'},
     {'name': 'Ring of Destruction', 'id': 50, 'rarity': 'Rare', 'type': 'Normal Trap Card', 'passcode': '83555666'},
     {'name': 'Torrential Tribute', 'id': 51, 'rarity': 'Rare', 'type': 'Normal Trap Card', 'passcode': '53582587'},
     {'name': 'Metal Reflect Slime', 'id': 52, 'rarity': 'Rare', 'type': 'Continuous Trap Card',
      'passcode': '26905245'},
     {'name': 'Skill Drain', 'id': 53, 'rarity': 'Rare', 'type': 'Continuous Trap Card', 'passcode': '82732705'},
     {'name': 'Divine Wrath', 'id': 54, 'rarity': 'Rare', 'type': 'Counter Trap Card', 'passcode': '49010598'},
     {'name': 'Dark Bribe', 'id': 55, 'rarity': 'Rare', 'type': 'Counter Trap Card', 'passcode': '77538567'},
     {'name': 'Greenkappa', 'id': 56, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '61831093'},
     {'name': 'Penguin Soldier', 'id': 57, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '93920745'},
     {'name': 'Mysterious Guard', 'id': 58, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '1347977'},
     {'name': 'Exiled Force', 'id': 59, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '74131780'},
     {'name': 'Old Vindictive Magician', 'id': 60, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '45141844'},
     {'name': 'Breaker the Magical Warrior', 'id': 61, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '71413901'},
     {'name': 'Grave Squirmer', 'id': 62, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '48343627'},
     {'name': 'Ryko, Lightsworn Hunter', 'id': 63, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '21502796'},
     {'name': 'Snowman Eater', 'id': 64, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '91133740'},
     {'name': 'Fissure', 'id': 65, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '66788016'},
     {'name': 'Tribute to The Doomed', 'id': 66, 'rarity': 'Common', 'type': 'Normal Spell Card',
      'passcode': '79759861'},
     {'name': 'Axe of Despair', 'id': 67, 'rarity': 'Common', 'type': 'Equip Spell Card', 'passcode': '40619825'},
     {'name': 'Mystical Space Typhoon', 'id': 68, 'rarity': 'Common', 'type': 'Quick-Play Spell Card',
      'passcode': '5318639'},
     {'name': 'Horn of the Unicorn', 'id': 69, 'rarity': 'Common', 'type': 'Equip Spell Card', 'passcode': '64047146'},
     {'name': 'Offerings to the Doomed', 'id': 70, 'rarity': 'Common', 'type': 'Quick-Play Spell Card',
      'passcode': '19230408'},
     {'name': 'Bait Doll', 'id': 71, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '7165085'},
     {'name': 'Book of Moon', 'id': 72, 'rarity': 'Common', 'type': 'Quick-Play Spell Card', 'passcode': '14087893'},
     {'name': 'Autonomous Action Unit', 'id': 73, 'rarity': 'Common', 'type': 'Equip Spell Card',
      'passcode': '71453557'},
     {'name': 'Ante', 'id': 74, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '34236961'},
     {'name': 'Big Bang Shot', 'id': 75, 'rarity': 'Common', 'type': 'Equip Spell Card', 'passcode': '61127349'},
     {'name': "Fiend's Sanctuary", 'id': 76, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '24874630'},
     {'name': 'Different Dimension Gate', 'id': 77, 'rarity': 'Common', 'type': 'Continuous Spell Card',
      'passcode': '56460688'},
     {'name': 'Enemy Controller', 'id': 78, 'rarity': 'Common', 'type': 'Quick-Play Spell Card',
      'passcode': '98045062'},
     {'name': 'Monster Gate', 'id': 79, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '43040603'},
     {'name': 'Shield Crush', 'id': 80, 'rarity': 'Common', 'type': 'Normal Spell Card', 'passcode': '30683373'},
     {'name': 'Fighting Spirit', 'id': 81, 'rarity': 'Common', 'type': 'Equip Spell Card', 'passcode': '6178850'},
     {'name': 'Forbidden Chalice', 'id': 82, 'rarity': 'Common', 'type': 'Quick-Play Spell Card',
      'passcode': '25789292'},
     {'name': 'Darkworld Shackles', 'id': 83, 'rarity': 'Common', 'type': 'Equip Spell Card', 'passcode': '83584898'},
     {'name': 'Forbidden Lance', 'id': 84, 'rarity': 'Common', 'type': 'Quick-Play Spell Card', 'passcode': '27243130'},
     {'name': 'Infected Mail', 'id': 85, 'rarity': 'Common', 'type': 'Continuous Spell Card', 'passcode': '6430659'},
     {'name': 'Ego Boost', 'id': 86, 'rarity': 'Common', 'type': 'Quick-Play Spell Card', 'passcode': '73178098'},
     {'name': 'Kunai with Chain', 'id': 87, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '37390589'},
     {'name': 'Dust Tornado', 'id': 88, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '60082869'},
     {'name': 'Windstorm of Etaqua', 'id': 89, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '59744639'},
     {'name': 'Magic Drain', 'id': 90, 'rarity': 'Common', 'type': 'Counter Trap Card', 'passcode': '59344077'},
     {'name': 'Magic Cylinder', 'id': 91, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '62279055'},
     {'name': 'Shadow Spell', 'id': 92, 'rarity': 'Common', 'type': 'Continuous Trap Card', 'passcode': '29267084'},
     {'name': 'Blast with Chain', 'id': 93, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '98239899'},
     {'name': 'Needle Ceiling', 'id': 94, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '38411870'},
     {'name': 'Reckless Greed', 'id': 95, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '37576645'},
     {'name': 'Nightmare Wheel', 'id': 96, 'rarity': 'Common', 'type': 'Continuous Trap Card', 'passcode': '54704216'},
     {'name': 'Spell Shield Type-8', 'id': 97, 'rarity': 'Common', 'type': 'Counter Trap Card', 'passcode': '38275183'},
     {'name': 'Interdimensional Matter Transporter', 'id': 98, 'rarity': 'Common', 'type': 'Normal Trap Card',
      'passcode': '36261276'},
     {'name': 'Compulsory Evacuation Device', 'id': 99, 'rarity': 'Common', 'type': 'Normal Trap Card',
      'passcode': '94192409'},
     {'name': 'Prideful Roar', 'id': 100, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '66518841'},
     {'name': 'Half or Nothing', 'id': 101, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '15552258'},
     {'name': 'Skill Successor', 'id': 102, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '73729209'},
     {'name': 'Pixie Ring', 'id': 103, 'rarity': 'Common', 'type': 'Continuous Trap Card', 'passcode': '46502013'},
     {'name': 'Changing Destiny', 'id': 104, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '24673894'},
     {'name': 'Fiendish Chain', 'id': 105, 'rarity': 'Common', 'type': 'Continuous Trap Card', 'passcode': '50078509'},
     {'name': 'Inverse Universe', 'id': 106, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '79161790'},
     {'name': "Miracle's Wake", 'id': 107, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '21636650'},
     {'name': 'Power Frame', 'id': 108, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '53656677'},
     {'name': 'Damage Gate', 'id': 109, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '87106146'},
     {'name': 'Liberty at Last!', 'id': 110, 'rarity': 'Common', 'type': 'Normal Trap Card', 'passcode': '72022087'},
     {'name': 'Luster Dragon', 'id': 111, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '11091375'},
     {'name': 'Archfiend Soldier', 'id': 112, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '49881766'},
     {'name': 'Mad Dog of Darkness', 'id': 113, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '79182538'},
     {'name': 'Charcoal Inpachi', 'id': 114, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '13179332'},
     {'name': 'Insect Knight', 'id': 115, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '35052053'},
     {'name': 'Gene-Warped Warwolf', 'id': 116, 'rarity': 'Common', 'type': 'Normal Monster', 'passcode': '69247929'},
     {'name': 'Buster Blader', 'id': 117, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '78193831'},
     {'name': 'Goblin Attack Force', 'id': 118, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '78658564'},
     {'name': 'Bazoo the Soul-Eater', 'id': 119, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '40133511'},
     {'name': 'Zombyra the Dark', 'id': 120, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '88472456'},
     {'name': 'Slate Warrior', 'id': 121, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '78636495'},
     {'name': 'Dark Ruler Ha Des', 'id': 122, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '53982768'},
     {'name': 'Freed the Matchless General', 'id': 123, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '49681811'},
     {'name': 'Airknight Parshath', 'id': 124, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '18036057'},
     {'name': 'Asura Priest', 'id': 125, 'rarity': 'Common', 'type': 'Spirit monster', 'passcode': '2134346'},
     {'name': 'Exarion Universe', 'id': 126, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '63749102'},
     {'name': 'Vampire Lord', 'id': 127, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '53839837'},
     {'name': 'Toon Gemini Elf', 'id': 128, 'rarity': 'Common', 'type': 'Toon monster', 'passcode': '42386471'},
     {'name': 'King Tiger Wanghu', 'id': 129, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '83986578'},
     {'name': 'Guardian Sphinx', 'id': 130, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '40659562'},
     {'name': 'Skilled White Magician', 'id': 131, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '46363422'},
     {'name': 'Zaborg the Thunder Monarch', 'id': 132, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '51945556'},
     {'name': 'D.D. Assailant', 'id': 133, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '70074904'},
     {'name': 'Theban Nightmare', 'id': 134, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '51838385'},
     {'name': 'The Tricky', 'id': 135, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '14778250'},
     {'name': 'Raging Flame Sprite', 'id': 136, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '90810762'},
     {'name': 'Chiron the Mage', 'id': 137, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '16956455'},
     {'name': 'Cyber Dragon', 'id': 138, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '70095154'},
     {'name': 'Cybernetic Magician', 'id': 139, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '59023523'},
     {'name': 'Goblin Elite Attack Force', 'id': 140, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '85306040'},
     {'name': 'Doomcaliber Knight', 'id': 141, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '78700060'},
     {'name': 'Chainsaw Insect', 'id': 142, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '77252217'},
     {'name': 'Card Trooper', 'id': 143, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '85087012'},
     {'name': 'Voltic Kong', 'id': 144, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '93151201'},
     {'name': 'Botanical Lion', 'id': 145, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '20546916'},
     {'name': 'Ancient Gear Knight', 'id': 146, 'rarity': 'Common', 'type': 'Gemini monster', 'passcode': '39303359'},
     {'name': 'Blizzard Dragon', 'id': 147, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '61802346'},
     {'name': 'Beast King Barbaros', 'id': 148, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '78651105'},
     {'name': 'The Calculator', 'id': 149, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '51196174'},
     {'name': 'Gaap the Divine Soldier', 'id': 150, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '37955049'},
     {'name': 'Arcana Force XIV - Temperance', 'id': 151, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '60953118'},
     {'name': 'Dark Valkyria', 'id': 152, 'rarity': 'Common', 'type': 'Gemini monster', 'passcode': '83269557'},
     {'name': 'Alector, Sovereign of Birds', 'id': 153, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '17573739'},
     {'name': 'Twin-Barrel Dragon', 'id': 154, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '70050374'},
     {'name': 'Abyssal Kingshark', 'id': 155, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '44223284'},
     {'name': 'Jurrac Protops', 'id': 156, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '23927545'},
     {'name': 'Hedge Guard', 'id': 157, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '59042331'},
     {'name': 'Fabled Ashenveil', 'id': 158, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '12235475'},
     {'name': 'Backup Warrior', 'id': 159, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '95637655'},
     {'name': 'Ambitious Gofer', 'id': 160, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '41224658'},
     {'name': 'Power Giant', 'id': 161, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '7025445'},
     {'name': 'Card Guard', 'id': 162, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '4694209'},
     {'name': 'Yaksha', 'id': 163, 'rarity': 'Common', 'type': 'Spirit monster', 'passcode': '94215860'},
     {'name': 'Gogogo Golem', 'id': 164, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '62476815'},
     {'name': 'Big Jaws', 'id': 165, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '51254277'},
     {'name': 'Wind-Up Soldier', 'id': 166, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '12299841'},
     {'name': 'Wind-Up Dog', 'id': 167, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '12076263'},
     {'name': 'Milla the Temporal Magician', 'id': 168, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '33225925'},
     {'name': 'Ape Fighter', 'id': 169, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '41098335'},
     {'name': 'Wind-Up Warrior', 'id': 170, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '53540729'},
     {'name': 'Giant Soldier of Stone', 'id': 171, 'rarity': 'Common', 'type': 'Normal Monster',
      'passcode': '13039848'},
     {'name': 'Mask of Darkness', 'id': 172, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '28933734'},
     {'name': 'Morphing Jar', 'id': 173, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '33508719'},
     {'name': 'Muka Muka', 'id': 174, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '46657337'},
     {'name': 'Blast Sphere', 'id': 175, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '26302522'},
     {'name': 'Big Shield Gardna', 'id': 176, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '65240384'},
     {'name': 'Gilasaurus', 'id': 177, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '45894482'},
     {'name': 'Possessed Dark Soul', 'id': 178, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '52860176'},
     {'name': 'Twin-Headed Behemoth', 'id': 179, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '43586926'},
     {'name': 'Makyura the Destructor', 'id': 180, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '21593977'},
     {'name': 'Helping Robo for Combat', 'id': 181, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '47025270'},
     {'name': 'Zolga', 'id': 182, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '16268841'},
     {'name': 'Chaos Necromancer', 'id': 183, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '1434352'},
     {'name': 'Stealth Bird', 'id': 184, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '3510565'},
     {'name': 'Hyper Hammerhead', 'id': 185, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '2671330'},
     {'name': 'Grave Protector', 'id': 186, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '11448373'},
     {'name': 'Night Assailant', 'id': 187, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '16226786'},
     {'name': 'Pitch-Black Warwolf', 'id': 188, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '88975532'},
     {'name': 'Dekoichi the Battlechanted Locomotive', 'id': 189, 'rarity': 'Common', 'type': 'Flip monster',
      'passcode': '87621407'},
     {'name': 'Gyroid', 'id': 190, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '18325492'},
     {'name': 'Drillroid', 'id': 191, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '71218746'},
     {'name': 'Gravitic Orb', 'id': 192, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '29216198'},
     {'name': 'Cloudian - Poison Cloud', 'id': 193, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '83982270'},
     {'name': 'Des Mosquito', 'id': 194, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '33695750'},
     {'name': 'Mad Reloader', 'id': 195, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '31034919'},
     {'name': 'Phantom of Chaos', 'id': 196, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '30312361'},
     {'name': 'Cyber Valley', 'id': 197, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '3657444'},
     {'name': 'Blue Thunder T-45', 'id': 198, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '14089428'},
     {'name': 'Vortex Trooper', 'id': 199, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '7736719'},
     {'name': 'DUCKER Mobile Cannon', 'id': 200, 'rarity': 'Common', 'type': 'Flip monster', 'passcode': '14506878'},
     {'name': 'Worm Barses', 'id': 201, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '15658249'},
     {'name': 'Shield Warrior', 'id': 202, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '95360850'},
     {'name': 'Dark Resonator', 'id': 203, 'rarity': 'Common', 'type': 'Effect Tuner monster', 'passcode': '97021916'},
     {'name': 'Noisy Gnat', 'id': 204, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '45620686'},
     {'name': 'Fabled Raven', 'id': 205, 'rarity': 'Common', 'type': 'Effect Tuner monster', 'passcode': '47217354'},
     {'name': 'Fortress Warrior', 'id': 206, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '66288028'},
     {'name': 'Twin-Sword Marauder', 'id': 207, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '40225398'},
     {'name': 'Level Warrior', 'id': 208, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '97385276'},
     {'name': 'Level Eater', 'id': 209, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '57421866'},
     {'name': 'Naturia Strawberry', 'id': 210, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '55099248'},
     {'name': 'Battle Fader', 'id': 211, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '19665973'},
     {'name': 'Amazoness Sage', 'id': 212, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '53162898'},
     {'name': 'Amazoness Trainee', 'id': 213, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '89567993'},
     {'name': 'Hardened Armed Dragon', 'id': 214, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '68473226'},
     {'name': 'Blackwing - Zephyros the Elite', 'id': 215, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '14785765'},
     {'name': 'Tanngrisnir of the Nordic Beasts', 'id': 216, 'rarity': 'Common', 'type': 'Effect Monster',
      'passcode': '15394083'},
     {'name': 'Shine Knight', 'id': 217, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '86952477'},
     {'name': 'Gagaga Magician', 'id': 218, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '26082117'},
     {'name': 'Goblindbergh', 'id': 219, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '25259669'},
     {'name': 'Psi-Blocker', 'id': 220, 'rarity': 'Common', 'type': 'Effect Monster', 'passcode': '29417188'}]

    # Changes made for Duelingbook integration
    obtained_list[69]['passcode'] = 19230407
    obtained_list[34]['passcode'] = 18144506
    obtained_list[20]['passcode'] = 10000002

    return obtained_list

# open_pack() returns a list of 5 (somewhat) randomly-generated cards. Each pack contains the following:
# -one Rare card (with id = 1-55)
# -one Common card (with id = 56-110)
# -one Common card (with id = 111-170)
# -one Common card (with id = 171-220)
# -one Starfoil card (with id = 1-220)


def open_pack(card_list):

    # Initialize
    pack_contents = []

    # Generate 5 random integers
    rare_id = random.randint(1, 55)
    common1_id = random.randint(56, 110)
    common2_id = random.randint(111, 170)
    common3_id = random.randint(171, 220)
    starfoil_id = random.randint(1, 220)

    # Find cards and append to list
    ids = [rare_id, common1_id, common2_id, common3_id, starfoil_id]
    for id_number in ids:
        card = dict(card_list[id_number - 1])

        # if Starfoil, change rarity
        if id_number == starfoil_id:
            card['rarity'] = 'Starfoil'

        pack_contents.append(card)

    # Return
    return pack_contents

# generate_deck() returns a list of 50 cards generated by 10 opened packs.


def generate_deck(card_list):

    # Initialize
    deck = []
    num_packs = 10

    # Iterate for each pack
    for pack in range(0, num_packs):

        # Open pack
        pack = open_pack(card_list)
        for pack_card in pack:
            deck.append(pack_card)

    # Return
    return deck

# generate_ydk() returns a .ydk file that consists of all passcodes of the 50 cards generated.


def generate_ydk(deck_list):

    # Initialize file
    ydk = open('bp_epic_dawn.ydk', 'w')
    ydk.write('#created by ...\n')
    ydk.write('#main\n')

    # Initialize lists
    main_deck = []
    extra_deck = []

    # Iterate through each card
    for deck_card in deck_list:
        if deck_card['type'].endswith('Xyz Monster'):
            extra_deck.append(deck_card['passcode'])
        else:
            main_deck.append(deck_card['passcode'])

    # Add all main deck cards
    for passcode in main_deck:
        ydk.write(str(passcode) + '\n')

    # More formatting
    ydk.write('#extra\n')

    # Add all extra deck cards, if any
    for passcode_extra in extra_deck:
        ydk.write(str(passcode_extra) + '\n')

    # Even more formatting
    ydk.write('!side\n')

    # Close file
    ydk.close()
