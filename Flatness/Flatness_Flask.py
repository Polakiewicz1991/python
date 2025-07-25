"Działa ale wyrkesy są statyczne, więc nie bardzo dam radę użyć tego jak programu webowego"

from flask import Flask, Response, render_template_string
import io
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # konieczne dla pracy z Flask, bez GUI
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.mplot3d import Axes3D  # wymóg pmplot3d

app = Flask(__name__)

@app.route('/')
def plot_3d_views():
    # Ścieżka do pliku - dostosuj do swojej
    path = r"E:\PP\22_0014_0000 - ADAPTSYS Walcarka\Pomiary\Nowe pomiary demonstratorów na walcarce z wykorzystaniem portalu, obrotnicy i kamery. Dane wpisywane przez operatora\Pomiar blachy 9"
    name = r"28BL2406x1206_S4-43_ID186_POM1_2024_02_01_08_32_28.txt"
    filename = path + '\\' + name

    # Wczytanie danych analogicznie do Twojego kodu
    header_line = None
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if line.strip().startswith('Punkty pomiarowe:'):
                header_line = i
                break
    if header_line is None:
        return "Nie znaleziono nagłówka danych", 500

    df = pd.read_csv(
        filename,
        sep='\t',
        skiprows=header_line,
        header=0,
        index_col=0,
        encoding='utf-8'
    )
    df.columns = [col.strip().replace(':', '') for col in df.columns]
    df = df.reset_index()

    x = df['X'].values
    y = df['Y'].values
    z = df['Wartosc Raw'].values

    flatness = z.max() - z.min()

    A = np.c_[x, y, np.ones_like(x)]
    coeffs, _, _, _ = np.linalg.lstsq(A, z, rcond=None)
    a, b, c = coeffs
    z_plane = a * x + b * y + c
    deviation = z - z_plane

    xlim = [x.min(), x.max()]
    ylim = [y.min(), y.max()]
    X_grid, Y_grid = np.meshgrid(np.linspace(*xlim, 10), np.linspace(*ylim, 10))
    Z_grid = a * X_grid + b * Y_grid + c

    z_min_limit = 15
    z_max_limit = 18

    # Rysowanie wykresu do bufora
    fig = plt.figure(figsize=(18, 8))
    fig.suptitle(name, fontsize=20)
    fig.text(0.45, 0.94, f'Płaskość: {flatness:.4f}', ha='left', va='top', fontsize=16)
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    # Widok z góry (XY)
    ax1 = fig.add_subplot(gs[0, 1], projection='3d')
    scat1 = ax1.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
    ax1.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
    ax1.view_init(elev=90, azim=-90)
    ax1.set_title('Widok z góry (XY)')
    ax1.set_xlim(xlim)
    ax1.set_ylim(ylim)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_box_aspect((1, 2, 0.5))
    ax1.set_zlim(z_min_limit, z_max_limit)

    # Widok z boku (XZ)
    ax2 = fig.add_subplot(gs[1, 1], projection='3d')
    scat2 = ax2.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
    ax2.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
    ax2.view_init(elev=0, azim=-90)
    ax2.set_title('Widok z boku (XZ)')
    ax2.set_xlim(xlim)
    ax2.set_ylim(ylim)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    ax2.set_box_aspect((1, 2, 0.5))
    ax2.set_zlim(z_min_limit, z_max_limit)

    # Widok ukośny (elewacja 45°, azymut -45°)
    ax3 = fig.add_subplot(gs[:, 0], projection='3d')
    scat3 = ax3.scatter(x, y, z, c=deviation, cmap='bwr', s=30, vmin=-1, vmax=1)
    ax3.plot_surface(X_grid, Y_grid, Z_grid, color='red', alpha=0.4)
    ax3.view_init(elev=45, azim=-45)
    ax3.set_title('Widok pośredni (45° ukośny)')
    ax3.set_xlim(xlim)
    ax3.set_ylim(ylim)
    ax3.set_xlabel('X')
    ax3.set_ylabel('Y')
    ax3.set_zlabel('Z')
    ax3.set_box_aspect((1, 2, 0.5))
    ax3.set_zlim(z_min_limit, z_max_limit)

    cbar = fig.colorbar(scat1, ax=[ax1, ax2, ax3], shrink=0.6, pad=0.05)
    cbar.set_label('Odchylenie od płaszczyzny')

    # Zapis do bufora
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    plt.close(fig)
    buf.seek(0)

    # Prosta strona HTML osadzająca obraz wykresu
    html = f"""
    <html>
    <head><title>Wykres 3D płaskości</title></head>
    <body>
      <h1>Wykres 3D płaskości: {name}</h1>
      <p>Płaskość: {flatness:.4f}</p>
      <img src="data:image/png;base64,{buf.getvalue().hex()}" alt="Wykres 3D">
    </body>
    </html>
    """

    import base64
    img_data = base64.b64encode(buf.getvalue()).decode('ascii')

    return render_template_string(f"""
    <html>
      <head><title>Wykres 3D płaskości</title></head>
      <body>
        <h1>Wykres 3D płaskości: {name}</h1>
        <p>Płaskość: {flatness:.4f}</p>
        <img src="data:image/png;base64,{img_data}" alt="Wykres 3D" style="max-width:100%;height:auto;">
      </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)