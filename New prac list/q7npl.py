def menustr():
    print('\n 1.Length of string\n 2.Max of three\n 3.Replace vowels with #\n 4.Number of Words\n 5.Check palindrome')
    v = int(input('Enter your choice : '))
    return v

choice = menustr()
while choice != 0:
    if choice == 1:
        s1 = str(input('Enter String: '))
        print('Length of String is ', len(s1))

    elif choice == 2:
        str1 = str(input('Enter String 1: '))
        str2 = str(input('Enter String 2: '))
        str3 = str(input('Enter String 3: '))

        print(max(str1, str2, str3))

    elif choice == 3:
            str1 = str(input("Enter any string: "))
            vowels = ['a', 'e', 'i', 'o', 'u']
            for c in vowels:
                str1 = str1.replace(c, '#')
            print("New String: ", str1)

    elif choice == 4:
        str = str(input('Enter a String: '))
        print('Number of words: ', len(str.split()))

    elif choice == 5:
        def isPalindrome(s):
            return s == s[::-1]

        s = str(input('Enter String: '))
        ans = isPalindrome(s)
        if ans:
            print('Is Palindrome')
        else:
            print('Is not Palindrome')
    else:
        print('Invalid choice')

    choice = menustr()
