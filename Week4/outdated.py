months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    outdated_date = input("Date: ").strip()
    try:
        if "/" in outdated_date:
            month, day, year = map(int, outdated_date.split("/"))
        elif "," in outdated_date:
            outdated_date = outdated_date.replace(",", "")
            month_str, day, year = outdated_date.split()
            if month_str in months:
                month = months.index(month_str) + 1
            else:
                continue
        else:
            continue

        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break

    except ValueError:
        continue

print(f"{year}-{int(month):02}-{int(day):02}")
