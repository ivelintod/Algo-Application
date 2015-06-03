import re


def check_validity(string):
    list_duplicate = list(string)
    left_norm_brackets = []
    right_norm_brackets = []
    left_curly_brackets = []
    right_curly_brackets = []
    left_square_brackets = []
    right_square_brackets = []


    for onb in list_duplicate:
        if onb == '(':
            left_norm_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '
        elif onb == ')':
            right_norm_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '
        elif onb == '{':
            left_curly_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '
        elif onb == '}':
            right_curly_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '
        elif onb == '[':
            left_square_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '
        elif onb == ']':
            right_square_brackets.append(list_duplicate.index(onb))
            list_duplicate[list_duplicate.index(onb)] = ' '

    validity = []

    if len(left_norm_brackets) == len(right_norm_brackets) and len(left_square_brackets) == len(right_square_brackets) and len(left_curly_brackets) == len(right_curly_brackets) and string != '':
        for i in range(len(left_norm_brackets)):
            res = string[left_norm_brackets[i]:right_norm_brackets[i]][1:]
            for i in '()[]{}':
                validity.append(i not in res)

        for i in range(len(left_square_brackets)):
            res = string[left_square_brackets[i]:right_square_brackets[i]][1:]
            for i in '{}[]':
                validity.append(i not in res)
            if ('(' in res and ')' not in res) or (')' in res and '(' not in res):
                validity.append(False)

        for i in range(len(left_curly_brackets)):
            res = string[left_curly_brackets[i]:right_curly_brackets[i]][1:]
            #if res[0] == '(' or res[len(res) - 1] == ')':
             #   validity.append(False)
            if '(' in res:
                index = res.index('(')
                if '[' not in res[:index]:
                    validity.append(False)

        for i in string[1:len(string) - 1]:
            for i in '{}':
                validity.append(i not in res)

        if string[0] not in '([{' or string[len(string) - 1] not in '})]':
            validity.append(False)

        index1 = None
        index2 = None
        stripped_string = string[1:len(string) - 1]
        for i in range(len(stripped_string)):
            if stripped_string[i] == ')' or stripped_string[i] == ']' or stripped_string[i] == '}':
                index1 = stripped_string.index(stripped_string[i])
            if stripped_string[i] == '(' or stripped_string[i] == '[' or stripped_string[i] == '{':
                index2 = stripped_string.index(stripped_string[i])
        if index1 < index2:
            validity.append(False)

        return False not in validity

    else:
        return False


def distinct_sum(stripped_string):
    sum_digits = 0
    if len(stripped_string) == 1:
        sum_digits += int(stripped_string[0])
    if len(stripped_string) == 2:
        sum_digits += 10 * int(stripped_string[0]) + int(stripped_string[1])
    if len(stripped_string) == 3:
        sum_digits += 100 * int(stripped_string[0]) + 10 * int(stripped_string[1]) + int(stripped_string[2])
    return sum_digits


def bracket_evaluation(string):
    if check_validity(string):
        list_duplicate = list(string)
        left_norm_brackets = []
        right_norm_brackets = []
        left_curly_brackets = []
        right_curly_brackets = []
        left_square_brackets = []
        right_square_brackets = []
        ultimate_sum = 0

        for onb in list_duplicate:
            if onb == '(':
                left_norm_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '
            elif onb == ')':
                right_norm_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '
            elif onb == '{':
                left_curly_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '
            elif onb == '}':
                right_curly_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '
            elif onb == '[':
                left_square_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '
            elif onb == ']':
                right_square_brackets.append(list_duplicate.index(onb))
                list_duplicate[list_duplicate.index(onb)] = ' '

        duplicate = string
        ultimate_sum = 0
        left_norm_inner_brackets = []
        right_norm_inner_brackets = []

        if string[0] == '(' and string[len(string) - 1] == ')':
            if string[1:len(string) - 1] == '':
                return 0
            else:
                return string[1:len(string) - 1]
        if string[0] == '[' and string[len(string) - 1] == ']':
            for i in range(len(left_norm_brackets)):
                res = string[left_norm_brackets[i]:right_norm_brackets[i]][1:]
                ultimate_sum += 2 * distinct_sum(res)
                duplicate = duplicate.replace('({})'.format(res), ',')
            numbers_clean = re.findall('\d+', duplicate)
            for n in numbers_clean:
                ultimate_sum += int(n)
            return ultimate_sum

        if string[0] == '{' and string[len(string) - 1] == '}':
            for i in range(len(left_square_brackets)):
                res = string[left_square_brackets[i]:right_square_brackets[i]][1:]
                list_duplicate2 = list(res)
                if '(' in list_duplicate2:
                    left_norm_inner_brackets.append(list_duplicate2.index('('))
                if ')' in list_duplicate2:
                    right_norm_inner_brackets.append(list_duplicate2.index(')'))
                for i in range(len(left_norm_inner_brackets)):
                    new_res = res[left_norm_inner_brackets[i]:right_norm_inner_brackets[i]][1:]
                    ultimate_sum += 2 * distinct_sum(new_res)
                    duplicate = duplicate.replace('({})'.format(new_res), ',')
                numbers_clean = re.findall('\d+', duplicate)
                for n in numbers_clean:
                    ultimate_sum += int(n)
            return ultimate_sum

    else:
        return 'NO'




def main():
    print(check_validity('[123(145)38(37)812]'))
    print(bracket_evaluation('[123(145)38(37)812]'))
    print(bracket_evaluation('{125[2][(1)][3]125}'))
    print(bracket_evaluation('{2[123]3}'))
    print(bracket_evaluation(''))
    print(bracket_evaluation('{125()125}'))
if __name__ == '__main__':
    main()
