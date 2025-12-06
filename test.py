#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook
"""

# Numerical Methods Assignment 1 
# KABEER AHMED SHABEER AHMED , 64230037

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# REAL NEWTON — Example 1: f(x) = x² − 3x − 4
# -------------------------------------------------------------

def convergence(x1, x0, tolerance):
    return abs(x1 - x0) < tolerance

def newt_meth(x0, tolerance, max_iter):
    for i in range(max_iter):
        f_x0 = x0**2 - 3*x0 - 4
        f_prime_x0 = 2*x0 - 3

        if abs(f_prime_x0) < 1e-8:
            return (None, i, "derivative_zero")

        x1 = x0 - f_x0/f_prime_x0

        if convergence(x1, x0, tolerance):
            return (x1, i, "convergent")

        x0 = x1

    return (None, max_iter, "not_converged")

print("=== Real Newton Method Test 1 ===")
initial_guesses = [-10, -5, 0, 1, 5, 10]

for x0 in initial_guesses:
    root, iterations, status = newt_meth(x0, 1e-6, 25)
    print(f"x0 = {x0} ---- root = {root}, iteration no = {iterations}, status = {status}")


# -------------------------------------------------------------
# REAL NEWTON — Example 2: f(x) = x² + 2x − 3
# -------------------------------------------------------------

def newt_meth2(x0, tolerance, max_iter):
    for i in range(max_iter):
        f_x0 = x0**2 + 2*x0 - 3     # <-- FIXED SIGN (you had +3)
        f_prime_x0 = 2*x0 + 2

        if abs(f_prime_x0) < 1e-8:
            return (None, i, "derivative_zero")

        x1 = x0 - f_x0/f_prime_x0

        if convergence(x1, x0, tolerance):
            return (x1, i, "convergent")

        x0 = x1

    return (None, max_iter, "not_converged")

print("\n=== Real Newton Method Test 2 ===")
for x0 in initial_guesses:
    root, iterations, status = newt_meth2(x0, 1e-6, 25)
    print(f"x0 = {x0} ---- root = {root}, iteration no = {iterations}, status = {status}")


# -------------------------------------------------------------
# COMPLEX NEWTON — f(z) = z³ − 1
# -------------------------------------------------------------

def newt_complex_meth(z0, tolerance, max_iter):
    z = z0
    for i in range(max_iter):

        f_z = z**3 - 1
        f_prime_z = 3*z**2

        if abs(f_prime_z) < 1e-12:
            return (None, i, "derivative_zero")

        z_new = z - f_z / f_prime_z

        if abs(z_new - z) < tolerance:
            return (z_new, i, "convergent")

        z = z_new

    return (None, max_iter, "not_converged")

print("\n=== Complex Newton Method Tests (z^3 - 1) ===")

complex_initials = [
    0.5 + 0.5j,
    -1 + 0.2j,
    2 - 1j,
    -0.3 - 0.7j,
    1 + 1j
]

for z0 in complex_initials:
    root, iters, status = newt_complex_meth(z0, 1e-6, 25)
    print(f"z0 = {z0}, root = {root}, iteration no = {iters}, status = {status}")
