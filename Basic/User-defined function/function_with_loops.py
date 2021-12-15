def cross_bridge(steps):
    for step in range(steps):
        print("Crossed steps")
    if steps > 5:
        print("The bridge is collapsing!")
    else:
        print("We must keep moving!")
cross_bridge(3)
cross_bridge(6)