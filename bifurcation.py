import numpy as np
import matplotlib.pyplot as plt
from logistic_map import logistic_map


def main():
    r_min = 2.5
    r_max = 4.0
    num_r = 5000

    iterations = 1000
    last = 100

    r_values = np.linspace(r_min, r_max, num_r)
    x = np.full(num_r, 0.5)

    plt.figure(figsize=(12, 8))

    for i in range(iterations):
        x = logistic_map(r_values, x)

        if i >= (iterations - last):
            plt.plot(r_values, x, ",k", alpha=0.25)

    plt.title("Bifurcation Diagram of the Logistic Map")
    plt.xlabel("r")
    plt.ylabel("x")
    plt.tight_layout()
    plt.savefig("bifurcation_diagram.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()
