import pickle

with open("../pickle_files/fitness-aqa.pkl", mode="rb") as f:
    data = pickle.load(f)

    for entry in data["annotations"]:
        if entry["frame_dir"] == "64462_2":
            pass
    pass