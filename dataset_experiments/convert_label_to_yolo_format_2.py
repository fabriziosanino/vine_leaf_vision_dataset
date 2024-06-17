import glob
import fileinput

"IT CONVERTS LABELSTUDIO FORMAT INTO OUR FOURMAT"

PATH = "vine_leaf_vision_dataset\\annotations\\*"

files = glob.glob(PATH)

for file in files:
    try:
        with fileinput.FileInput(file, inplace=True) as file:
            for line in file:
                parts = line.split(" ")

                parts[4] = parts[4].replace("\n", "")

                x0 = float(parts[1])
                y0 = float(parts[2])
                x1 = float(parts[3])
                y1 = float(parts[4])

                w = x1 - x0
                h = y1 - y0

                x_center = x0 + (w / 2)
                y_center = y0 + (h / 2)

                parts[1] = str(x_center)
                parts[2] = str(y_center)
                parts[3] = str(w)
                parts[4] = str(h)
                parts[4] += "\n"

                new_line = " ".join(parts)
                print(new_line, end="")
    except:
        print("NOT FOUND")