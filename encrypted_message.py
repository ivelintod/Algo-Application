import re


def find_numbers_helper(string):
    return re.findall('\d+', string)


def multiple_replace(string, list_replace):
    for i in list_replace:
        string = string.replace(i, '')
    string = string.replace('~', '')
    return string


def get_key(string, cycle):
    key = string[::-1][:cycle][::-1]
    return key


def remove_key(string, cycle):
    list1 = list(string)
    count = 1
    for i in range(cycle):
        list1[len(list1) - count] = ''
        count += 1
    return ''.join(list1)


def recreate_compound_key(encrypted_message, key):
    count = 0
    new_key = ''
    for i in encrypted_message:
        if count == len(key):
            count = 0
        new_key += key[count]
        count += 1
    return new_key


def get_indices(key, alphabet):
    alphabet_indices = []
    for i in key:
        alphabet_indices.append(alphabet.index(i))
    return alphabet_indices


def reverse_modulo(key_indices, encr_mess_indices, a_length):
    for i in range(len(key_indices)):
        if encr_mess_indices[i] < key_indices[i]:
            encr_mess_indices[i] += a_length
    return encr_mess_indices


def get_message_indices(key_indices, sum_indices):
    message_indices = []
    for i in range(len(key_indices)):
        message_indices.append(sum_indices[i] - key_indices[i])
    return message_indices


def recreate_message(message_indices, alphabet):
    message = ''
    for i in message_indices:
        message += alphabet[i]
    return message


def decrypt(string):
    step1 = string[len(string) // 2:] + string[:len(string) // 2]
    print(step1)
    lengths = find_numbers_helper(step1)
    print(lengths)
    a_length = lengths[0]
    k_length = lengths[1]
    print(a_length)
    print(k_length)
    no_lengths = multiple_replace(step1, lengths)
    print(no_lengths)
    key = get_key(no_lengths, int(k_length))
    print(key)
    no_len_removed_key = remove_key(no_lengths, int(k_length))
    print(no_len_removed_key)
    alphabet = no_len_removed_key[:int(a_length)]
    encrypted_message = no_len_removed_key[int(a_length):]
    print(alphabet)
    print(encrypted_message)
    compound_key = recreate_compound_key(encrypted_message, key)
    print(compound_key)
    key_indices = get_indices(compound_key, alphabet)
    encr_mess_indices = get_indices(encrypted_message, alphabet)
    print(key_indices)
    print(encr_mess_indices)
    sum_indices = reverse_modulo(key_indices, encr_mess_indices, int(a_length))
    print(sum_indices)
    message_indices = get_message_indices(key_indices, sum_indices)
    print(message_indices)
    message = recreate_message(message_indices, alphabet)
    print(message)



def main():
    decrypt('o?uin uw?stutnfwat?~413~orwa? thfuisnnrsiu')


if __name__ == '__main__':
    main()
