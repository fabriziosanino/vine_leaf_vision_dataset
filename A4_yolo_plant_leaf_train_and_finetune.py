from ultralyticsplus import YOLO

if __name__ == "__main__":
    model = YOLO('foduucom/plant-leaf-detection-and-classification')

    results = model.train(data="conf_plant_leaf_train.yaml", epochs=100, device=0, project="yolo-plant-leaf-train-and-finetune")

    model = YOLO('yolo-plant-leaf-train-and-finetune\\train\\weights\\best.pt')

    results = model.train(data="conf_plant_leaf_train_finetune.yaml", epochs=50, device=0, project="yolo-plant-leaf-train-and-finetune")

    model = YOLO('yolo-plant-leaf-train-and-finetune\\train2\\weights\\best.pt')

    results = model.val(data="conf_plant_leaf_train_test.yaml", project="yolo-plant-leaf-train-and-finetune")
