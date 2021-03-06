from babel.dates import format_datetime
import phonenumbers

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
        return False, number
    try:
        phone = phonenumbers.parse(number, "UA")
        if len(phone.national_number.__str__()) != 9:
            return False, number
        print(phone)
        number = "+" + phone.country_code.__str__() + phone.national_number.__str__()
    except:
        print('EROR')
        return False, number

    return True, number


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
        row1 = "π΄ ΠΠ΅Π±Π΅Π·ΠΏΠ΅ΡΠ½ΠΈΠΉ"
    elif level == 2:
        row1 = "π  ΠΠ°Π΄ΠΎΠΊΡΡΠ»ΠΈΠ²ΠΈΠΉ"
    elif level == 3:
        row1 = "π‘ ΠΠ΅ΠΉΡΡΠ°Π»ΡΠ½ΠΈΠΉ"
    else:
        row1 = "π’ ΠΠ΅Π·ΠΏΠ΅ΡΠ½ΠΈΠΉ"
    content = data[1]
    date_create = format_datetime(data[2], 'd.MM.Y HH:mm', locale='uk_UA')
    result = f"*{row1}*\n"\
             "ββββββββββββββββββ\n" \
             f"{content}\n" \
             "ββββββββββββββββββ\n" \
             f"_{date_create}_π"
    return result

#  f"ππΌ *{data[5]}* | ππΌ *{data[6]}*\n\n" \

def create_beautiful_qa(data):
    result = f"β *{data[2]}*\n\n" \
             f"- - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -   - - -\n" \
             f"\nβ«οΈ {data[3]}"

    return result

def get_category_icon(category):
    cicon = ""
    if category == "last_view":
        cicon = "πβπ¨"
    elif category == "popular_view":
        cicon = "πβπ¨"
    elif category == "max_comment":
        cicon = "π"
    return cicon