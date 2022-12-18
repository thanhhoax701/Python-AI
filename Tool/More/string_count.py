import numpy as np

def main():
    s = np.array(list("LOVERS LOVE ROSE"))
    print(''.join(s))
    values, counts = np.unique(s, return_counts=True)
    for i in range(len(values)):
        print("'{}': {}".format(values[i], counts[i]/len(s)))

if __name__ == "__main__":
    main()