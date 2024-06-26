from ultralyticsplus import YOLO

if __name__ == "__main__":
  model = YOLO("yolov8n.pt")

  results = model.train(data="conf_without_pretraining.yaml", epochs=50, device=0, project="yolo-without-pretraining", pretrained=False)

  model = YOLO("yolo-without-pretraining\\train\\weights\\best.pt")

  results = model.val(data="conf_without_pretraining_test.yaml", project="yolo-without-pretraining")