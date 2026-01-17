# slopier_1.0
Density-aware 1D interpolation models that outperform linear regression on structured data.

# Slopier = Slop Pair

Slopier is a lightweight, deterministic 1D regression/interpolation module designed for **small, structured datasets**.  
It focuses on **local geometry**, **neighbor spacing**, and **curve continuity** instead of global fitting.

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

## Model

### 1️⃣  Slopier
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
