from ultralytics import YOLO
import os

model = YOLO("yolov8n.pt")

file_name = input("Enter image or video name: ")

if os.path.isfile(file_name):
    model.predict(
        source=file_name,
        save=True,
        project="results",
        name="output",
        exist_ok=True
    )
    print("Detection completed!")
else:
    print("File not found!")