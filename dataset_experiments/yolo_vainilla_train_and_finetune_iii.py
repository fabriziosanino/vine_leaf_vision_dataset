from ultralyticsplus import YOLO

if __name__ == "__main__":
    model = YOLO('yolov8n.pt')

    results = model.train(data="conf_vanilla_train.yaml", epochs=100, device=0, project="yolo-vanilla-train-and-finetune", pretrained=False)

    model = YOLO('yolo-vanilla-train-and-finetune\\train\\weights\\best.pt')

    results = model.train(data="conf_vanilla_train_finetune.yaml", epochs=50, device=0, project="yolo-vanilla-train-and-finetune")

    model = YOLO('yolo-vanilla-train-and-finetune\\train2\\weights\\best.pt')

    results = model.val(data="conf_vanilla_train_test.yaml", project="yolo-vanilla-train-and-finetune")
