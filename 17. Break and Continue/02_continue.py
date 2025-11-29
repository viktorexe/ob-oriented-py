# Continue is used to skip that particular iteration

for i in range(10):
    if i == 4:
        print("Skipping this....")
        continue
    else:
        print("Hi", i)