import numpy as np
from scipy.spatial import ConvexHull

def calculate_flatness(df):
    """
    Prosta metoda przybliżająca płaskość jako max różnicę wysokości (Z) po optymalnym obrocie.
    W praktyce można poszukać minimalnej odległości między dwoma równoległymi płaszczyznami
    zawierającymi chmurę punktów.
    """
    # zs = points[:, 2]
    print(df)
    print("Kolumny w df:", df.columns.tolist())
    zs = df['z'].to_numpy()
    flatness = np.max(zs) - np.min(zs)
    return flatness