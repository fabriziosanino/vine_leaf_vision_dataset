import matplotlib.pyplot as plt

file = open("vine_leaf_vision_dataset\\finetune_summary.txt", "r")

n_b_rot_train = 0
n_b_rot_valid = 0
n_b_rot_test = 0
n_healthy_train = 0
n_healthy_valid = 0
n_healthy_test = 0

for line in file:
    parts = line.split(",")

    if ("vitis_vinifera" in parts[2] or "V_HL" in parts[0]) and "train" in parts[3]:
        n_healthy_train += 1
    elif ("vitis_vinifera" in parts[2] or "V_HL" in parts[0]) and "valid" in parts[3]:
        n_healthy_valid += 1
    elif ("vitis_vinifera" in parts[2] or "V_HL" in parts[0]) and "test" in parts[3]:
        n_healthy_test += 1
    elif "B.Rot" in parts[0] and "train" in parts[3]:
        n_b_rot_train += 1
    elif "B.Rot" in parts[0] and "valid" in parts[3]:
        n_b_rot_valid += 1
    elif "B.Rot" in parts[0] and "test" in parts[3]:
        n_b_rot_test += 1

n_b_rot_train += 46
n_b_rot_valid += 5
n_b_rot_test += 15

n_healthy_train += 45
n_healthy_valid += 5
n_healthy_test += 15

"""print("B ROT TRAIN " + str(n_b_rot_train))
print("B ROT VALID " + str(n_b_rot_valid))
print("B ROT TEST " + str(n_b_rot_test))
print("H TRAIN " + str(n_healthy_train))
print("H VALID " + str(n_healthy_valid))
print("H TEST " + str(n_healthy_test))"""

data = [n_b_rot_train, n_b_rot_valid, n_b_rot_test, n_healthy_train, n_healthy_valid, n_healthy_test]
labels = ["black_rot train", "black_rot valid", "black_rot test", "healthy train", "healthy valid", "healthy test"]

plt.bar(labels, data)

plt.title("Distribuzione delle classi")
plt.xlabel("Classe")
plt.ylabel("Valori")

plt.show()
