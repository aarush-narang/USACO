"""
ID: Aarush Narang [anarang2]
LANG: PYTHON3
TASK: beads
"""

def main():
    with open('beads.in', 'r') as f:
        beads_string = f.readlines()[1].strip()

    if len(set(beads_string)) == 1: # if all characters are the same, just return the length of the string
        return len(beads_string)
    
    most_beads = 0 # the most beads, updated as the for loop runs

    for i in range(len(beads_string)): # move a "pointer" through the string
        n = 0 # temporary variable to keep track of the number of beads
        right_start = beads_string[i] # the character on the pointer
        left_start = beads_string[i-1]  # the character to the left of the pointer

        right_arr = beads_string[i:]+beads_string[:i] # the string to the right of the pointer concatenated with the string to the left of the pointer
        left_arr = beads_string[i-1::-1] + beads_string[:i-1:-1] # the string to the right of the pointer reversed (to get the left side of the necklace) concatenated with the string to the left of the pointer reversed

        # for each character in the right side, if the character is the same as right_start or equal to w, add 1 to n. If the index of the character reaches the pointer, 
        # break so these beads are not repeated as they will be counted on the left side
        for right_i in range(len(right_arr)):
            if right_arr[right_i] != right_start and right_start == 'w': # check if the starting character is equal to w and if it is, replace it with the next character not equal to w
                right_start = right_arr[right_i]
            if right_i == i:
                break
            if right_arr[right_i] == right_start or right_arr[right_i] == 'w':
                n+=1
            else:
                break
        
        # for each character in the left side, if the character is the same as left_stwart or equal to w, add 1 to n. We do not need to check if the index = to the pointer because these beads were not counted in the right side.
        for left_i in range(len(left_arr)):
            if left_arr[left_i] != left_start and left_start == 'w': # check if the starting character is equal to w and if it is, replace it with the next character not equal to w
                left_start = left_arr[left_i]
            if left_arr[left_i] == left_start or left_arr[left_i] == 'w':
                n+=1
            else:
                break

        if n > most_beads:
            most_beads = n

    return most_beads

if __name__ == '__main__':
    with open('beads.out', 'w') as f:
        f.write(str(main()) + '\n')
