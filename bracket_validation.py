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

def bracket_evaluation(string):
    if check_validity(string):

        if string[0] == '(' and string[len(string) - 1] == ')':
            if string[1:len(string) - 1] == '':
                return 0
            else:
                return string[1:len(string) - 1]

        if string[0] == '[' and string[len(string) - 1] == ']':
            result = re.findall("\([^\d]*(\d+)[^\d]*\)", string)
            string_dupl = string
            total_sum = 0
            for n in result:
                total_sum += 2 * int(n)
                string_dupl = string_dupl.replace('({})'.format(n), ',')
            for i in re.findall('\d+', string_dupl):
                total_sum += int(i)
            return total_sum

        if string[0] == '{' and string[len(string) - 1] == '}':
            string_dupl = string
            total_sum = 0
            result = re.findall('\[([^]]*)\]', string)
            for r in result:
                string_dupl = string_dupl.replace('[{}]'.format(r), ',')
            new_str = ','.join(result)
            sub_result = re.findall("\([^\d]*(\d+)[^\d]*\)", new_str)
            for i in sub_result:
                total_sum += 4 * int(i)
            for n in sub_result:
                new_str = new_str.replace('({})'.format(n), ',')
            for number in re.findall("\d+", new_str):
                total_sum += 2 * int(number)
            for num in re.findall("\d+", string_dupl):
                total_sum += int(num)
            return total_sum

    else:
        return 'NO'




def main():
    print(check_validity('[123(145)38(37)812]'))
    print(bracket_evaluation('[123(145)38(37)812]'))
    print(bracket_evaluation('{125[2][(1)][3]125}'))
    print(bracket_evaluation('{2[123]3}'))
    print(bracket_evaluation(''))
    print(bracket_evaluation('{125()125}'))
    print(bracket_evaluation('{123[123(123)123(123)]23[123]2}'))
    print(bracket_evaluation('[123(123])'))
    print(bracket_evaluation('{125[2][(1)][3]125}'))
    print(bracket_evaluation('{125()125}'))
if __name__ == '__main__':
    main()
