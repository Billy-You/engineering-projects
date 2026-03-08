import numpy as np
from model import first_order_servo_response


def generate_step_reference(t, step_times, step_values):
    """
    Genera una referencia angular escalonada.

    step_times: lista de tiempos en los que cambia la referencia
    step_values: lista de valores angulares correspondientes
    """
    theta_ref = np.zeros_like(t, dtype=float)

    for i, time_value in enumerate(t):
        for j in range(len(step_times)):
            if time_value >= step_times[j]:
                theta_ref[i] = step_values[j]

    return theta_ref


def run_simulation():
    t = np.linspace(0, 8, 2000)

    step_times = [0, 2, 4, 6]
    step_values = [0, 45, 120, 70]

    theta_ref = generate_step_reference(t, step_times, step_values)
    theta = first_order_servo_response(theta_ref, t, tau=0.18)

    return t, theta_ref, theta