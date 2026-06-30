import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# ====== PARAMETRY ======
R = 31
X, Y = 75, 52

# Twoje kąty (stopnie)
A_deg = 0   # obrót wokół Z
B_deg = 15    # obrót wokół Y
C_deg = 15   # obrót wokół X

# konwersja na radiany
A = np.radians(A_deg)
B = np.radians(B_deg)
C = np.radians(C_deg)


# ====== MACIERZE ROTACJI ======
def Rz(a):
    return np.array([
        [np.cos(a), -np.sin(a), 0],
        [np.sin(a),  np.cos(a), 0],
        [0, 0, 1]
    ])

def Ry(a):
    return np.array([
        [ np.cos(a), 0, np.sin(a)],
        [0, 1, 0],
        [-np.sin(a), 0, np.cos(a)]
    ])

def Rx(a):
    return np.array([
        [1, 0, 0],
        [0, np.cos(a), -np.sin(a)],
        [0, np.sin(a),  np.cos(a)]
    ])

# stała rotacja lokalna
R_local = Rz(A) @ Ry(B) @ Rx(C)

# ===== GENEROWANIE PUNKTÓW =====
points = []


n = 37
for i in range(n):
    phi = 2 * np.pi * i / (n - 1)  # zamknięcie okręgu

    # punkt na okręgu
    x = X + R * np.cos(phi)
    y = Y + R * np.sin(phi)
    z = 0

    # lokalny układ
    tangent = np.array([-np.sin(phi), np.cos(phi), 0])
    normal = np.array([np.cos(phi), np.sin(phi), 0])
    binormal = np.array([0, 0, 1])

    R_frame = np.column_stack((tangent, normal, binormal))

    # wektor Y2
    v_local = np.array([0, 1, 0])
    v_rot = R_local @ v_local
    v = R_frame @ v_rot

    # NORMALIZACJA
    v = v / np.linalg.norm(v)

    # ===== KĄTY ORIENTACJI =====
    # kąty względem osi
    alpha_X = np.degrees(np.arccos(v[0]))
    alpha_Y = np.degrees(np.arccos(v[1]))
    alpha_Z = np.degrees(np.arccos(v[2]))

    # zapis
    points.append({
        "x": x,
        "y": y,
        "z": z,
        "A": alpha_Z,  # względem Z
        "B": alpha_Y,  # względem Y
        "C": alpha_X   # względem X
    })

# ===== GENEROWANIE PUNKTÓW =====
points = []

for i in range(n):
    phi = 2 * np.pi * i / (n - 1)  # zamknięcie okręgu

    # punkt na okręgu
    x = X + R * np.cos(phi)
    y = Y + R * np.sin(phi)
    z = 0

    # lokalny układ
    tangent = np.array([-np.sin(phi), np.cos(phi), 0])
    normal = np.array([np.cos(phi), np.sin(phi), 0])
    binormal = np.array([0, 0, 1])

    R_frame = np.column_stack((tangent, normal, binormal))

    # wektor Y2
    v_local = np.array([0, 1, 0])
    v_rot = R_local @ v_local
    v = R_frame @ v_rot

    # NORMALIZACJA
    v = v / np.linalg.norm(v)

    # ===== KĄTY ORIENTACJI =====
    # kąty względem osi
    alpha_X = np.degrees(np.arccos(v[0]))
    alpha_Y = np.degrees(np.arccos(v[1]))
    alpha_Z = np.degrees(np.arccos(v[2]))

    # zapis
    points.append({
        "x": x,
        "y": y,
        "z": z,
        "A": alpha_Z,  # względem Z
        "B": alpha_Y,  # względem Y
        "C": alpha_X   # względem X
    })


# ===== WYJŚCIE =====
for i, p in enumerate(points):
    print(f"P{i+1} = {{{p['x']:.4f}, {p['y']:.4f}, {p['z']:.4f}, "
          f"{p['A']:.2f}, {p['B']:.2f}, {p['C']:.2f}}}")
x
# ====== WIZUALIZACJA ======
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

phi_vals = np.linspace(0, 2*np.pi, 100)
circle_x = X + R * np.cos(phi_vals)
circle_y = Y + R * np.sin(phi_vals)
circle_z = np.zeros_like(phi_vals)


def update(frame):
    ax.cla()

    # okrąg
    ax.plot(circle_x, circle_y, circle_z, 'gray')

    # kąt na okręgu
    phi = frame * 0.05

    # punkt styku
    x0 = X + R * np.cos(phi)
    y0 = Y + R * np.sin(phi)
    z0 = 0

    # ====== LOKALNY UKŁAD ======
    tangent = np.array([-np.sin(phi), np.cos(phi), 0])   # X'
    normal = np.array([np.cos(phi), np.sin(phi), 0])     # Y'
    binormal = np.array([0, 0, 1])                       # Z'

    # macierz lokalna -> globalna
    R_frame = np.column_stack((tangent, normal, binormal))

    # # ====== WEKTOR Y2 ======
    # # bazowo: kierunek promienia (Y')
    # v_local = np.array([0, 1, 0])
    # v_base = np.array([0, 0, 1])
    #
    # # najpierw Twoja rotacja (stała)
    # v_rotated = R_local @ v_local
    #
    # # potem transformacja do świata
    # v_global = R_frame @ v_rotated
    # ====== WEKTOR Y2 ======
    v_base = np.array([0, 0, 1])  # <-- KLUCZOWA ZMIANA

    v_rotated = R_local @ v_base
    v_global = R_frame @ v_rotated

    # rysowanie linii
    line_len = R * 0.5
    t = np.linspace(-line_len, line_len, 20)
    x_line = x0 + v_global[0] * t
    y_line = y0 + v_global[1] * t
    z_line = z0 + v_global[2] * t

    ax.plot(x_line, y_line, z_line, 'r', linewidth=2)
    ax.scatter(x0, y0, z0, color='blue')

    # osie
    margin = R * 1.5
    ax.set_xlim([X - margin, X + margin])
    ax.set_ylim([Y - margin, Y + margin])
    ax.set_zlim([-margin, margin])
    ax.set_box_aspect([1, 1, 1])

    ax.set_title(f"A={A_deg}°, B={B_deg}°, C={C_deg}°")

    return []


ani = FuncAnimation(fig, update, frames=200, interval=50)

plt.show()