import pandas as pd
import random
import datetime
import os

MENU = "\
1. Open base from file\n\
2. Generate new base\n\
3. Save base to file\n\
4. Find record in base\n\
5. Add record to base\n\
6. Update record in base\n\
7. Delete record in base\n\
8. Delete base file\n\
9. Clean base\n\
0. Import/Export\n\
Enter a number or q(uit): "

SUBMENU = "\
i. set id\n\
l. set last name\n\
n. set first name\n\
m. set middle name\n\
b. set birthday\n\
c. set mobile\n\
p. set phone\n\
k. kill buffer\n\
BUF: "

PORT = "\
ic. imports csv to base\n\
ij. import json to base\n\
ec. export to csv file\n\
ej. export to json file\n\
bc. buffer to csv file\n\
bj. buffer to json file\n\
BUF: "

record = ["", "", "", "", "", "", ""]
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
# 2 Generate new base
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
    base = pd.DataFrame({ 'id': soc_id, 'last': last_name, 'first': first_name, 'middle': middle_name, 'birth': birth_day, 'cell': mobile, 'tel': phone })
    return base
# 3. Save base to file
def save_base(base: pd.DataFrame, filename: str = "base.csv") -> str:
    if os.path.isfile(filename):
        try:
           base.to_csv(filename, index=False)
        except BaseException as error:
            return f"Error! {error}"
        return f"File {filename} is updated"
    else:
        try:
           base.to_csv(filename, index=False)
        except BaseException as error:
            return f"Error! {error}"
        return f"File {filename} is created"
# 4. Find record in base
def find_record(base: pd.DataFrame) -> pd.DataFrame:
    columns = list(base.columns.values)
    que = " & ".join([f'{columns[i]} == "{record[i]}"' for i in range(len(columns)) if record[i] != ""])
    try:
        find = base.query(que)
    except BaseException as error:
            return f"Error! {error}"
    return "Not found" if find.empty else find
# 5. Add record to base
def add_record(base: pd.DataFrame) -> pd.DataFrame:
    record[0] = str(random.randint(22222,99999))
    base.loc[record[0]] = record
    return base
#6. Update record in base
def update_record(base: pd.DataFrame) -> pd.DataFrame:
    for i in range(len(record)):
        if record[i] != "":
            base.loc[base['id'] == record[0], list(base.columns.values)[i]] = record[i]
    return base
# 7. Delete record in base
def del_record(base: pd.DataFrame) -> pd.DataFrame:
    if record[0] != "":
        base.drop(base[base.id == record[0]].index, inplace=True)
    else:
        return f"Введите id для удаления"
    return base
# 8. Delete base file
def del_file(filename: str) -> str:
    if os.path.isfile(filename):
        os.remove(filename)
        return f"{filename} deleted"
    else:
        return f"{filename} not found"
# 9. Clean base
def clean_base(base: pd.DataFrame) -> pd.DataFrame:
    base = pd.DataFrame()
    return base
# buffer
def buffer(base: pd.DataFrame, number: int) -> None: 
    for i in range(len(record)):
        record[i] = base.loc[number].tolist()[i]
    return
#kill set
def kill_buffer() -> None:
    for i in range(len(record)):
        record[i] = ""
    return
# main menu 10 digits
def menu():
    base = pd.DataFrame()
    choice = ""
    msg = "Main DBS menu"
    while choice != "q":
        print("\033c", end="")
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
            case "4": # Find record in base
                submenu(base, "Set one or more elements\nexecute find with first key\nf. find record")
            case "5": # Add  record to base 
                submenu(base, "Set all elements\nexecute adding with first key\na. add record")
            case "6": # Update record in base
                submenu(base, "Set any element for update\nexecute del with first key\nu. update record") 
            case "7": # Delete record from base
                submenu(base, "Set id only for deletion\nexecute del with first key\nd. delete record")   
            case "8": # delete base file
                filename = input("Enter filename to delete: ") 
                msg = del_file(filename)
            case "9": # Clean base
                base = input("Enter word 'base' in prompt: ") 
                base = clean_base(base)
                msg = "Database is clean" if base.empty else f"Database contains {len(base)} rows"
            case "0": # Import / Export
                base = port(base)
    print("\033c", end="")
    return print("Have a nice day!\nGood Bye!")
# Submenu 10 chars
def submenu(base: pd.DataFrame , msg: str) -> pd.DataFrame:
    choice = ""
    while choice != "r":
        print("\033c", end="")
        print(f"{msg}")
        print(SUBMENU, end="")
        print(*record)
        choice = input("f(ill), r(eturn) or q(uit): ")
        match choice:
            case "i": # i. set id
                record[0] = input("edit id: ")
            case "l": # l. set last surname
                record[1] = input("edit last name: ")
            case "n": # f. set first name
                record[2] = input("edit first name: ")
            case "m": # o. set middle name
                record[3] = input("edit middle name: ")
            case "b": # b. set birthday
                record[4] = input("edit birth day: ")
            case "c": # c. set cellular mobile
                record[5] = input("edit cellular: ")
            case "p": # p. set phone
                record[6] = input("edit phone: ")
            case "k": # k. kill buffer
                kill_buffer()
            case "f": # s. search records
                print("\033c", end="")
                print(find_record(base))
                try:
                    number = int(input("enter line number to copy in BUF\nor hit Enter to return: "))
                    buffer(base, number)
                except BaseException as error:
                    print(f"enter line number to copy in BUF\nor hit Enter to return: ")
            case "a": # a. add record
                base = add_record(base)
                print("Record was added") if type(base) != str else print(base)
                choice = input("a(ny) key to return:")
            case "d": # d. delete record
                base = del_record(base)
                print("Record was deleted") if type(base) != str else print(base)
                choice = input("a(ny) key to return:")
            case "u": # u. update record
                print("\033c", end="")
                print(f"The BUFF:", end="")
                print(*record, end="")
                print(f' was in this record\n{base.loc[base["id"]==record[0]]}')
                base = update_record(base)
                print("Record was updated") if type(base) != str else print(base)
                print(base.loc[base["id"]==record[0]])
                choice = input("a(ny) key to return:")
            case "q":
                print("\033c", end="")
                print("Have a nice day!\nGood Bye!")
                exit()
    return base

def port(base: pd.DataFrame) -> pd.DataFrame:
    choice = ""
    while choice != "r":
        print("\033c", end="")
        #print(f"{msg}")
        print(PORT, end="")
        print(*record)
        choice = input("fi(ll), r(eturn) or q(uit): ")
        match choice:
            case "ic": # ic. imports csv to base
                print("\033c", end="")
                sep = input("Enter separator , or t(ab): ")
                encoding = input("Enter encoding utf8: ")
                if sep == "t":
                    sep ="\t"
                filename = input("Enter name.csv to import: ")
                chunk = pd.read_csv(filename, sep=sep, encoding=encoding, dtype=str)
                base = pd.concat([base, chunk], ignore_index=True)
                print(f"{len(chunk)} row from {filename} imported\nnew base have {len(base)} rows")
                choice = input("press a(ny) key to return: ")
            case "ij": # ij. import json to base
                print("\033c", end="")
                filename = input("Enter name.csv to import: ")
                chunk = pd.read_json(filename, orient='split')
                base = pd.concat([base, chunk], ignore_index=True)
                print(f"{len(chunk)} row from {filename} imported\nnew base have {len(base)} rows")
                choice = input("press a(ny) key to return: ")
            case "ec": # ic. export to csv file
                print("\033c", end="")
                sep = input("Enter separator , or t(ab): ")
                encoding = input("Enter encoding utf8: ")
                if sep == "t":
                    sep ="\t"
                filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S.csv')
                base.to_csv(filename, sep=sep, encoding=encoding, index=False)
                print(f"{len(base)} row exported to {filename}")
                choice = input("press a(ny) key to return: ")
            case "ej": # ij. export to json file
                print("\033c", end="")
                filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S.json')
                base.to_json(filename, orient='split', index=False)
                print(f"{len(base)} row exported to {filename}")
                choice = input("press a(ny) key to return: ")
            case "bc": # bc. buffer to csv file
                print("\033c", end="")
                sep = input("Enter separator , or t(ab): ")
                encoding = input("Enter encoding utf8: ")
                if sep == "t":
                    sep ="\t"
                filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S.csv')
                found = find_record(base)
                found.to_csv(filename, sep=sep, encoding=encoding, index=False)
                print(f"{len(found)} row exported to {filename}")
                choice = input("press a(ny) key to return: ")
            case "bj": # bj. buffer to json file
                print("\033c", end="")
                filename = datetime.datetime.now().strftime('%Y%m%d%H%M%S.json')
                found = find_record(base)
                found.to_json(filename, orient='split', index=False)
                print(f"{len(found)} row exported to {filename}")
                choice = input("press a(ny) key to return: ")
            case "q":
                print("\033c", end="")
                print("Have a nice day!\nGood Bye!")
                exit()
    return base

menu()

