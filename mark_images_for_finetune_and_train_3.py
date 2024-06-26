import fileinput
import numpy as np
from PIL import Image

res_file = open("vine_leaf_vision_dataset\\finetune_summary.txt", "w")
train_file = open("vine_leaf_vision_dataset\\train_summary.txt", "w")

file = "vine_leaf_vision_dataset\\dataset_summary.txt"
first = True

n_b_rot = 0
n_healthy = 0

with fileinput.FileInput(file, inplace=True) as file:
    for line in file:
        parts = line.split(",")

        if first:
            first = False
        else:
            try:
                img = Image.open("vine_leaf_vision_dataset\\" + parts[0])
                lbl = open("vine_leaf_vision_dataset\\" + parts[1], "r")

                if "grapevine" in parts[2]:
                    if "V_HL" in parts[1]:
                        res_file.write(",".join(parts))
                        n_healthy += 1
                    else:
                        b_rot = True
                        for l in lbl:
                            p = l.split(" ")
                            if p[0] != "1":
                                b_rot = False
                                break

                        if b_rot:
                            res_file.write(",".join(parts))
                            n_b_rot += 1
                        else:
                            train_file.write(",".join(parts))
                elif "pddc" in parts[2]:
                    b_rot = False
                    for l in lbl:
                        p = l.split(" ")
                        if p[0] == "1":
                            b_rot = True
                            break

                    if b_rot:
                        res_file.write(",".join(parts))
                        n_b_rot += 1
                    else:
                        res_file.write(",".join(parts))
                        n_healthy += 1
                elif "vitis_vinifera" in parts[2] and n_healthy < n_b_rot:
                    red_spot = False
                    hly = 0
                    for l in lbl:
                        p = l.split(" ")
                        if "12" in p[0]:
                            red_spot = True
                            break
                        else:
                            hly += 1

                    if not red_spot:
                        res_file.write(",".join(parts))
                        n_healthy += hly
                    else:
                        train_file.write(",".join(parts))
                else:
                    train_file.write(",".join(parts))
            except:
                # img or lbl missing, discard
                print("Img or Lbl not found")

        new_line = ",".join(parts)
        print(new_line, end="")

print("B ROT " + str(n_b_rot))
print("H " + str(n_healthy))
