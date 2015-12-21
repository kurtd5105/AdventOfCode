import itertools


def simulate(boss, player, items):
	#Boost the player's stats based on the items
	for item in items:
		player[1] += item[1]
		player[2] += item[2]

	#Damage is attacker attack - defender armor
	playerDmg = (player[1] - boss[2])
	if playerDmg < 1:
		playerDmg = 1

	bossDmg = (boss[1] - player[2])
	if bossDmg < 1:
		bossDmg = 1

	#Make them fight until at least one of them has no more health
	while boss[0] > 0 and player[0] > 0:
		boss[0] -= playerDmg
		player[0] -= bossDmg

	#Player attacks first so the boss will die first
	if boss[0] <= 0:
		return True
	return False


#Damage done is damage - armor but always at least 1 damage
#Hitpoints, damage, armor
bossStats = [103, 9, 2]
playerStats = [100, 0, 0]

#Weapon, ring, armor. Can't buy duplicates
limits = [1, 2, 1]

#Cost, damage, armor
armors = [[13, 0, 1], [31, 0, 2], [53, 0, 3], [75, 0, 4], [102, 0, 5]]
rings = [[25, 1, 0], [50, 2, 0], [100, 3, 0], [20, 0, 1], [40, 0, 2], [80, 0, 3]]
weapons = [[8, 4, 0], [10, 5, 0], [25, 6, 0], [40, 7, 0], [74, 8, 0]]

#Simulate the player fighting without any items
success = simulate(list(bossStats), list(playerStats), [])
maxGold = 0
#For every possible amount of weapons, rings, armor
for i in range(1, limits[0] + 1):
	for j in xrange(limits[1] + 1):
		for k in xrange(limits[2] + 1):
			#For every combination of every possible amount of weapons, rings, armor
			for weapon in itertools.combinations(weapons, i):
				for ring in itertools.combinations(rings, j):
					for armor in itertools.combinations(armors, k):
						items = []
						gold = 0
						#Add the items to the item list if they exist and add their gold cost
						if weapon:
							items.append(weapon[0])
							gold += weapon[0][0]
						if ring:
							items.extend([x for x in ring])
							gold += sum([x[0] for x in ring])
						if armor:
							items.append(armor[0])
							gold += armor[0][0]

						success = simulate(list(bossStats), list(playerStats), items)
						if not success:
							if gold > maxGold:
								maxGold = gold
print maxGold
