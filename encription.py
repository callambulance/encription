import string
import math
from operator import itemgetter


alphabet = list(string.ascii_lowercase)

def main_menu():

    user_word = input("\nWhat word you want to encrypt?\n").lower()

    while user_word.isalpha() == False:
        user_word = input("\nType only letters for encryption\n")
    while True:
        try:
            user_chose = int(input("\nWhat type of encryption you want to choose? \n1 - shift, 2 - mirror, 3 - matrix, 4 - rotate right, 5 - square index, 6 - remove odd blocks, 7 - reduce to fixed\n"))

            while user_chose not in range(1,8):
                user_chose = int(input("\nChoose the encryption method:\n1 - shift, 2 - mirror, 3 - matrix, 4 - rotate right, 5 - square index, 6 - remove odd blocks, 7 - reduce to fixed\n"))
            break

        except ValueError:
            print("please choose the number between 1 and 7")
    
    if user_chose == 1:
        user_shift = int(input("Type shift number\n"))
        encrypting_result = shift_characters(user_word, user_shift)

    elif user_chose == 2:
        encrypting_result = abc_mirror(user_word)
        
    elif user_chose == 3:
        word2 = input("Type second word for encrypting\n")
        encrypting_result = create_matrix(user_word, word2)
        
    elif user_chose == 4:
        user_rotate_number = int(input("Type number for rotating\n"))
        encrypting_result = rotate_right(user_word, n)

    elif user_chose == 5:
        encrypting_result = get_square_index_chars(user_word)

    elif user_chose == 6:
        block_length = int(input("Type length of the block for encrypting\n"))
        encrypting_result = remove_odd_blocks(user_word, block_length)

    elif user_chose == 7:
        reducing = int(input("Type number for reducing\n"))
        encrypting_result = reduce_to_fixed(user_word, reducing)
    
    return encrypting_result


def shift_characters(word, shift): #1
    shift_i = []
    shift_word = []
    while shift>len(alphabet):
        shift = shift - len(alphabet)
    for char in word:
        if char in alphabet:
            new_char = alphabet.index(char)+shift
            if new_char<=len(alphabet):
                shift_i.append(new_char)
            else:
                loop_index = len(alphabet) - alphabet.index(char)
                new_index = shift - loop_index
                shift_i.append(new_index)
        
            
    shift_word = [alphabet[i] for i in shift_i] 
    new_word = ''.join(shift_word)
    return new_word
            
   

#print(shift_characters('ayz', 4))


def abc_mirror(word): #2
    mirror = []
    for char in word:
        if char in alphabet:
            new_index = -alphabet.index(char)-1
            mirror.append(new_index)

    shift_word = [alphabet[i] for i in mirror] 
    return ''.join(shift_word)

#abc_mirror("abc")



def create_matrix(word1, word2): #3
    shift_word = []
    shift_index=[]
    result=[]
    for char in word2:
        if char in alphabet:
            shift_index.append(alphabet.index(char))

    for i in shift_index:
        shift_i = []
        for char in word1:
            if char in alphabet:
                new_char = alphabet.index(char)+i
                if new_char<=len(alphabet):
                    shift_i.append(new_char)
                else:
                    loop_index = len(alphabet) - alphabet.index(char)
                    new_index = i - loop_index
                    shift_i.append(new_index)

        shift_word = [alphabet[i] for i in shift_i] 
        new_word = ''.join(shift_word)
        result.append(new_word)
    
    return result

#create_matrix('mamas', 'papas')



def rotate_right(word, n): #4
    word_list = list(word)
    result_list=[]
    all_char=[]
    i = 0

    while i < n:
        result_list.insert(0, word_list[-1])
        word_list.pop(-1)
        i+=1

    all_char = result_list + word_list
    print(all_char)

    result = ''.join(all_char)

    return result


#rotate_right('abcdefgh', 3)


def get_square_index_chars(word):  #5
    result_list=[]
    list_word = list(word)
    print(list_word)

    for i in list_word:
        root = math.sqrt(list_word.index(i))
        if int(root + 0.5) ** 2 == list_word.index(i):
            result_list.append(i)
    
    result_word = ''.join(result_list)

    return result_word

#get_square_index_chars('abcdefghijklm')


def remove_odd_blocks(word, block_length): #6
    i = 0
    slice=[]
    changed_word = []
    result=[]
    for char in word:
        if i < block_length-1:
            slice.append(char)
            i+=1
        elif i == block_length-1:
            slice.append(char)
            changed_word.append(''.join(slice))
            slice = []
            i = 0
    if len(slice)>0:
        changed_word.append(''.join(slice))

    for i in changed_word:
        if changed_word.index(i)%2==0:
            result.append(i)
        
        word_result = ''.join(result) 

    return word_result



#remove_odd_blocks('abcdefghijklm', 3)


def reduce_to_fixed(word, n): #7
    word_list = list(word)
    word_slice = [] 
    new_word_slice = []
    result_word_list = []
    i = 0
    j = 0
    
    for char in word_list:
        if i < n:
            word_slice.append(char)
            i+=1
    
    rotation_slice = int(n/3)

    for char in word_slice:
        while j < rotation_slice:
            new_word_slice.append(word_slice[0])
            word_slice.pop(0)
            j+=1
    
    result_word_list = word_slice + new_word_slice

    result_word = ''.join(result_word_list)

    return result_word

    
#reduce_to_fixed('abcdefghijklm', 6)



print(main_menu())