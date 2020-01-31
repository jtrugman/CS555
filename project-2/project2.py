# Author: Justin Trugman
# CS-555 Project02

def separate_line(ged_line):
    stripped = ged_line.strip('\n') 
    return stripped.split(" ")

def validate_tags (separate_lines):
    supported_zero_tags = ["INDI",  "FAM",  "HEAD", "TRLR", "NOTE"]
    supported_one_tags = ["NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "CHIL", "DIV"]
    supported_two_tags = ["DATE"]

    level = separate_lines.pop(0)
    tag = separate_lines.pop(0)
    args = " ".join(separate_lines)

    if (args in supported_zero_tags or args in supported_one_tags or args in supported_two_tags):
        temp = tag
        tag = args
        args = temp

    if (level == "0"):
        if tag in supported_zero_tags:
            valid = "Y"
        else:
            valid = "N"
    elif (level == "1"):
        if tag in supported_one_tags:
            valid = "Y"
        else: 
            valid = "N"
    elif (level == "2"):
        if tag in supported_two_tags:
            valid = "Y"
        else:
            valid = "N"
    else: 
        valid = "N"

    return "<-- " + level + "|" + tag + "|" + valid + "|" + args 
            




if __name__ == "__main__":
    file = open('./targaryen.ged')
    
    ged_lines = file.readlines()

    for ged_line in ged_lines:
        print ("--> " + ged_line)
        print(validate_tags(separate_line(ged_line)))
        print ("-------------------")

    file.close