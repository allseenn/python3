import pandas as pd
import random
import datetime
import os

MENU = "\
1. Open base\n\
2. Generate base\n\
3. Save base\n\
4 Ops with records\n\
5! Export to ; \n\
6! Export to , \n\
7! Import ; \n\
8! Import ,\n\
9. Clean base\n\
0. Delete base\n\
Enter a number or q(uit): "

SUBMENU = "\
i. set id\n\
l. set last name\n\
f. set first name\n\
o. set middle name\n\
b. set birthday\n\
c. set mobile\n\
p. set phone\n\
s. search records\n\
a. add/update record\n\
d. delete record\n\
REC: "

# 1 Open base
def open_base(filename: str = "base.csv") -> pd.DataFrame:
    if os.path.isfile(filename):
        try:
            base = pd.read_csv(filename, dtype=str)
        except BaseException as error:
            return f"Error! {error}"
        return base
    else:
        return "File not found, make new one or save base"
# 2 Generate base
def new_base(size: int = 200) -> pd.DataFrame :
    syllables = ['ба', 'бо', 'бу', 'бы', 'би', 'бя', 'бю', 'бе', 'ва', 'во', 'ву', 'вы', 'вэ', 'ви', 'вя', 'вю', 'ве', 'да', 'до', 'ду', 'ды', 'ди', 'дя', 'дю', 'де', 'га', 'го', 'гу', 'ги', 'гя', 'гю', 'ге', 'за', 'зо', 'зу', 'зи', 'зя', 'зю', 'зе', 'ка', 'ко', 'ку', 'ки', 'кя', 'кю', 'ке', 'са', 'со', 'су', 'сы', 'си', 'ся', 'сю', 'се', 'па', 'по', 'пу', 'пы', 'пи', 'пя', 'пю', 'пе', 'жа', 'жо', 'жу', 'жи', 'жю', 'же', 'ла', 'ло', 'лу', 'лы', 'ли', 'ля', 'лю', 'ле', 'ма', 'мо', 'му', 'мы', 'ми', 'мя', 'мю', 'ме', 'на', 'но', 'ну', 'ны', 'ни', 'ня', 'ню', 'не', 'ра', 'ро', 'ру', 'ри', 'ря', 'рю', 'ре', 'та', 'то', 'ту', 'ти', 'тя', 'тю', 'те', 'ха', 'хо', 'ху', 'хи', 'хя', 'хю', 'хе', 'ца', 'цо', 'цу', 'ци', 'це', 'ша', 'шо', 'шу', 'ши', 'ше', 'ща', 'що', 'щу', 'щи', 'ще', 'ча', 'чо', 'чу', 'чи', 'че', 'фа', 'фо', 'фу', 'фи', 'фя', 'фе', 'аб', 'об', 'уб', 'иб', 'яб', 'юб', 'ав', 'ов', 'ув', 'ив', 'яв', 'юв', 'ев', 'ад', 'од', 'уд', 'ид', 'яд', 'юд', 'ед', 'аг', 'ог', 'уг', 'иг', 'яг', 'юг', 'ег', 'аз', 'оз', 'уз', 'из', 'яз', 'юз', 'ез', 'ак', 'ок', 'ук', 'ик', 'як', 'юк', 'ек', 'ас', 'ос', 'ус', 'ис', 'яс', 'юс', 'ес', 'ап', 'оп', 'уп', 'ип', 'яп', 'юп', 'аж', 'ож', 'уж', 'иж', 'юж', 'еж', 'ал', 'ол', 'ул', 'ил', 'ял', 'юл', 'ел', 'ам', 'ом', 'ум', 'им', 'ям', 'юм', 'ем', 'ан', 'он', 'ун', 'ин', 'ян', 'юн', 'ен', 'ар', 'ор', 'ур', 'ир', 'яр', 'юр', 'ер', 'ат', 'от', 'ут', 'ит', 'ят', 'ют', 'ет', 'ах', 'ох', 'ух', 'их', 'ях', 'юх', 'ех', 'ац', 'оц', 'уц', 'иц', 'яц', 'юц', 'ец', 'аш', 'ош', 'уш', 'иш', 'яш', 'юш', 'еш', 'ач', 'оч', 'уч', 'ич', 'яч', 'юч', 'еч', 'аф', 'оф', 'уф', 'иф', 'яф', 'юф', 'еф']
    endings = ['лин', 'лов', 'нин', 'нов', 'шин', 'шов', 'рин', 'ров', 'пин', 'пов', 'ков', 'кин', 'ко', 'кий', 'ций', 'вич', 'цев', 'цов', 'цин']
    names = ['Андрей', 'Борис', 'Владимир', 'Георгий', 'Дмитрий', 'Евгений', 'Иосиф', 'Кирилл', 'Леонид', 'Михаил', 'Николай', 'Олег', 'Петр', 'Роман', 'Сергей', 'Тимофей', 'Умар', 'Фёдор', 'Харитон', 'Эмануил', 'Юрий', 'Яков']
    middles = ['Андреевич', 'Борисович', 'Владимирович', 'Георгиевич', 'Дмитриевич', 'Евгеньевич', 'Иосифович', 'Кириллович', 'Леонидович', 'Михаилович', 'Николаевич', 'Олегович', 'Петрович', 'Романович', 'Сергеевич', 'Тимофеевич', 'Умарович', 'Фёдорович', 'Харитонович', 'Эмануилович', 'Юрьевич', 'Яковлевич']
    mobile_prefix = ['910', '915', '916', '917', '919', '985', '986', '903', '905', '906', '909', '962', '963', '964', '965', '966', '967', '968', '969', '980', '983', '986', '925', '926', '929', '936', '999', '901', '958', '977', '999', '995', '996', '999']
    phone_prefix = ['495', '499', '498']
    soc_id = pd.Series([str(i) for i in range(11111, 11111+size)])
    last_name = pd.Series([''.join(random.sample(syllables, random.randint(2, 3)) + random.sample(endings, 1)).title() for i in range(size)])
    first_name = pd.Series(["".join(random.sample(names, 1)) for i in range(size)])
    middle_name = pd.Series(["".join(random.sample(middles, 1)) for i in range(size)])
    birth_day = pd.Series([datetime.date.fromtimestamp(random.randint(0, 1000000000)).strftime('%Y-%m-%d') for i in range(size)]) # , dtype='datetime64[ns]'
    mobile = pd.Series(['8' + ''.join(random.sample(mobile_prefix, 1)) + str(random.randint(1111111, 9999999)) for i in range(size)])
    phone = pd.Series(['8' + ''.join(random.sample(phone_prefix, 1)) + str(random.randint(1111111, 9999999)) for i in range(size)])
    base = pd.DataFrame({ 'id': soc_id,
                        'last': last_name,
                        'first': first_name,
                        'middle': middle_name,
                        'birth': birth_day,
                        'cell': mobile,
                        'tel': phone
                        })
    #base.set_index("id")
    return base
# 3 Save base
def save_base(base: pd.DataFrame, filename: str = "base.csv") -> str:
    if os.path.isfile(filename):
        try:
           base.to_csv(filename, index=False)
        except BaseException as error:
            return f"Error! {error}"
        return f"File {filename} id updated"
    else:
        try:
           base.to_csv(filename, index=False)
        except BaseException as error:
            return f"Error! {error}"
        return f"File {filename} id created"
#!4 Find record
def find_record(base: pd.DataFrame,  record: list) -> pd.DataFrame:
    columns = ["id", "last", "first", "middle", "birth", "cell", "tel"]
    que = " & ".join([f'{columns[i]} == "{record[i]}"' for i in range(len(columns)) if record[i] != ""])
    try:
        find = base.query(que)
    except BaseException as error:
            return f"Error! {error}"
    return find
#!5 Change record
def change_record(base: pd.DataFrame,  record: list) -> pd.DataFrame:
    length = [len(base)]
    base.loc[length[0]] = length + record
    return base
#!6 Add record
def add_record(base: pd.DataFrame,  record: list) -> pd.DataFrame:
    record[0] = str(random.randint(22222,99999))
    base.loc[record[0]] = record
    return base
#!7 Import records
def import_record(base: pd.DataFrame,  record: list) -> pd.DataFrame:
    length = [len(base)]
    base.loc[length[0]] = length + record
    return base
#!8 Delete records
def del_record(base: pd.DataFrame,  record: list) -> pd.DataFrame:
    if record[0] != "":
        base.drop(base[base.id == record[0]].index, inplace=True)
    else:
        return f"Введите id для удаления"
    return base
# 9. Clean base
def clean_base(base: pd.DataFrame) -> pd.DataFrame:
    base = pd.DataFrame()
    return base
# 0. Delete base
def del_file(filename: str) -> str:
    if os.path.isfile(filename):
        os.remove(filename)
        return f"{filename} deleted"
    else:
        return f"{filename} not found"

# main menu 10 digits
def menu():
    base = pd.DataFrame()
    choice = ""
    msg = "Main DBS menu"
    while choice != "q":
        os.system('cls')
        print(f"MSG: {msg}")
        choice = input(MENU)
        match choice:
            case "1": # open base from file
                filename = input("Enter base.csv name: ")
                filename = "base.csv" if filename == "" else filename
                base = open_base(filename)
                msg = "Base is open" if type(base) != str else base
            case "2": # generate new base in memory
                size = int(input("How many records generate?: "))
                base = new_base(size)
                msg = f"Generated {len(base)} rows" if type(base) != str else base
            case "3": # save base to file
                filename = input("Enter base.csv name: ")
                filename = "base.csv" if filename == "" else filename 
                msg = save_base(base, filename)
            case "4": # Ops with records
                submenu(base)
            case "9": # clean base
                base = input("Enter word 'base' in prompt: ") 
                base = clean_base(base)
                msg = "Database is clean" if base.empty else f"MSG:Database contains {len(base)} rows"
            case "0": # delete base
                filename = input("Enter filename to delete: ") 
                msg = del_file(filename)
    return print("Good by!")
# Submenu 10 chars
def submenu(base):
    choice = ""
    msg = "Edit, delete, add or update records"
    record = ["", "", "", "", "", "", ""]
    while choice != "m":
        os.system('cls')
        print(f"MSG: {msg}")
        print(SUBMENU, end="")
        print(*record)
        choice = input("Enter a char, m(enu) or q(uit): ")
        match choice:
            case "i": # i. set id
                record[0] = input("edit id: ")
                # base = open_base(filename)
                # msg = "Base is open" if type(base) != str else base
            case "l": # l. set last name
                record[1] = input("edit last name: ")
            case "f": # f. set first name
                record[2] = input("edit first name: ")
            case "o": # o. set middle name
                record[3] = input("edit middle name: ")
            case "b": # b. set birthday
                record[4] = input("edit birth day: ")
            case "c": # c. set mobile
                record[5] = input("edit cellular: ")
            case "p": # p. set phone
                record[6] = input("edit phone: ")
            case "s": # s. search records
                print(find_record(base, record))
                # if find != str:
                #     print(find)
                # else:
                #     print(find)
                choice = input("d(elete), u(pdate):")
            case "a": # a. add/update record
                base = add_record(base, record)
                msg = "Record was added" if type(base) != str else base
            case "d": # d. delete record
                base = del_record(base, record)
                msg = "Record was deleted" if type(base) != str else base
            case "q":
                exit()
    return base

menu()
