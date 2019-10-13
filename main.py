number = int(input("Input a number between 1 and 3999: "))

if number < 1 or number > 3999 :
    print("Invalid number")
    exit() 

roman_numerals = [['M',1000], ['D',500], ['C',100], ['L',50], ['X',10], ['V',5], ['I',1]]

def solve(number, step_index = 0, result = '') :
    symbol = roman_numerals[step_index][0]
    step = roman_numerals[step_index][1]

    # Trivial case
    if number == 0 :
        return result
    # 42 => 50 + 2; 422 => 500 + 22 
    elif number >= 4 * step :
        result += symbol
        return solve(number - 4 * step + roman_numerals[step_index - 1][1], step_index - 1, result)
    # 57 => 7
    elif number > step :
        result += symbol
        return solve(number - step, step_index, result)
    # Trivial case
    elif number == step :
        return result + symbol
    # 92 => 102
    elif number >= step * 9 / 10 :
        result += roman_numerals[step_index + 2][0]
        return solve(number + step / 10, step_index, result)
    # Number lower than step; 82 => 82 - 50 = 32
    else :
        return solve(number, step_index +1, result)
    
print (number, '=', solve(number))
