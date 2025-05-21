import pickle

with open("fitness-aqa.pkl", mode="rb") as f:
    data = pickle.load(f)

    for entry in data["annotations"]:
        if entry["frame_dir"] == "64462_2":
            pass
    pass