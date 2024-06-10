multidimensional_dict = {
        'first_level': {
             'second_level_1': {
                     'third_level_1': 1,
                     'third_level_2': 2
               },
        'second_level_2': {
                    'third_level_3': 3,
                    'third_level_4': 4
                   }
              },
 'another_first_level': {
                'second_level_3': {
                             'third_level_5': 5,
                             'third_level_6': 6
                             },
              'second_level_4': {
                            'third_level_7': 7,
                            'third_level_8': 8
                    }
             }
        }
#taking above example dictionary
value = multidimensional_dict['first_level']['second_level_1']['third_level_2']
print(value)

multidimensional_dict['new_first_level'] = {'new_second_level': {'new_third_level': 100}}
print(multidimensional_dict)

for first_level_key, second_level_dict in multidimensional_dict.items():
    print(f"First Level Key: {first_level_key}")

    for second_level_key, third_level_dict in second_level_dict.items():
        print(f"  Second Level Key: {second_level_key}")

        for third_level_key, value in third_level_dict.items():
            print(f"    Third Level Key: {third_level_key}, Value: {value}")
