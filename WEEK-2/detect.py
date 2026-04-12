from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run detection
results = model("https://ultralytics.com/images/bus.jpg", show=True)

# Save results
results[0].save()