from copy import copy

def is_report_save(report):
    previous = None
    increasing = None
    for reading in report:
        if previous is None:
            previous = reading
            continue
        if abs(reading - previous) > 3 or abs(reading - previous) == 0:
            return False

        if increasing is None:
            increasing = reading > previous
        elif increasing and reading < previous:
            return False
        elif not increasing and reading > previous:
            return False
        previous = reading
    return True

reports = []
with open("input_big.txt") as f:
    for line in f:
        line = line.replace("\n", "" )
        report = [int(n) for n in line.split(" ")]
        reports.append(report)

save = 0
for report in reports:
    if is_report_save(report):
        save += 1
print(f"Part one, no problem dampener: {save}")

save = 0
for report in reports:
    for i in range(len(report)):
        short_report = copy(report)
        short_report.pop(i)
        if is_report_save(short_report):
            save += 1
            break
print(f"Part two, with problem dampener: {save}")
