
#David Le
#ACSG-570-01-2021U Comp Systems Security
#Professor Yacine Merdjemak
#Week 9. Problem - The Playfair Cipher
#8/1/2021


#Playfair function will call functions below to create a encryption table with the key and encrypt the plaintext
def playfair(key, plaintext):
    create_table(key)
    print('\n'.join(' '.join(map(str,sl)) for sl in list_of_lists))
    print("\n")
    cleanup(plaintext)
    resultEncryption=encrypt(plaintext)
    print(resultEncryption)

    
#created 5x5 table as a list of lists.
list_of_lists = [[1,2,3,4,5], 
                     [1,2,3,4,5],
                     [1,2,3,4,5],
                     [1,2,3,4,5],
                     [1,2,3,4,5]]
print('\n'.join(' '.join(map(str,sl)) for sl in list_of_lists))
print("\n")

#init_table Function initalizes the 5x5 table with stars when called
def init_table():
   for x in range(5):
       for y in range(5):
            list_of_lists[x][y]='*'
   print('\n'.join(' '.join(map(str,sl)) for sl in list_of_lists))
   print("\n")

#table_has function will check if letter exists within the table/lists and then returns either true or false
def table_has(letter): 
    for x in range(5):
        for y in range(5):
            if list_of_lists[x][y]==letter:
                return True

    return False
    
#clean_key changes the secret key to uppercase and replaces J by I and returns a clean key.
def clean_key(key):
    key=key.upper()
    if "J" in key:
        key.replace('J','I')
        return key
    else:
       return key

#set_cell sets a table cell to a specific letter in the table
def set_cell(letter):
    for x in range(5):
        for y in range(5):
            list_of_lists[x][y]=letter

#create_table function populates the encryption table when given the secret key by first cleaning the table using init_table and cleaning the key using clean_key
#
def create_table(key):
        alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        init_table()
        clean_key(key)
        key=key.upper()
        global list_of_lists

        flatKeyList=[] #create a list for the key
        for x in key:#the list will be updated to exclude characters that already occured and special characters
            if (x in flatKeyList)== False:#not in flatKeyList:
                if x=='J':
                    flatKeyList.append("I")
                elif x==' ':
                    continue
                else:
                    flatKeyList.append(x)
            else:
                if table_has(x)== True:
                    continue
        for x in alphabet:#append the alphabet to the flat key list after the key has been adjusted.
            if (x in flatKeyList)== False:#not in flatKeyList:
                if x=='J':
                    continue#since I/J are considered the same and if they already in the list they will be excluded
                else:
                    flatKeyList.append(x)
            else:
                if table_has(x)== True:
                    continue
        list_of_lists=[flatKeyList[i:i + 5] for i in range(0, 25, 5)]
        
#find_letter function takes a char/letter and returns the row and column of the letter that exists within the table
def find_letter(letter): 
    letter=letter.upper()
    if letter=='J':
        letter='I'
    for row in range(5):
        for column in range(5):
            if list_of_lists[row][column]==letter:
                return [row,column]


#encode_pair function will take a pair of letters and then encrypt them using the playfair cipher rules
def encode_pair(a,b):
    a.upper()
    b.upper()
    a_location=find_letter(a) #gives the row and then the column of the letter[row,column] from the list of lists
    b_location =find_letter(b)#gives the row and then the column of the letter[row,column] from the list of lists
    a_row=a_location[0]
    a_col=a_location[1]
    b_row=b_location[0]
    b_col=b_location[1]

    if (a_col==b_col) and (a_row==b_row):
        print("Error the pair are the same letter. Please input different letters.")
        return#if its the same exact row and column

    elif (a_col==b_col):# this is the column rule where if a and b share same column, the column stay the same but the rows change by shifting down by 1 and wrap back up
        a_new_col=a_col
        b_new_col=b_col
        if (a_row==4) and (b_row==4):
            a_new_row=0
            b_new_row=0
        if (a_row==4):
            a_new_row=0
        if (b_row==4):
            b_new_row=0
        else:
            a_new_row=a_row+1#shift down for desired row
            b_new_row=b_row+1
    elif (a_row==b_row):# this is the row rule where if a and b share same row, the row stay the same but the columns change by shifting right by 1 and wrap back left
        a_new_row=a_row
        b_new_row=b_row
        if (a_col==4):
            a_new_col=0
        if (b_col==4):
            b_new_col=0
        else:
            a_new_col=a_col+1#shift to the right for row
            b_new_col=b_col+1
    
    elif(a_row!=b_row and a_col!=b_col):#if rectangle as in no same row AND no same column then just swap their locations
        a_new_row=a_row#SWAP THE column location keep the row
        b_new_row=b_row
        a_new_col=b_col
        b_new_col=a_col
    a_new_col=a_col

    newLetterA=list_of_lists[a_new_row][a_new_col]
    newLetterb=list_of_lists[b_new_row][b_new_col]
    
    
    newletterpair=newLetterA+newLetterb
    return newletterpair

#cleanup function will take a message/plaintext and cleans up the message to remove spaces and replace J with I, and make use of playfair cipher message rules 
#to return the modified message
def cleanup(plaintext):
    plaintext=plaintext.upper()
    if ' ' in plaintext:
        plaintext=plaintext.replace(" ", "")
    if 'J' in plaintext:
        plaintext=plaintext.replace("J", "I")
    newPlaintext=""
    for x in range(len(plaintext)):
        
        if plaintext[x-1]==plaintext[x]:
            if plaintext[x-1]=="X":
                newPlaintext=newPlaintext + "Q"
                newPlaintext=newPlaintext+plaintext[x]
            else:
                newPlaintext=newPlaintext + "X"
                newPlaintext=newPlaintext+plaintext[x]
        else:
            newPlaintext=newPlaintext+plaintext[x]
    if len(newPlaintext)%2!=0:
        if(newPlaintext[len(newPlaintext)-1]=="Z"):
            newPlaintext=newPlaintext+"Q"
        else:
            newPlaintext=newPlaintext+"Z"
    return newPlaintext

#encrypt function will take a message/plaintext and then encrypt the message and return the encrypted text in a 5 letter with a space pattern
def encrypt(plaintext): 
    plaintext=cleanup(plaintext)
    encryptedtext=""
    for x in range(0,len(plaintext),2):
        if x<len(plaintext)-1:
            encryptedtext+=encode_pair(plaintext[x],plaintext[x+1])
    encryptedtext=' '.join(encryptedtext[i:i+5] for i in range(0, len(encryptedtext), 5))

    
    return(encryptedtext)
#this is part of the execution phase that will prompt the user for input for key and message and then call the playfair function which prints out the encrypted message
##and then prompts the user if they wish to continue or not.
if __name__=="__main__":
    repeat=True
    while repeat==True:
        print('Enter secret key:')
        x = input()
        print('Your secret key:'+x)
        print('Enter secret message:')
        y = input()
        print('Your secret message:'+y)

        print("\n")

        playfair(x,y)
        
        print("\n")
        print("Do you want to encrypt another message?")
        responseInput=input()
        responseInput=responseInput.upper()
        if responseInput=="YES":
            pass
        else:
            repeat=False
    
    
    



