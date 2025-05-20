import pickle

with open("fitness-aqa.pkl", mode="rb") as f:
    dict = pickle.load(f)

    for entry in dict["annotations"]:
        if entry["frame_dir"] == "66189_5":
            pass