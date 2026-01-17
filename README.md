# slopier_1.0
Density-aware 1D interpolation models that outperform linear regression on structured data.

# Slopier

Slopier is a lightweight, deterministic 1D regression/interpolation module designed for **small, structured datasets**.  
It focuses on **local geometry**, **neighbor spacing**, and **curve continuity** instead of global fitting.

This repository contains two models:
- **HorizontalSlope**
- **SlopePair** (density-aware, gap-skipping interpolation)

---

## Why Slopier?

Traditional models fail in this setup:

| Model | Problem |
|-----|-------|
| Linear Regression | Cannot model curvature |
| Decision Tree | Piecewise jumps, loses smoothness |
| Neural Networks | Overkill, slow, unstable on small data |

Slopier works best when:
- Data is **ordered (1D)**
- Dataset is **small (10–500 points)**
- Shape matters more than global fitting
- Missing values need accurate reconstruction

---

## Models

### 1️⃣ HorizontalSlope
- Finds left & right neighbors
- Predicts using **average of their y-values**
- Produces a **horizontal segment**
- Extremely stable under noise

Best for:
- Missing value filling
- Noisy datasets
- Flat-trend approximation

---

### 2️⃣ SlopePair (Main Model)
- Finds surrounding neighbors
- **Skips unreliable points** when x-spacing is irregular
- Uses **local linear interpolation**
- Extrapolates using last known slope if needed

Key innovation:
> Neighbor selection is **density-aware**, not distance-only.

---

## Installation

No installation needed.

```bash
git clone https://github.com/Jayamurugan-it/slopier.git
