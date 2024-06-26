from ultralyticsplus import YOLO

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")

    results = model.train(data="conf_without_pretraining.yaml", epochs=50, device=0, project="yolo-without-pretraining", pretrained=False)

    model = YOLO("yolo-without-pretraining\\train\\weights\\best.pt")

    results = model.val(data="conf_without_pretraining_test.yaml", project="yolo-without-pretraining")

    model = YOLO('foduucom/plant-leaf-detection-and-classification')

    results = model.train(data="conf_plant_leaf_finetune.yaml", epochs=50, device=0, project="yolo-plant-leaf-detection")

    model = YOLO('yolo-plant-leaf-detection\\train\\weights\\best.pt')

    results = model.val(data="conf_plant_leaf_finetune_test.yaml", project="yolo-plant-leaf-detection")

    model = YOLO('yolov8n.pt')

    results = model.train(data="conf_vanilla_train.yaml", epochs=100, device=0, project="yolo-vanilla-train-and-finetune", pretrained=False)

    model = YOLO('yolo-vanilla-train-and-finetune\\train\\weights\\best.pt')

    results = model.train(data="conf_vanilla_train_finetune.yaml", epochs=50, device=0, project="yolo-vanilla-train-and-finetune")

    model = YOLO('yolo-vanilla-train-and-finetune\\train2\\weights\\best.pt')

    results = model.val(data="conf_vanilla_train_test.yaml", project="yolo-vanilla-train-and-finetune")

    model = YOLO('foduucom/plant-leaf-detection-and-classification')

    results = model.train(data="conf_plant_leaf_train.yaml", epochs=100, device=0, project="yolo-plant-leaf-train-and-finetune")

    model = YOLO('yolo-plant-leaf-train-and-finetune\\train\\weights\\best.pt')

    results = model.train(data="conf_plant_leaf_train_finetune.yaml", epochs=50, device=0, project="yolo-plant-leaf-train-and-finetune")

    model = YOLO('yolo-plant-leaf-train-and-finetune\\train2\\weights\\best.pt')

    results = model.val(data="conf_plant_leaf_train_test.yaml", project="yolo-plant-leaf-train-and-finetune")
