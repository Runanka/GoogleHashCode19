A=[];
file=open('a_example.txt','r')
while True:
    line1=file.readline()
    if line1=='' :
        break
    A.append(line1.strip('\n'))
    
no_of_pictures=int(A[0]);
a2=[];
for i in range(1,len(A)):
    a2.append(A[i].split());
    
for i in range(0,len(a2)):
    a2[i][1]=int(a2[i][1]);
    
for i in range(0,len(a2)):
    tags=[];
    for j in range(0,a2[i][1]):
        tags.append(a2[i][j+2])
    a2[i].insert(2,tags);
    del a2[i][3:];
    
for i in range(0,len(a2)):
    a2[i].append(i);
    a2[i].append(0);


#sorting out the vertical & horizontal ones:
pics_vertical=[];
pics_horizontal=[];
for i in range(0,len(a2)):
    if a2[i][0]=='V':
        pics_vertical.append(a2[i]);
    else:
        pics_horizontal.append(a2[i]);

#grouping of the similar tags part1:
import math
import string

def count_frequency(word_list):
    D = {}
    for new_word in word_list:
        if new_word in D:
            D[new_word] = D[new_word]+1
        else:
            D[new_word] = 1
    return D

def word_frequencies_for_file(word_list):
    freq_mapping = count_frequency(word_list)
    return freq_mapping

def inner_product(D1,D2):
    sum = 0.0
    for key in D1:
        if key in D2:
            sum += D1[key] * D2[key]
    return sum

def vector_angle(D1,D2):
    numerator = inner_product(D1,D2)
    denominator = math.sqrt(inner_product(D1,D1)*inner_product(D2,D2))
    return math.acos(numerator/denominator)

def mainfunc(tag_list1,tag_list2):
        sorted_word_list_1 = word_frequencies_for_file(tag_list1)
        sorted_word_list_2 = word_frequencies_for_file(tag_list2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        return distance

#grouping of similar tags part2:
total_vert=len(pics_vertical);
matrix_vert = [[0]*total_vert for _ in range(total_vert)] 
for i in range(total_vert):
    for j in range(i):
        matrix_vert[i][j] = mainfunc(pics_vertical[i][2],pics_vertical[j][2])
        matrix_vert[j][i] = mainfunc(pics_vertical[i][2],pics_vertical[j][2])
vertical_pairs=[];
for i in range(len(pics_vertical)-1):
    value=matrix_vert[i][i+1];
    max_index=i+1;
    for j in range(len(pics_vertical)):
        if matrix_vert[i][j]>value:
            value=matrix_vert[i][j];
            max_index=j;
            
tags2=list(set().union(pics_vertical[i][2],pics_vertical[j][2]))
vertical_pairs.append(['V',len(tags2),tags2,[pics_vertical[i][3],pics_vertical[j][3]],0]);


total_list=[];
for i in range(len(vertical_pairs)):
    total_list.append(vertical_pairs[i]);
for j in range(len(pics_horizontal)):
    total_list.append(pics_horizontal[j]);    

#function for extracting the minimum of the tags
def mainfunct2(n1,n2,ct):
    ct1=1.571-ct;
    n1=n1-ct1;
    n2=n2-ct1;
    return min(n1,n2,ct1);

total_len=len(total_list);
matrix = [[0]*total_len for _ in range(total_len)] 
for i in range(total_len):
    for j in range(i):
        matrix[i][j] = mainfunc(total_list[i][2],total_list[j][2]);
        matrix[j][i] = mainfunc(total_list[i][2],total_list[j][2]);

final_array=[];

final_array.append(total_list[0][3]);
total_list[0][4]==1;

for i in range(len(total_list)-1):
    total_list[i][4]=1;
    id=i+1;
    max_value=mainfunct2(total_list[i][1],total_list[i+1][1],matrix[i][i+1]);
    for j in range((i+1),len(total_list)):
        if(total_list[j][4]==0):
            value=mainfunct2(total_list[i][1],total_list[j][1],matrix[i][j]);
            if value>max_value:
                max_value=value;
                id=j;
    final_array.append(total_list[id][3]);
    i=id;
    
print(final_array)
