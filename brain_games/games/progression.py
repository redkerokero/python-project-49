import random

GAME_TASK = 'What number is missing in the progression?'
MAX_NUMBER = 99


def generate_progression(
    progression_length,
    max_number,
    delta_min_limit=-10,
    delta_max_limit=10,
):
    delta = random.randint(delta_min_limit, delta_max_limit)
    progression_item = str(random.randint(1, max_number))
    progression = [progression_item]
    for _ in range(progression_length - 1):
        progression_item = int(progression_item) + delta
        progression.append(str(progression_item))
    return progression


def hide_list_item(input_list):
    output_list = []
    rand_elem_index = random.randint(0, len(input_list) - 1)
    for index, element in enumerate(input_list):
        if index == rand_elem_index:
            output_list.append('..')
            hiden_element = element
        else:
            output_list.append(element)
    return output_list, hiden_element


def gen_question_answer(max_number):
    min_progression_length = 5
    max_progression_length = 15
    progression_length = random.randint(
        min_progression_length,
        max_progression_length,
    )
    progression = generate_progression(progression_length, max_number)
    question, answer = hide_list_item(progression)
    question = ' '.join(question)
    return question, answer
