import pickle

correct = {}
elbows_error = {}
knees_error = {}

with open('/home/pasey/Documents/DL/Project/FitnessPose/pickle_files/correct.pkl', mode='rb') as f:
    correct = pickle.load(f)

with open('/home/pasey/Documents/DL/Project/FitnessPose/pickle_files/knees_error.pkl', mode='rb') as f:
    knees_error = pickle.load(f)

with open('/home/pasey/Documents/DL/Project/FitnessPose/pickle_files/elbows_error.pkl', mode='rb') as f:
    elbows_error = pickle.load(f)

out = {}

split = {}
for set in ("train", "val", "test"):
    split[set] = correct["split"][set] + knees_error["split"][set] + elbows_error["split"][set]

out["split"] = split
annotations = correct["annotations"] + knees_error["annotations"] + elbows_error["annotations"]
out["annotations"] = annotations

with open('/home/pasey/Documents/DL/Project/FitnessPose/pickle_files/fitness-aqa.pkl', mode='wb') as f:
    pickle.dump(out, f)
