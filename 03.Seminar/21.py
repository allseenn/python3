# Напишите программу для печати всех уникальных значений в словаре. 
# Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# my_data = []
# for i in data:
#     for value in i.values():
#         my_data.append(value)
# print(set(my_data))
# input_list = [{"V": " S001"}, {"V": " S002"}, {"VI": "S001 "},
# {"VI": "S005 "}, {"VII": " S005"}, {" V ":"S009"}, {" VIII":"S007 "}]

# unic_values = set()
# for d in input_list:
#     print('d это - ',d)
#     print('d.values это -', d.values())    
#     unic_values.add(tuple(d.values())[0].strip())
        
# print(unic_values)

input_list = [{"V": " S001"}, {"V": " S002"}, {"VI": "S001 "},
{"VI": "S005 "}, {"VII": " S005"}, {" V ":"S009"}, {" VIII":"S007 "}]

unic_values = set()
for d in input_list:
    print('d это - ',d)
    print('d.values это -', d.values())
    elem = d.values()
    elem = tuple(elem)
    elem = elem[0]
    elem = elem.strip()
    unic_values.add(elem)
        
print(unic_values)