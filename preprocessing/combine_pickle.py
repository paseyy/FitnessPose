import pickle

TYPE = "track"
assert TYPE in ["track", "full", ""]

with open(f'../pickle_files/correct_{TYPE}.pkl', mode='rb') as f:
    correct = pickle.load(f)

with open(f'../pickle_files/knees_error_{TYPE}.pkl', mode='rb') as f:
    knees_error = pickle.load(f)

with open(f'../pickle_files/elbows_error_{TYPE}.pkl', mode='rb') as f:
    elbows_error = pickle.load(f)

out = {}
split = {}
for set in ("train", "val", "test"):
    split[set] = correct["split"][set] + knees_error["split"][set] + elbows_error["split"][set]

out["split"] = split
annotations = correct["annotations"] + knees_error["annotations"] + elbows_error["annotations"]
out["annotations"] = annotations

with open(f'../pickle_files/fitness-aqa-wrong-framecounts-{TYPE}.pkl', mode='wb') as f:
    pickle.dump(out, f)
