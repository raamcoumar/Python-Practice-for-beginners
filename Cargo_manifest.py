import time

# each item in the manifest is an item and its weight
manifest = [["bananas", 15], ["mattresses", 34], ["dog kennels",42], ["machine that goes ping!", 120], ["tea chests", 10], ["cheeses", 0]]

cargo_weight = 0
cargo_hold = []

for cargo in manifest:
    print("debug: the weight is currently: {}\n".format(cargo_weight))
    if cargo_weight + cargo[1] >= 100:
        print("debug: breaking loop now!")
        time.sleep(1)
        break
    else:
        print("debug: adding item: {}".format(cargo[0]))
        time.sleep(1)
        print("debug: with weight: {}\n".format(cargo[1]))
        time.sleep(1)
        cargo_hold.append(cargo[0])
        cargo_weight += cargo[1]
        print ("Items loaded: {}".format(cargo_hold))

