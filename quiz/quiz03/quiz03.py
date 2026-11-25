student = {'이름':'김파이','학년':2,'전공':'컴퓨터공학','점수':[90,85,77]}
print(student['이름'])
print(student['전공'])
print(student['점수'][1])
student['학년'] = 3
student['email'] = 'kim@py.com'
print(student)

keys = ['alpha', 'bravo', 'charlie', 'delta']
values = [10, 20, 30, 40]
print(list(zip(keys,values)))  # 딕셔너리가 아닌 그냥 묶고 출력

dics = dict(zip(keys,values)) 
print(dics['delta'])

camille = {'health': 575.6, 'health_regen': 1.7, 'mana': 338.8,
        'mana_regen': 1.63, 'melee': 125, 'attack_damage': 60,
        'attack_speed': 0.625, 'armor': 26, 'magic_resistance': 32.1,
        'movement_speed': 340}
stat = input('키 이름 :')
print(camille.get(stat,'없는 항목'))

if stat in camille :
    print(camille.get(stat,'없는 항목'))
