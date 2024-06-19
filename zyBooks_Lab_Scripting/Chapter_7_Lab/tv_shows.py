# Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. 
# The input file contains an unsorted list of number of seasons followed by the corresponding TV show. 
# Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, and a list of TV shows are the values (since multiple shows could have the same number of seasons).

# Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, separating multiple TV shows associated with the same key with a semicolon (;).
# Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.


def read_file_to_dict(filename):
    seasons_dict = {}
    
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 2):
            seasons = int(lines[i].strip())
            show = lines[i+1].strip()
            if seasons not in seasons_dict:
                seasons_dict[seasons] = []
            seasons_dict[seasons].append(show)
    
    return seasons_dict

def write_dict_sorted_by_keys(seasons_dict, output_filename):
    with open(output_filename, 'w') as file:
        for seasons in sorted(seasons_dict.keys()):
            shows = '; '.join(seasons_dict[seasons])
            file.write(f"{seasons}: {shows}\n")

def write_dict_sorted_by_values(seasons_dict, output_filename):
    sorted_shows = sorted((show, seasons) for seasons in seasons_dict for show in seasons_dict[seasons])
    with open(output_filename, 'w') as file:
        for show, seasons in sorted_shows:
            file.write(f"{show}\n")

def main():
    input_filename = input('Enter filename: ').strip()
    
    seasons_dict = read_file_to_dict(input_filename)
    
    write_dict_sorted_by_keys(seasons_dict, 'output_keys.txt')
    write_dict_sorted_by_values(seasons_dict, 'output_titles.txt')

if __name__ == "__main__":
    main()
