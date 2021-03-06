import matplotlib.pyplot as plt
import convexHull
import sorters
import fn
import time

n = 100
points = []
times = []
title = ("Bubble Sort", "Quick Sort", "Insertion Sort", "Merge Sort")

for i in range(4):
    n = 100
    for j in range(20):
        # making the points to plot, from 100 to 1000 with step 100
        fn.make_points(points, n)
        start = time.time()  # start the timer
        if i != 3:
            sorters.choose_sorter(i, points)
        else:
            points = sorters.merge_sort(points)
        hull = convexHull.convex_hull(points)
        end = time.time()  # end the timer after sorting
        times.append((n, end-start))
        if n in (100, 500, 1000):
            colors = []

            for x in points:
                if x in hull:
                    colors.append('red')
                else:
                    colors.append('blue')

            plt.scatter([x[0] for x in points], [y[1] for y in points], s=10, c=colors)
            for _ in range(len(hull)):
                x = [val[0] for val in hull]
                y = [val[1] for val in hull]
                x.append(hull[0][0])
                x.append(hull[-1][0])
                y.append(hull[0][1])
                y.append(hull[-1][-1])
                plt.plot(x, y)
            the_title = title[i] + " " + str(n) + " Points"
            plt.title(the_title)
            plt.show()
        n += 100
    print("all the times ")
    print("No of points, time")
    print(*times)
    plt.scatter([x[0] for x in times], [y[1] for y in times], s=10)
    plt.show()
    points.clear()
    times.clear()

