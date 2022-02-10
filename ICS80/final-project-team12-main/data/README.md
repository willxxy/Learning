# Source of Data: https://archive.ics.uci.edu/ml/datasets/Deepfakes%3A+Medical+Image+Tamper+Detection



exp1_known_AI_instances - 
"data/Response EXP1 - AI_instances.csv"

exp1_known_AI_patients -
"data/Response EXP1 - AI_patients.csv"


exp1_known_reviewer1_instances -
"data/Response EXP1 - Reviewer 1_instances.csv"


exp1_known_reviewer1_patients -
"data/Response EXP1 - Reviewer 1_patients.csv"


exp1_known_reviewer2_instances -
"data/Response EXP1 - Reviewer 2_instances.csv"


exp1_known_reviewer2_patients -
"data/Response EXP1 - Reviewer 2_patients.csv"


exp1_known_reviewer3_instances -
"data/Response EXP1 - Reviewer 3_instances.csv"


exp1_known_reviewer3_patients -
"data/Response EXP1 - Reviewer 3_patients.csv"


exp2_unknown_reviewer1_instances -
"data/Response EXP2 - Reviewer 1_instances.csv"


exp2_unknown_reviewer1_patients -
"data/Response EXP2 - Reviewer 1_patients.csv"


exp2_unknown_reviewer2_instances -
"data/Response EXP2 - Reviewer 2_instances.csv"


exp2_unknown_reviewer2_patients -
"data/Response EXP2 - Reviewer 2_patients.csv"


exp2_unknown_reviewer3_instances -
"data/Response EXP2 - Reviewer 3_instances.csv"


exp2_unknown_reviewer3_patients -
"data/Response EXP2 - Reviewer 3_patients.csv"



# Number of Observations:

exp1_known_AI_instances - 133

exp1_known_AI_patients - 80

exp1_known_reviewer1_instances - 133

exp1_known_reviewer1_patients - 80

exp1_known_reviewer2_instances - 133

exp1_known_reviewer2_patients - 80

exp1_known_reviewer3_instances - 133

exp1_known_reviewer3_patients - 80

exp2_unknown_reviewer1_instances - 36

exp2_unknown_reviewer1_patients - 20

exp2_unknown_reviewer2_instances - 36

exp2_unknown_reviewer2_patients - 20

exp2_unknown_reviewer3_instances - 36

exp2_unknown_reviewer3_patients - 20

# Number of Variables:

exp1_known_AI_instances - 8

exp1_known_AI_patients - 13

exp1_known_reviewer1_instances - 8

exp1_known_reviewer1_patients - 13

exp1_known_reviewer2_instances - 8

exp1_known_reviewer2_patients - 13

exp1_known_reviewer3_instances - 8

exp1_known_reviewer3_patients - 13

exp2_unknown_reviewer1_instances - 10

exp2_unknown_reviewer1_patients - 13

exp2_unknown_reviewer2_instances - 10

exp2_unknown_reviewer2_patients - 13

exp2_unknown_reviewer3_instances - 10

exp2_unknown_reviewer3_patients - 13



# Codebook/Data Dictionary:
Experiment 1 is blind trials, and experiment 2 is open trials.

Blind trial has 10 scans of an original instance with no cancer,
10 scans of an original instance with cancer,
30 scans of a tampered instance with cancer removed, and
30 scans of a tampered instance with cancer injected.

Open trial has 5 scans of an original instance with no cancer,
5 scans of an original instance with cancer,
5 scans of a tampered instance with cancer removed, and
5 scans of a tampered instance with cancer injected.

Types of scans are True-Benign(TB), True-Malign(TM), False-Benign(FB), and False-Malign(FM).

- TB: an original instance with no cancer
- TM: an original instance with cancer
- FB: a tampered instance with cancer removed
- FM: a tampered instance with cancer injected

'x' refers to the x axis, 'y' refers to the y axis, and 'slice' refers to the z axis.

