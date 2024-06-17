import glob
import fileinput

TO_LABEL = "0"
PATH_TO_LABELS = "vine_leaf_vision_dataset\\annotations\\*"

annotations_list = glob.glob(PATH_TO_LABELS)

for annotation in annotations_list:
    try:
        with fileinput.FileInput(annotation, inplace=True) as file:
            for line in file:
                parts = line.split(" ")

                if parts[0] == "4":
                    parts[0] = "17"

                if parts[0] == "9":
                    parts[0] = "4"
                elif parts[0] == "10":
                    parts[0] = "5"
                elif parts[0] == "11":
                    parts[0] = "6"
                elif parts[0] == "12":
                    parts[0] = "7"
                elif parts[0] == "13":
                    parts[0] = "8"
                elif parts[0] == "14":
                    parts[0] = "9"
                elif parts[0] == "15":
                    parts[0] = "10"
                elif parts[0] == "16":
                    parts[0] = "11"
                elif parts[0] == "17":
                    parts[0] = "12"

                new_line = " ".join(parts)
                print(new_line, end="")
    except:
        print(annotation + " NOT FOUND")
