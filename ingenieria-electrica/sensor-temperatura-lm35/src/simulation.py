from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

VREF = 5.0
ADC_MAX = 1023


def main() -> None:
    output_dir = Path("data/processed")
    figures_dir = Path("results/figures")
    output_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    temperatura_c = np.linspace(0, 50, 200)
    voltaje_v = 0.01 * temperatura_c
    adc = (voltaje_v / VREF) * ADC_MAX

    df = pd.DataFrame(
        {
            "temperatura_c": temperatura_c,
            "voltaje_v": voltaje_v,
            "adc": adc,
        }
    )

    csv_path = output_dir / "lm35_simulation.csv"
    df.to_csv(csv_path, index=False)

    print("Primeros 10 valores simulados:")
    print(df.head(10).to_string(index=False))
    print(f"\nCSV guardado en: {csv_path}")

    plt.figure(figsize=(8, 5))
    plt.plot(temperatura_c, voltaje_v)
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Voltaje de salida (V)")
    plt.title("LM35 ideal: Temperatura vs Voltaje")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(figures_dir / "lm35_temperatura_vs_voltaje.png", dpi=300)
    plt.show()

    plt.figure(figsize=(8, 5))
    plt.plot(temperatura_c, adc)
    plt.xlabel("Temperatura (°C)")
    plt.ylabel("Lectura ADC")
    plt.title("LM35 ideal: Temperatura vs ADC")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(figures_dir / "lm35_temperatura_vs_adc.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()