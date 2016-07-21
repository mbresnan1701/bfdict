#!/usr/bin/env python3
import os

password = '!abba919'
common_subs = {
  'l': '1',
  'e': '3',
  'a': '4',
  't': '7',
  'o': '0',
  's': '$',
}
dict_and_target_lists = [os.getcwd() + "/target.txt",
                         os.getcwd() + "/words.txt"]
preset_lists = [os.getcwd() + "/topPWList.txt"]


def uniquify(seq):
    my_set = set(seq)
    return list(my_set)


def do_variations(word):
    results = [word]

    def get_variations(word, index):
        for idx, val in enumerate(range(index, len(word))):

            if word[idx] in common_subs:
                temp = list(word)
                temp[idx] = common_subs[temp[idx]]
                temp = ''.join(temp)
                results.append(temp)
                get_variations(temp, idx)

    get_variations(word, 0)

    return uniquify(results)


def test_guess(string):
    return string == password


def do_preset_lists():
    found = False
    for item in preset_lists:
        if found is False:
            result = None
            with open(item, "r") as f:
                for item in f:
                    result = test_guess(item.strip())
                    if result is True:
                        found = item
                        break

    return found


def do_word(word):
    print(word)
    variations = do_variations(word)
    for item in variations:
        for num in list(range(1, 3000)):
            if test_guess(item + str(num)):
                return item + str(num)
            if test_guess(item + str(num) + '!'):
                return item + str(num) + '!'
            if test_guess('!' + item + str(num)):
                return '!' + item + str(num)

    return False


def main():
    result = do_preset_lists()
    if result is not False:
        print("Got it! PW was {}".format(result))
    else:
        for item in dict_and_target_lists:
            if result is False:
                with open(item, "r") as f:
                    for item in f:
                        result = do_word(item.strip().lower())
                        if result is not False:
                            print("Got it! PW was {}".format(result))
                            break

        if result is False:
            print("Counldn't find it, Master. I have failed you.")


if __name__ == '__main__':
    main()
