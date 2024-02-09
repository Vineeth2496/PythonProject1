# str1='Hello dude, how r u doing'
# x=str1.split()
# print(x)
# print(len(x))
path=r"F:\SpringBoot Videos\Raghu Sir MS Video\Notes\data.log"
print(path)
f=open(path,'r')
text=f.read()
print(len(text))

'''
def count_words(file_path):
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the content of the file
            content = file.read()
            
            # Split the content into words
            words = content.split()
            
            # Count the number of words
            num_words = len(words)
            
            # Print the result
            print(f'The number of words in the file is: {num_words}')

    except FileNotFoundError:
        print(f'File not found: {file_path}')
    except Exception as e:
        print(f'An error occurred: {e}')

file_path = 'sample.txt'  
count_words(file_path)

'''