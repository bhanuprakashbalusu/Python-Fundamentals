print('Imported my_module...')

test = 'Test String'


def find_index(to_search_in, target):
    ''' to find index of the value in a sequence '''
    for i, course in enumerate(to_search_in):
        if course == target:
            return i
    return -1
