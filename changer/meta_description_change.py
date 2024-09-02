import random

with open('../additional/meta_description_variants_kink_light.txt', 'r', encoding='UTF=8') as file:
    variants = file.readlines()

def meta_description(name, material, color, room):
    temp = random.choice(variants).strip()
    description = temp.format(name=name, material=material, color=color, room=room)

    return description