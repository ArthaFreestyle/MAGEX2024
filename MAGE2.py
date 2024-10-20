N = input()

end = N.find(')')

if (len(N) - end) == end:
    print('TRUE')
else:
    print('FALSE')