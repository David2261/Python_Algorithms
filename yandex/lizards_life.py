# Входные данные
# 980 2 12 10 30 1
# 980 3 1 10 31 37
# Выходные данные
# 17 96

def days_in_month(year: int, month: int) -> int:
	days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	return days_in_month[month]

def main() -> None:
	year1: int
	month1: int
	day1: int
	hour1: int
	min1: int
	sec1: int
	year2: int
	month2: int
	day2: int
	hour2: int
	min2: int
	sec2: int

	year1, month1, day1, hour1, min1, sec1 = map(int, input().split())
	year2, month2, day2, hour2, min2, sec2 = map(int, input().split())

	full_days: int = 0
	remaining_seconds: int = 0

	while (year1, month1, day1) != (year2, month2, day2):
		remaining_seconds += 24 * 60 * 60
		day1 += 1

		if day1 > days_in_month(year1, month1):
			day1 = 1
			month1 += 1

			if month1 > 12:
				month1 = 1
				year1 += 1

	remaining_seconds += (hour2 - hour1) * 3600 + (min2 - min1) * 60 + (sec2 - sec1)
	full_days = remaining_seconds // (24 * 60 * 60)
	remaining_seconds %= (24 * 60 * 60)

	print(full_days, remaining_seconds)

if __name__ == "__main__":
	main()
