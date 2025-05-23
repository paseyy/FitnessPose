import json
import os
import matplotlib.pyplot as plt
import sys
import re
from numpy import mean

def load_training_data(log_file):
    results = {"train_loss": [],
               "val_loss": [],
               "train_top1_acc": [],
               "val_top1_acc": []}

    for line in f:
        iteration_data = json.loads(line)
        try:
            mode = iteration_data["mode"]
        except KeyError:
            continue

        results[mode + "_loss"].append(iteration_data["loss"])
        results[mode + "_top1_acc"].append(iteration_data["top1_acc"])

    num_epochs = len(results["val_loss"])
    epoch_size = len(results["train_loss"]) // num_epochs
    temp_loss = []
    temp_top1 = []
    for i in range(num_epochs):
        temp_loss.append(mean(results["train_loss"][(i * epoch_size):((i+1) * epoch_size)]))
        temp_top1.append(mean(results["train_top1_acc"][(i * epoch_size):((i + 1) * epoch_size)]))

    results["train_loss"] = temp_loss
    results["train_top1_acc"] = temp_top1
    return results


def plot_training(data, metric="loss"):
    model_name = re.split(r"[\\/]", args[1])[1]
    layers_frozen = 1
    lr = 0.01
    momentum = 0.9
    weight_decay = 0.0003

    title = (model_name + "\ntrained with\n"
             f"lr = {lr}\n"
             f"momentum = {momentum}\n"
             f"weight_decay = {weight_decay}\n"
             f"{layers_frozen} frozen layers\n")

    fig, ax = plt.subplots(figsize=(10,8))
    ax.plot(data["train_" + metric], label="train")
    ax.plot(data["val_" + metric], label="val")
    plt.subplots_adjust(top=0.8)

    plt.xlabel("epochs")
    plt.ylabel(metric)
    plt.suptitle(title)
    plt.legend()
    plt.grid()
    plt.savefig(f"{model_name}_" + metric + ".png")
    plt.show()


if __name__ == "__main__":
    args = sys.argv
    print("Opening folder", args[1])

    newdir = os.path.join(os.getcwd(), args[1])
    os.chdir(newdir)
    files = os.listdir(os.getcwd())
    log_filename = ""
    for filename in files:
        if filename[-9:] == ".log.json":
            log_filename = os.path.abspath(filename)

    try:
        with open(log_filename, "rt") as f:
            training_results = load_training_data(f)
    except Exception as e:
        print("No log file present:", e)

    plot_training(training_results, "loss")
    plot_training(training_results, "top1_acc")