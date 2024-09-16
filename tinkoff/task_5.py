from collections import defaultdict
from datetime import datetime

def parse_time(time_str):
	return datetime.strptime(time_str, "%H:%M:%S")

def calculate_penalty(start_time, request_time):
	delta = request_time - start_time
	minutes = delta.seconds // 60
	return minutes

def main():
	start_time_str = input()
	start_time = parse_time(start_time_str)
	n = int(input())
	teams = defaultdict(lambda: {"score": 0, "penalty": 0, "servers": set()})
	for _ in range(n):
		team_name, request_time_str, server, result = input().split()
		request_time = parse_time(request_time_str)
		if result == "ACCESSED":
			teams[team_name]["score"] += 1
			teams[team_name]["servers"].add(server)
			penalty = calculate_penalty(start_time, request_time)
			teams[team_name]["penalty"] += penalty
		elif result in ["DENIED", "FORBIDEN"]:
			penalty = 20
			teams[team_name]["penalty"] += penalty

	sorted_teams = sorted(teams.items(), key=lambda x: (-x[1]["score"], x[1]["penalty"], x[0]))
	for i, (team_name, team_info) in enumerate(sorted_teams):
		print(f"{i+1} {team_name} {team_info['score']} {team_info['penalty']}")

if __name__ == "__main__":
	main()