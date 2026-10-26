def brute_force(text,patern):
    patern_positions=[]
    pattern_len=len(patern)
    for i in range(len(text)-pattern_len+1):
        cur_text=text[i:i+pattern_len]
        if cur_text == patern:
            patern_positions.append(i)
    return patern_positions
#print(brute_force("AAAA", "AA"))

def suffix_array(text):
    substring_dict={}
    for i in range(len(text)):
        substring=text[i:]
        substring_dict[i]=substring
    substring_sorted=sorted(
        substring_dict.items(),
        key=lambda item: (0 if item[1].startswith('$') else 1, item[1])
    )

    key_list_ordered = [t[0] for t in substring_sorted]
    return key_list_ordered
#print(suffix_array("AAGGCGGCTTCA$"))

def find_block(text,sa,p):

    left, right = 0, len(sa) - 1
    first_index = -1
    while left <= right:
        mid = (left + right) // 2
        if text[sa[mid]:].startswith(p):
            first_index = mid
            right = mid - 1  # search left for earlier match
        elif text[sa[mid]:] < p:
            left = mid + 1
        else:
            right = mid - 1

    # Binary search for last match
    left, right = 0, len(sa) - 1
    last_index = -1
    while left <= right:
        mid = (left + right) // 2
        if text[sa[mid]:].startswith(p):
            last_index = mid
            left = mid + 1  # search right for later match
        elif text[sa[mid]:] < p:
            left = mid + 1
        else:
            right = mid - 1

    # Output matches
    if first_index != -1:
        matches = sa[first_index:last_index + 1]
        print("Matches:", matches)
    else:
        print("No matches found.")
    return None
#print(find_block("AAGGCGGCTTCA$",suffix_array("AAGGCGGCTTCA$"),"GGC"))

def bwt(text,sa):
    bwt_string=""
    for row in sa:
        if row==0:
            letter ="$"
        else:
            letter=text[row-1]
        bwt_string=bwt_string+letter
    return bwt_string

def first_occurrence(letters):
    output={}
    chars = list(letters)
    chars.sort(key=lambda c: (0 if c == '$' else 1, c))
    for i, ch in enumerate(chars):
        if ch not in output:  # first occurrence only
            output[ch] = i
    return output

print(first_occurrence("TC$A"))
