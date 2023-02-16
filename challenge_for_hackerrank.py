import re

for a in range(int(input())):
    check = input()
   
    rule1 = bool(re.match(r"^[456]\d{15}$", check))
    ruleNext = bool(re.match(r"^[456]\d{3}\-\d{4}\-\d{4}\-\d{4}$", check))
   
    num  = check.replace("-", "")
    ruleNext2 = bool(re.match(r"(?!.*(\d)(-?\1){3})", num))
   
    if (rule1 or ruleNext) and ruleNext2:
        print("Valid")
    else:
        print("Invalid")
