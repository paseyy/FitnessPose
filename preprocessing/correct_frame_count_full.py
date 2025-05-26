import pickle

with open("../pickle_files/fitness-aqa-wrong-framecounts-full.pkl", mode="rb") as f:
    data = pickle.load(f)

for i in range(len(data["annotations"])):
    data["annotations"][i]["total_frames"] = data["annotations"][i]["keypoint"].shape[1]

with open("../pickle_files/fitness-aqa-full.pkl", mode="wb") as f:
    pickle.dump(data, f)
