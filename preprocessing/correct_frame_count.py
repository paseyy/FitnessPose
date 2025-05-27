import pickle

TYPE = "track"
assert TYPE in ["track", "full", ""]

with open(f"../pickle_files/fitness-aqa-wrong-framecounts-{TYPE}.pkl", mode="rb") as f:
    data = pickle.load(f)

for i in range(len(data["annotations"])):
    data["annotations"][i]["total_frames"] = data["annotations"][i]["keypoint"].shape[1]

with open(f"../pickle_files/fitness-aqa-{TYPE}.pkl", mode="wb") as f:
    pickle.dump(data, f)
