from collections import defaultdict
def count_words (input_file, output_file):
    word_count = defaultdict(int)

    try:
        with open(input_file,'r') as rf:
            for line in rf:
                #covent to lowercase and keep only alphanumeric and spaces
                cleaned_line = ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in line )
                words = cleaned_line.split()
                print(words)
                for word in words:
                    word_count[word] +=1
        
        with open(output_file,'w') as wf:
            for word, count in word_count.items():
                wf.write(f"The word '{word}' appears {count} time(s)\n")

    except IOError as e:
        print(f"An error occured: {e}")

count_words("test.txt", "result.txt")