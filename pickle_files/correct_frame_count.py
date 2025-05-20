import pickle

with open("fitness-aqa-wrong-framecounts.pkl", mode="rb") as f:
    data = pickle.load(f)

for i in range(len(data["annotations"])):
    if data["annotations"][i]["total_frames"] != data["annotations"][i]["keypoint"].shape[1]:
        data["annotations"][i]["total_frames"] = data["annotations"][i]["keypoint"].shape[1]

with open("fitness-aqa.pkl", mode="wb") as f:
    pickle.dump(data, f)
