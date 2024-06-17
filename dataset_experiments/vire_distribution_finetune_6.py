import matplotlib.pyplot as plt

file = open("vine_leaf_vision_dataset\\train_summary.txt", "r")

n_healthy_train = 0
n_healthy_valid = 0
n_blight_train = 0
n_blight_valid = 0
n_esca_train = 0
n_esca_valid = 0
n_gfe_train = 0
n_gfe_valid = 0
n_gfh_train = 0
n_gfh_valid = 0
n_pve_train = 0
n_pve_valid = 0
n_pvgfe_train = 0
n_pvgfe_valid = 0
n_pvgfh_train = 0
n_pvgfh_valid = 0
n_pvh_train = 0
n_pvh_valid = 0
n_pvwsd_train = 0
n_pvwsd_valid = 0
n_wsd_train = 0
n_wsd_valid = 0
n_rs_train = 0
n_rs_valid = 0

br = 0

for line in file:
    parts = line.split(",")

    lbl = open("vine_leaf_vision_dataset\\" + parts[1])

    lbl_count = {
        "0": 0,
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": 0,
        "11": 0,
        "12": 0,
    }

    for l in lbl:
        p = l.split(" ")
        lbl_count[p[0]] += 1

    if lbl_count["1"] > 0:
      br += lbl_count["1"]

    if "train" in parts[3]:
        n_healthy_train += lbl_count["0"]
        n_blight_train += lbl_count["2"]
        n_esca_train += lbl_count["3"]
        n_gfe_train += lbl_count["4"]
        n_gfh_train += lbl_count["5"]
        n_pve_train += lbl_count["6"]
        n_pvgfe_train += lbl_count["7"]
        n_pvgfh_train += lbl_count["8"]
        n_pvh_train += lbl_count["9"]
        n_pvh_train += lbl_count["10"]
        n_wsd_train += lbl_count["11"]
        n_rs_train += lbl_count["12"]
    elif "valid" in parts[3]:
        n_healthy_valid += lbl_count["0"]
        n_blight_valid += lbl_count["2"]
        n_esca_valid += lbl_count["3"]
        n_gfe_valid += lbl_count["4"]
        n_gfh_valid += lbl_count["5"]
        n_pve_valid += lbl_count["6"]
        n_pvgfe_valid += lbl_count["7"]
        n_pvgfh_valid += lbl_count["8"]
        n_pvh_valid += lbl_count["9"]
        n_pvh_valid += lbl_count["10"]
        n_wsd_valid += lbl_count["11"]
        n_rs_valid += lbl_count["12"]


"""print("H TRAIN " + str(n_healthy_train))
print("B TRAIN " + str(br))
print("LB TRAIN " + str(n_blight_train))
print("E TRAIN " + str(n_esca_train))
print("GFE TRAIN " + str(n_gfe_train))
print("GFH TRAIN " + str(n_gfh_train))
print("PVE TRAIN " + str(n_pve_train))
print("PVGFE TRAIN " + str(n_pvgfe_train))
print("PVGFH TRAIN " + str(n_pvgfh_train))
print("PVH TRAIN " + str(n_pvh_train))
print("PVWSD TRAIN " + str(n_pvwsd_train))
print("WSD TRAIN " + str(n_wsd_train))
print("RS TRAIN " + str(n_rs_train))
print("H VALID " + str(n_healthy_valid))
print("LB VALID " + str(n_blight_valid))
print("E VALID " + str(n_esca_valid))
print("GFE VALID " + str(n_gfe_valid))
print("GFH VALID " + str(n_gfh_valid))
print("PVE VALID " + str(n_pve_valid))
print("PVGFE VALID " + str(n_pvgfe_valid))
print("PVGFH VALID " + str(n_pvgfh_valid))
print("PVH VALID " + str(n_pvh_valid))
print("PVWSD VALID " + str(n_pvwsd_valid))
print("WSD VALID " + str(n_wsd_valid))
print("RS VALID " + str(n_rs_valid))"""

data = [n_healthy_train, 
        n_healthy_valid, 
        n_blight_train, 
        n_blight_valid, 
        n_esca_train, 
        n_esca_valid, 
        n_gfe_train,
        n_gfe_valid, 
        n_gfh_train, 
        n_gfh_valid, 
        n_pve_train, 
        n_pve_valid, 
        n_pvgfe_train, 
        n_pvgfe_valid, 
        n_pvgfh_train, 
        n_pvgfh_valid, 
        n_pvh_train, 
        n_pvh_valid, 
        n_wsd_train, 
        n_wsd_valid, 
        n_pvwsd_train, 
        n_pvwsd_valid, 
        n_rs_train, 
        n_rs_valid]
labels = ["healthy train",
        "healthy valid",
        "leaf blight train", 
        "leaf blight valid", 
        "esca train", 
        "esca valid", 
        "golden fleck \n esca train", 
        "golen fleck esca valid", 
        "golen fleck healthy train", 
        "golen fleck healthy valid", 
        "partially visible esca train", 
        "partially visible esca valid", 
        "partially visible \n golden fleck esca train", 
        "partially visible \n golden fleck esca valid", 
        "partially visible \n golden fleck healthy train", 
        "partially visible \n golden fleck healthy valid", 
        "partially visible healthy train",
        "partially visible healthy valid",
        "white speckle dapple train", 
        "white speckle dapple valid", 
        "partially visible white speckle dapple train", 
        "partially visible white speckle dapple valid", 
        "red spot train", 
        "red spot valid"]

plt.bar(labels, data)

plt.title("Distribuzione delle classi")
plt.xlabel("Classe")
plt.ylabel("Valori")

plt.show()