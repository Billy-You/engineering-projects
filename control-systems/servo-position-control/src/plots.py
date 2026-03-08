import matplotlib.pyplot as plt
from simulation import run_simulation


def plot_results():
    t, theta_ref, theta = run_simulation()

    plt.figure(figsize=(10, 5))
    plt.plot(t, theta_ref, label="Referencia angular")
    plt.plot(t, theta, label="Respuesta simulada")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Ángulo [deg]")
    plt.title("Simulación de servo con modelo de primer orden")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("results/servo_simulation.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    plot_results()