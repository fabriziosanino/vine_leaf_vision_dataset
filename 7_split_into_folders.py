import os
import shutil

file = open("vine_leaf_vision_dataset\\finetune_summary.txt", "r")
dataset_name = "finetune-dataset"
#file = open("vine_leaf_vision_dataset\\train_summary.txt", "r") #Commentare righe test
#dataset_name = "train-dataset"

os.mkdir("./" + dataset_name)
os.mkdir("./" + dataset_name + "/images")
os.mkdir("./" + dataset_name + "/labels")
os.mkdir("./" + dataset_name + "/images" + "/train")
os.mkdir("./" + dataset_name + "/images" + "/valid")
os.mkdir("./" + dataset_name + "/images" + "/test")
os.mkdir("./" + dataset_name + "/labels" + "/train")
os.mkdir("./" + dataset_name + "/labels" + "/valid")
os.mkdir("./" + dataset_name + "/labels" + "/test")

for line in file:
  parts = line.split(",")

  if "train" in parts[3]:
    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[0],
        ".\\" + dataset_name + "\\images\\train\\",
    )

    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[1],
        ".\\" + dataset_name + "\\labels\\train\\",
    )
  elif "valid" in parts[3]:
    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[0],
        ".\\" + dataset_name + "\\images\\valid\\",
    )

    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[1],
        ".\\" + dataset_name + "\\labels\\valid\\",
    )
  else: 
    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[0],
        ".\\" + dataset_name + "\\images\\test\\",
    )

    shutil.copy(
        "vine_leaf_vision_dataset\\" + parts[1],
        ".\\" + dataset_name + "\\labels\\test\\",
    )