from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def main() -> None:
    data_path = Path("data/processed/lm35_simulation.csv")
    figures_path = Path("results/figures")
    figures_path.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(data_path)

    print("Resumen de datos simulados:")
    print(df.head(10))
    print("\nEstadísticas:")
    print(df.describe())

    plt.figure(figsize=(8, 5))
    plt.plot(df["temperatura_c"], df["voltaje_v"])
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Voltaje de salida (V)")
    plt.title("LM35: análisis de datos simulados")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(figures_path / "lm35_analisis_voltaje.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()