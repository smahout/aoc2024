import logging
from copy import copy

debug = logging.debug
info = logging.info


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


def is_report_saveish(report, try_again=False):
    increasing = None
    is_safe = True
    false_index = None
    for i in range(len(report)):
        if i == 0:
            continue
        previous = report[i - 1]
        reading = report[i]
        increasing = reading > previous if increasing is None else increasing
        if abs(reading - previous) > 3 or abs(reading - previous) == 0:
            debug(
                f"Problem with DIFFERENCE; {reading} and {previous}, diff is {abs(reading - previous)}. Try again is {try_again}")
            is_safe = False
            false_index = i
            break
        if increasing and reading < previous:
            debug(f"Problem with DECREASE; {reading} and {previous}. Try again is {try_again}")
            is_safe = False
            false_index = i
            break
        elif not increasing and reading > previous:
            debug(f"Problem with INCREASE; {reading} and {previous}. Try again is {try_again}")
            is_safe = False
            false_index = i
            break

    if (not is_safe) and try_again:
        split1 = copy(report)
        split2 = copy(report)
        split1.pop(false_index - 1)
        split2.pop(false_index)

        if false_index - 1 == 1:
            split0 = copy(report)
            split0.pop(0)
            debug(
                f"Making split1: {split1}. Making split2: {split2}. FIRST PROBLEM ENCOUNTERED ON INDEX ONE. Making split0: {split0}. From source: {report}")
            return is_report_saveish(split1) or is_report_saveish(split2) or is_report_saveish(split0)

        debug(f"Making split1: {split1}. Making split2: {split2}. From source: {report}")
        return is_report_saveish(split1) or is_report_saveish(split2)
    return is_safe


logging.getLogger().setLevel(logging.INFO)
reports = []
with open("big2.txt") as f:
    for line in f:
        line = line.replace("\n", "")
        report = [int(n) for n in line.split(" ")]
        reports.append(report)

save = 0
report_nodamp = []
for report in reports:
    if is_report_save(report):
        report_nodamp.append(report)
        save += 1

info(f"Part one, no problem dampener: {save}")
save = 0
reports_good = []
for report in reports:
    debug(f"_____________________Checking report {report}________________________")
    if result := is_report_saveish(report, True):
        reports_good.append(report)
        save += 1
    debug(f"______________________________Result is {result}____________________________________________")
info(f"Part two, with problem dampener: {save}")
