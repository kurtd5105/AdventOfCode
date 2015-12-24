#Took 3 tries from scratch to get working
#Apply the timed spells, cast the current spell, apply the timed spells for the boss
#turn, apply the damage from the boss turn. 
def success(player, boss, moves):
	playerHp = player[0]
	playerArmor = player[2]
	bossHp = boss[0]
	bossDmg = boss[1] - playerArmor
	if bossDmg < 1:
		bossDmg = 1
	mana = player[1]
	cost = 0
	poison = 0
	recharge = 0
	shield = 0
	poisonTime = 6
	rechargeTime = 5
	shieldTime = 6

	spells = {"M": [53, 4], "D": [73, 2], "P": [173, 3], "S": [113, 7], "R": [229, 101]}
	for spell in moves:
		if poison > 0:
			bossHp -= spells["P"][1]
			poison -= 1
		if recharge > 0:
			mana += spells["R"][1]
			recharge -= 1
		if shield > 0:
			playerArmor = spells["S"][1]
			shield -= 1
		else:
			playerArmor = 0

		if spell == "P" and poison > 0:
			return 0
		if spell == "R" and recharge > 0:
			return 0
		if spell == "S" and shield > 0:
			return 0
		if spell == "P":
			if spells["P"][0] < mana:
				mana -= spells["P"][0]
				cost += spells["P"][0]
				poison = poisonTime
			else:
				return 0
		if spell == "R":
			if spells["R"][0] < mana:
				mana -= spells["R"][0]
				cost += spells["R"][0]
				recharge = rechargeTime
			else:
				return 0
		if spell == "S":
			if spells["S"][0] < mana:
				mana -= spells["S"][0]
				cost += spells["S"][0]
				shield = shieldTime
			else:
				return 0

		if spell == "M":
			if spells["M"][0] < mana:
				bossHp -= spells["M"][1]
				mana -= spells["M"][0]
				cost += spells["M"][0]
			else:
				return 0
		if spell == "D":
			if spells["D"][0] < mana:
				bossHp -= spells["D"][1]
				playerHp += spells["D"][1]
				mana -= spells["D"][0]
				cost += spells["D"][0]
			else:
				return 0

		if poison > 0:
			bossHp -= spells["P"][1]
			poison -= 1
		if recharge > 0:
			mana += spells["R"][1]
			recharge -= 1
		if shield > 0:
			playerArmor = spells["S"][1]
			shield -= 1
		else:
			playerArmor = 0

		if bossHp <= 0:
			return cost
		else:
			bossDmg = boss[1] - playerArmor
			if bossDmg < 1:
				bossDmg = 1
			playerHp -= bossDmg
			if playerHp <= 0:
				return 0

#Iterator for generating the set of moves
def cyclePart(move, maxS, count, pos, offset):
	move[pos] = "MDPSR"[offset]
	if count < maxS:
		for i in xrange(5):
			for move in cyclePart(list(move), maxS, count + 1, pos + 1, i):
				yield move
	else:
		yield move


#hp, damage
boss = [58, 9]

#hp, mana, armor
player = [50, 500, 0]

minMana = 1e100
count = 0
move = ['M'] * 20
result = 0

for j in xrange(10):
	for i in range(1, 15):
		for k in xrange(5):
			for moves in cyclePart(list(move), i, 0, j, k):
				#Can't be won without these prerequisites
				if "R" in moves[:9] and "S" in moves[:8]:
					result = success(player, boss, moves)
					if result < minMana and result != 0:
						minMana = result
						print "Current min:", minMana


print minMana
