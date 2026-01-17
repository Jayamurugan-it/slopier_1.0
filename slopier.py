import pandas as pd
import numpy as np

class Slopier:
    """
    1D slope interpolation model (your SlopePair / slope-copy logic)
    - Uses nearest neighbors
    - Skips points if spacing is too large
    - Linear interpolation between neighbors
    """
    def __init__(self, x_col, y_col, gap_ratio=2.0):
        self.df = pd.DataFrame({"x": x_col, "y": y_col})
        self.df = self.df.sort_values("x").reset_index(drop=True)
        self.gap_ratio = gap_ratio

    def _select_neighbors(self, xq):
        xs = self.df["x"].values
        idx = np.searchsorted(xs, xq)

        # candidate indices around xq
        candidates = []
        for i in [idx - 2, idx - 1, idx, idx + 1, idx + 2]:
            if 0 <= i < len(xs):
                candidates.append(i)

        if len(candidates) < 2:
            # if only one neighbor, extend line to infinity
            if len(candidates) == 1:
                return candidates[0], candidates[0]
            return None

        # compute gaps between consecutive candidates
        gaps = [abs(xs[candidates[i+1]] - xs[candidates[i]]) for i in range(len(candidates)-1)]

        # skip large gap logic
        for i in range(len(gaps)-1):
            if gaps[i] > self.gap_ratio * gaps[i+1]:
                return candidates[i], candidates[i+2]

        # default: nearest two
        return candidates[1], candidates[2]

    def predict(self, x_query):
        """
        x_query: pandas Series of x values
        returns: DataFrame with predicted y-values
        """
        preds = []
        for xq in x_query:
            pair = self._select_neighbors(xq)
            if pair is None:
                preds.append(np.nan)
                continue
            i, j = pair
            x1, y1 = self.df.iloc[i]
            x2, y2 = self.df.iloc[j]

            # linear interpolation
            if x2 != x1:
                y_pred = y1 + (y2 - y1) * (xq - x1) / (x2 - x1)
            else:
                y_pred = y1
            preds.append(y_pred)

        return pd.DataFrame({"x": x_query.values, "y": preds})