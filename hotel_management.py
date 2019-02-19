
hotel = {
    '1': {
        '101': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}


def check_in_out():
    user_input_check_in_out = input('Would you like to check in or check out?')
    user_input_floor = input('what floor number?: ')
    user_input_room = input('what room number?: ')

    if user_input_check_in_out == 'check in':
        # hotel[user_input_floor][user_input_room] =
        occupant_number = int(input('number of occupants?: '))

        occupant_names = input('what are occupant names?: ')

    if user_input_check_in_out == 'check out':
        hotel['1'][]

    #directions:
# Write a program that works with this hotel data:

# Display a menu asking whether to check in or check out.
# Prompt the user for a floor number, then a room number.
# If checking in, ask for the number of occupants and what their names are.
### asking for number of occupants -> create values for key(room) & setting customer names to the value
# If checking out, remove the occupants from that room.
### 
# Do not allow anyone to check into a room that is already occupied.
# Do not allow checking out of a room that isn't occupied.



    #questions: