import numpy as np
import random

# Function to read the text file into a list of rows
def read_txt_to_list(file_path, delimiter=","):
    with open(file_path, "r") as file:
        data = [line.split("\n")[0].split(delimiter) for line in file]
    return data


# Function to shuffle the rows of the list
def shuffle_rows(data):
    random.shuffle(data)
    return data


# Function to append a value to each row in the list
def append_value_to_rows(data, value):
    for row in data:
        row.append(value)
    return data

# Function to write the shuffled list back to a text file
def write_list_to_txt(file_path, data, delimiter=","):
    with open(file_path, "w") as file:
        for row in data:
            file.write(delimiter.join(row) + "\n")


#input_path = "vine_leaf_vision_dataset\\finetune_summary.txt"
input_path = "vine_leaf_vision_dataset\\train_summary.txt" #COMMENTARE LE PARTI PER IL TEST
data = read_txt_to_list(input_path)
data = data[1:]

train = 70
valid = 10
test = 20

n_train = int(np.around(len(data) * train / 100))
n_valid = int(np.around(len(data) * valid / 100))

##
n_test = int(np.around(len(data) * test / 100))

n_train += len(data) - (n_train + n_valid)

##
#n_train += len(data) - (n_train + n_valid + n_test)

shuffled_data = shuffle_rows(data)

train_split = shuffled_data[0:n_train]
train_split = append_value_to_rows(train_split, "train")
valid_split = shuffled_data[n_train : n_train + n_valid]
valid_split = append_value_to_rows(valid_split, "valid")

##
#test_split = shuffled_data[n_train + n_valid : n_train + n_valid + n_test]
#test_split = append_value_to_rows(test_split, "test")

train_split.extend(valid_split)

##
#train_split.extend(test_split)

write_list_to_txt(input_path, train_split)