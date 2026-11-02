"""Stor-IA di Torino - effetto minimo rilevabile (MDE) per il disegno sperimentale.

t non centrale, alpha = 0.05 bilaterale, potenza = 0.80.
Confronto tra bracci: ANCOVA con il punteggio pre come covariata, che riduce
la varianza residua di un fattore (1 - r^2), dove r = correlazione pre-post.
Versione 2 novembre 2026.
"""
import numpy as np
from scipy import stats, optimize

ALPHA, POWER = 0.05, 0.80


def power_two_sample(d, n1, n2, r_pre=0.0, k_cov=0):
    d_eff = d / np.sqrt(1 - r_pre**2)
    df = n1 + n2 - 2 - k_cov
    ncp = d_eff * np.sqrt(n1 * n2 / (n1 + n2))
    tcrit = stats.t.ppf(1 - ALPHA / 2, df)
    return stats.nct.sf(tcrit, df, ncp) + stats.nct.cdf(-tcrit, df, ncp)


def power_paired(dz, n):
    df, ncp = n - 1, dz * np.sqrt(n)
    tcrit = stats.t.ppf(1 - ALPHA / 2, df)
    return stats.nct.sf(tcrit, df, ncp) + stats.nct.cdf(-tcrit, df, ncp)


def mde(fun):
    return optimize.brentq(lambda d: fun(d) - POWER, 0.05, 0.9)


if __name__ == "__main__":
    print("A) Due bracci (agenti vs contenuti curati dagli enti)")
    for n in (50, 45, 40):
        for r in (0.0, 0.5, 0.6):
            d = mde(lambda d: power_two_sample(d, n, n, r, k_cov=1 if r else 0))
            print(f"   n={n}/braccio, r pre-post={r:.1f} -> d minimo = {d:.2f}")
    print("B) Confronti tra agenti, entro soggetto")
    for n in (100, 90, 50, 45):
        print(f"   n={n} -> dz minimo = {mde(lambda d: power_paired(d, n)):.2f}")
    print("C) Disegno originale a 4 bracci da 25, confronto a coppie, r=0.5")
    print(f"   d minimo = {mde(lambda d: power_two_sample(d, 25, 25, 0.5, 1)):.2f}")
