from babel.dates import format_datetime


def number_with_character(text):
    result = ""
    for val in text:
        if val in "+()-_|\\/';:=":
            result += '\\' + val
        else:
            result += val
    return result


def is_phone_number(number):
    if len(number) < 10:
        return False
    for val in number:
        if val not in "+1234567890()- ":
            return False
    return True


def create_comment_data(data):
    result = {'number_id': data['id'], 'level_id': 1, 'comment': ''}

    if data.get('Dangerous'):
        result['level_id'] = 1
        result['comment'] = data['Dangerous']

    elif data.get('Tiresome'):
        result['level_id'] = 2
        result['comment'] = data['Tiresome']

    elif data.get('Neutral'):
        result['level_id'] = 3
        result['comment'] = data['Neutral']

    elif data.get('Safe'):
        result['level_id'] = 4
        result['comment'] = data['Safe']

    return result


def create_beautiful_comment(data):
    level = data[3]
    if level == 1:
        row1 = "🔴 Небезпечний"
    elif level == 2:
        row1 = "🟠 Надокучливий"
    elif level == 3:
        row1 = "🟡 Нейтральний"
    else:
        row1 = "🟢 Безпечний"
    content = data[1]
    date_create = format_datetime(data[2], 'd.MM.Y HH:mm', locale='uk_UA')
    result = f"*{row1}*\n"\
             "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
             f"{content}\n" \
             "➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
             f"👍🏼 *{data[5]}* | 👎🏼 *{data[6]}*\n\n" \
             f"_{date_create}_🕐"
    return result

