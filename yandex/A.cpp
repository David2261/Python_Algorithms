#include <iostream>

bool isLeapYear(int year) {
	return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
}

int daysInMonth(int year, int month) {
	const int daysInMonth[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	return daysInMonth[month];
}

int main() {
	int year1, month1, day1, hour1, min1, sec1;
	int year2, month2, day2, hour2, min2, sec2;

	std::cin >> year1 >> month1 >> day1 >> hour1 >> min1 >> sec1;
	std::cin >> year2 >> month2 >> day2 >> hour2 >> min2 >> sec2;

	long long fullDays = 0;
	long long remainingSeconds = 0;

	while (year1 != year2 || month1 != month2 || day1 != day2) {
		remainingSeconds += 24ll * 60 * 60;
		day1++;

		if (day1 > daysInMonth(year1, month1)) {
			day1 = 1;
			month1++;

			if (month1 > 12) {
				month1 = 1;
				year1++;
			}
		}

		if (day1 > daysInMonth(year1, month1)) {
			day1 = 1;
			month1++;

			if (month1 > 12) {
				month1 = 1;
				year1++;
			}
		}
	}

	remainingSeconds += (hour2 - hour1) * 3600 + (min2 - min1) * 60 + (sec2 - sec1);
	fullDays = remainingSeconds / (24 * 60 * 60);
	remainingSeconds %= (24 * 60 * 60);

	std::cout << fullDays << " " << remainingSeconds << std::endl;

	return 0;
}
