from ultralyticsplus import YOLO

if __name__ == "__main__":
    model = YOLO('foduucom/plant-leaf-detection-and-classification')

    results = model.train(data="conf_plant_leaf_finetune.yaml", epochs=50, device=0, project="yolo-plant-leaf-detection")

    model = YOLO('yolo-plant-leaf-detection\\train\\weights\\best.pt')

    results = model.val(data="conf_plant_leaf_finetune_test.yaml", project="yolo-plant-leaf-detection")