def check_cards_part_one(file):
    with open(file, 'r') as f:
        txt_card_nums = f.readlines()

    txt_card_nums = list(map(lambda s : s.replace('\n', ''), txt_card_nums))

    list_of_winning_values = []

    for card in txt_card_nums:
        [winning_nums, nums_you_have] = card.split('|')
        list_nums_you_have = list(filter(lambda x: not x == "", nums_you_have.split(" ")))
        list_winning_nums = list(filter(lambda x: not x == "", winning_nums.split(" ")))
        score = 0
        is_first = False

        for num in list_nums_you_have:
            if num in list_winning_nums:
                # if it's the first number just add one otherwise double the next winner(s)
                if is_first:
                    score *= 2
                else:
                    is_first = True
                    score += 1
        list_of_winning_values.append(score)

    return list_of_winning_values

def check_cards_part_two(file):
    with open(file, 'r') as f:
        txt_card_nums = f.readlines()

    txt_card_nums = list(map(lambda s : s.replace('\n', ''), txt_card_nums))

    list_of_winning_values = []

    # each card will hold the value of how many winners there are and the number of times the card was won
    # example: {
    #   "1" : num_of_times
    # }
    card_no = {}

    for i in range(len(txt_card_nums)):
        card_no[i + 1] = 1

    for index, card in enumerate(txt_card_nums):
        [winning_nums, nums_you_have] = card.split('|')
        list_nums_you_have = list(filter(lambda x: not x == "", nums_you_have.split(" ")))
        list_winning_nums = list(filter(lambda x: not x == "", winning_nums.split(" ")))
        score = 0

        for num in list_nums_you_have:
            if num in list_winning_nums:
                score += 1

        j = 1
        # make sure to iterate over each time the number of cards that exist
        for x in range(card_no[index + 1]):
            while j <= score:
                card_no.update({index + 1 + j: (card_no[index + 1 + j] + 1)})
                j += 1
            j = 1

    # continue to update based on the number of cards won per card 
    for key in card_no:
        list_of_winning_values.append(card_no[key])

    return list_of_winning_values