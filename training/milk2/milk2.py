"""
ID: Aarush Narang [anarang2]
LANG: PYTHON3
TASK: milk2
"""

def parse_input():
    with open('milk2.in', 'r') as f:
        lines = f.read().strip().split('\n')
        times = [[int(line.split(' ')[0]), int(line.split(' ')[1])] for line in lines[1:]]
        times.sort()

    return times

def calc_work_time(times):
    t = [times[0][0], times[0][1]]

    for i in range(len(times)):
        if i + 1 >= len(times): break # prevents list overflow

        if times[i+1][0] <= t[1] and times[i+1][1] > t[1]: # if the next pair's start time is before the end time of the current pair, merge them into one duration
            t[1] = times[i+1][1]
        elif times[i+1][0] > t[1]: # if the next pair's start time is after the end time of the current pair's end time, 
            if t[1] - t[0] < times[i+1][1] - times[i+1][0]: # check if the duration of the current pair is longer than the previous pair/merged pair
                t = [times[i+1][0], times[i+1][1]]
    
    idle = calc_idle_time(times, t[0], t[1])
    work = t[1] - t[0]

    return work, idle

def calc_idle_time(times, overlap_start, overlap_end):
    # remove overlapping times
    for i in range(len(times)):
        if times[i][0] > overlap_start and times[i][1] < overlap_end:
            times[i] = [None, None]
        if times[i][0] == overlap_start:
            times[i] = [None, None]
        if times[i][1] == overlap_end:
            times[i] = [None, None]

    # append work start time and end time to list (total overlap time)
    times.append([overlap_start, overlap_end])

    # calculate idle time
    # first remove all lists with None values
    times = [t for t in times if t != [None, None]]
    times.sort()

    if len(times) == 1: return 0 # if there is only one pair of times, there is no idle time
    t = [0, 0]
    
    for i in range(len(times)):
        if i + 1 >= len(times): break # prevents list overflow
        if times[i+1][0] > times[i][1] and times[i+1][0] - times[i][1] > t[1] - t[0]:
            t = [times[i][1], times[i+1][0]]
  
    idle = t[1] - t[0]

    return idle

def main():
    times = parse_input()
    (work, idle) = calc_work_time(times)

    with open('milk2.out', 'w') as f:
        f.write(f'{work} {idle}\n')

if __name__ == '__main__':
    main()
