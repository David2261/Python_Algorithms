def group_by_toponyms(explorers):
	places = {}
	for explorer in explorers:
		for place in explorer[1:]:
			places.setdefault(place, [])
	for explorer in explorers:
		for place in explorer[1:]:
			places[place].append(explorer[0])
	result = []
	for place, explorers in places.items():
		result.append([place] + explorers)
	return result

if __name__ == '__main__':
	explorers = [["Mallory", "Everest", "Mont Blanc", "Pillar Rock"],
			 ["Mawson", "South Pole", "New Hebrides"],
			 ["Hillary", "Everest", "South Pole"]]
	print(group_by_toponyms(explorers))
