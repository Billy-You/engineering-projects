import numpy as np


def adc_to_angle(adc: float) -> float:
    """
    Convierte un valor ADC (0-1023) a un ángulo objetivo (0-180 grados).
    """
    adc_clamped = np.clip(adc, 0, 1023)
    return 180.0 * adc_clamped / 1023.0


def first_order_servo_response(theta_ref, t, tau=0.15):
    """
    Simula la respuesta de un servo con modelo de primer orden:
        tau * dtheta/dt + theta = theta_ref

    Parámetros:
        theta_ref : array de referencia angular [deg]
        t         : array de tiempos [s]
        tau       : constante de tiempo [s]

    Devuelve:
        theta     : array de posición angular simulada [deg]
    """
    theta = np.zeros_like(theta_ref, dtype=float)
    dt = t[1] - t[0]

    for k in range(1, len(t)):
        dtheta = (theta_ref[k - 1] - theta[k - 1]) / tau
        theta[k] = theta[k - 1] + dtheta * dt

    return theta
    