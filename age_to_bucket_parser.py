import json


# return list of ranges
def list_of_range(num_list, max_age):
    range_list = [range(0, num_list[0])]
    for i in range(1, len(num_list)):
        range_list.append(range(num_list[i - 1], num_list[i]))
    range_list.append(range(num_list[-1],max_age+1))      
    return range_list


# return list of names
def list_of_names(ppl_dict, num_list):
    list_name = []
    for x in range(len(num_list)):
        temp = []
        for key, value in ppl_dict.items():
            if value in num_list[x]:
                temp.append(key)
        list_name.append(temp)
    return list_name


# return string list of ranges
def range_string_list(range_list):
    string_range = []
    for x in range(len(range_list)):
        a = str(range_list[x].start) + '-' + str(range_list[x].stop)
        string_range.append(a)
    return string_range


# print  range and names
def printing_dict_vertical(dict1):
    for key, value in dict1.items():
        print(key, ':\n')
        for i in range(len(value)):
            print(value[i], '\n')


def main():
    with open('hw.json') as f:
         data = json.load(f)
    list_of_num = (data['buckets'])
    list_of_num.sort()
    max_age= max(data['ppl_ages'].values())
    ranged_list = list_of_range(list_of_num, max_age)
    named_list = list_of_names((data['ppl_ages']), ranged_list)
    string_range_list = range_string_list(ranged_list)
    merged_dict = dict(zip(string_range_list, named_list))
    printing_dict_vertical(merged_dict)

if __name__ == '__main__':
    main()
