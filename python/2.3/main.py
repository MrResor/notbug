def main():
    print('Get users from Poland.')
    # missing } after dict with name Kamil
    # assuming that no country indicates someone is not from Poland
    users = [{"name": "Kamil", "country":"Poland"}, {"name":"John", "country": "USA"}, {"name":"Yeti"}]
    print('Initial list of users:')
    print(users)
    # filter out users without country key to not cause errors when finding only PL users
    have_country = [user for user in users if "country" in user.keys()]
    PL_users = [user for user in have_country if user["country"] == "Poland"]
    print('Users from Poland:')
    print(PL_users)

    print('-' * 25)

    print('Sum of first 10 elements, starting from 5th element.')
    numbers = [1,5,2,3,1,4,1,23,12,2,3,1,2,31,23,1,2,3,1,23,1,2,3,123]
    print('List of numbers:')
    print(numbers)
    # python indexes from 0, so under index 4 we have 5th element of the array
    # while splicing arrays the value under second index is not taken into consideration (in this case 23)
    res = sum(numbers[4:14])
    print('Sum of numbers:')
    print(res)

    print('-' * 25)

    print('List with powers of 2.')
    # checked with timeit, faster than 2**n 
    powers = [1<<n for n in range(1,21)]
    print('The list:')
    print(powers)
    
if __name__ == "__main__":
    main()