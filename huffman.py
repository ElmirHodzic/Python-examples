import operator

def built_dict(string):
    #make asociative array from string in which key values are chars,
    #and items are number of repetitions
    dictionary = {};    
    for i in range(len(string)):
        char = string[i]
        if string[i] in dictionary:
            dictionary[char] += 1;
        else:
            dictionary[char] = 1;  
    return dictionary;

def sort_dict(dictionary):
    #sorting asociative array of items like 'C' : 1 by item value descending
    sorted_dictionary = sorted(dictionary.items(), key=operator.itemgetter(1));    
    return sorted_dictionary;

def initialize_list_of_codes(string):
    #make asociative array from string in which key values are chars,
    #and items are empty strings (will be binary strings)
    loc = {};
    for i in range(len(string)):
        char = string[i][0]
        loc[char] = '';
    return loc;

def make_tree(data):
    #Making huffman tree: 
    #take two tuples sum their second component make list of two components(tuples), 
    #nodes of tree are tuples and tuples are from same parent if they are in same list, 
    #in for loop we move element created in last step on appropriate index in string 
    #to keep list sorted (use >= to move element behind tuples and give a tuples higher priority)
    while len(data) > 2:    
        data[0] = ([data[0], data[1]], data[0][1] + data[1][1])
        data.pop(1);
        
        for i in range(len(data)-1):
            if data[i][1] >= data[i + 1][1]:
                data[i], data[i+1] = data[i+1], data[i]
            else:
                break

    return data
    
def make_codes(lst, string, dictionary):    
    left_string = string + '0'
    right_string = string + '1'
    left = lst[0]
    right = lst[1]

    if type(left[0]) is str:
        dictionary[left[0]] = left_string
    if type(right[0]) is str:
        dictionary[right[0]] = right_string
        
    if type(left[0]) is list:
        make_codes(left[0], left_string, dictionary)
    if type(right[0]) is list:
        make_codes(right[0], right_string, dictionary)
        

def HuffmanCoding(string):
    dictionary = built_dict(string)
    data = sort_dict(dictionary)
    data = make_tree(data)
    loc = initialize_list_of_codes(string)
    make_codes(data, '', loc)
    return loc
    

def CompresionRatio(loc, string):
    sum_input_stream = len(string) * 8.0
    sum_output_stream = 0.0
    for i in range(len(string)):
        sum_output_stream += (len(loc[string[i]]))
    return sum_input_stream / sum_output_stream

test1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce pretium nisl id sapien laoreet, vel condimentum augue rhoncus. Nunc tincidunt a leo non euismod."
loc1 = HuffmanCoding(test1)
cr1 = CompresionRatio(loc1, test1)
print(loc1)
print(cr1)   