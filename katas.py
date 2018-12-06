def tribonacci(signature, n):
    result = signature[:n]
    for number in range(3, n):
        result.append(sum(result[number - 3:number]))
    return result


def how_many_bees(hive):
    result = 0
    try:
        line_length = len(hive[0])
    except (IndexError, TypeError):
        return result
    for line_index in range(len(hive)):
        for char_index in range(len(hive[line_index])):
            if hive[line_index][char_index] == "b":
                if line_index > 1 and hive[line_index-2][char_index] + hive[line_index-1][char_index] == "ee":
                    result += 1
                if line_index < hive.index(hive[-2]) and hive[line_index+1][char_index] + hive[line_index+2][char_index] == "ee":
                    result += 1
                if char_index > 1 and hive[line_index][char_index-2:char_index] == "ee":
                    result += 1
                if char_index < line_length - 2 and hive[line_index][char_index+1:char_index+3] == "ee":
                    result += 1
    return result


def bowling_pins(arr):
    bullshit = {}
    for number in range(1, 11):
        if number in arr:
            bullshit[str(number) + "babu"] = ""
        else:
            bullshit[str(number) + "babu"] = "I"
    result = "{7babu} {8babu} {9babu} {10babu}\n {4babu} {5babu} {6babu} \n  {2babu} {3babu}  \n   {1babu}   ".format(
        **bullshit, sep="")
    return result
