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

work_durations = []
def calc_work_time(times):
    work = times[0][1] - times[0][0]

    for i in range(len(times)):
        if i + 1 >= len(times): 
            work_durations.append(work)
            break # prevents list overflow

        if times[i+1][0] <= times[i][1] and times[i+1][1] > times[i][1]:
            work += times[i+1][1] - times[i][1]
        elif times[i+1][0] > times[i][1]:
            work_durations.append(work)
            calc_work_time(times[i+1:])
            break
    
    return max(work_durations)


def calc_idle_time(times):
    idle = 0

    for i in range(len(times)):
        if i + 1 >= len(times): break # prevents list overflow
        if times[0][1] > times[i][1]: continue
        if times[i+1][0] > times[i][1] and times[i+1][0] - times[i][1] > idle:
            idle = times[i+1][0] - times[i][1]

    return idle

def main():
    times = parse_input()
    work = calc_work_time(times)
    idle = calc_idle_time(times)

    print(work, idle)
    
    with open('milk2.out', 'w') as f:
        f.write(f'{work} {idle}\n')

if __name__ == '__main__':
    main()
