import json
import pickle


def relabel_annotations(ann, labels):
    for i in range(len(ann)):
        ann[i]["label"] = int(labels[ann[i]["frame_dir"]] != [])
    return ann


with open("../pickle_files/fitness-aqa.pkl", mode="rb") as f:
    data = pickle.load(f)

with open("error_elbows.json", mode="rt") as f:
    elbow_labels = json.load(f)

with open("error_knees.json", mode="rt") as f:
    knee_labels = json.load(f)

ann_elbows = relabel_annotations(data["annotations"], elbow_labels)
ann_knees = relabel_annotations(data["annotations"], knee_labels)

data_elbows = data
data_elbows["annotations"] = ann_elbows
with open("../pickle_files/fitness-aqa-elbows.pkl", mode="wb") as f:
    pickle.dump(data_elbows, f)

data_knees = data
data_knees["annotations"] = ann_knees
with open("../pickle_files/fitness-aqa-knees.pkl", mode="wb") as f:
    pickle.dump(data_knees, f)
