import os
import csv
import sys
import joblib

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

MODELPATH = os.path.join(root, "..", "..", "checkpoints")


# my model
def my_model(smiles_list):
    mdl1 = joblib.load(os.path.join(MODELPATH, "hdac1_bin7_morgan_model.joblib"))
    mdl2 = joblib.load(os.path.join(MODELPATH, "hdac1_bin8_morgan_model.joblib"))

    y_pred1 = mdl1.predict_proba(smiles_list)[:,1]
    y_pred2 = mdl2.predict_proba(smiles_list)[:,1]

    return y_pred1, y_pred2


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output1, output2  = my_model(smiles_list)

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["hdac1_inh_pIC50_7", "hdac1_inh_pIC50_8"])  # header with column names
    for o1, o2 in zip(output1, output2):
        writer.writerow([o1, o2])
