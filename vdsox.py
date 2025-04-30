import numpy as np
import plotly.graph_objects as go
from matplotlib import cm

def generate_world_inside_one_3d(depth=4, shrink_factor=0.5):
    points = []
    radii = []
    colors = []

    def add_spheres(x, y, z, r, current_depth, parent_index=None):
        current_index = len(points)
        points.append((x, y, z))
        radii.append(r)
        distance = np.sqrt(x**2 + y**2 + z**2)
        colors.append(distance)  # Alternativa: colors.append(depth - current_depth)

        if current_depth > 0:
            num_children = 6
            phi = np.linspace(0, np.pi, num_children//2, endpoint=False)
            theta = np.linspace(0, 2*np.pi, num_children, endpoint=False)

            for p in phi:
                for t in theta:
                    new_x = x + np.sin(p) * np.cos(t) * r * 0.5
                    new_y = y + np.sin(p) * np.sin(t) * r * 0.5
                    new_z = z + np.cos(p) * r * 0.5
                    add_spheres(new_x, new_y, new_z, r * shrink_factor, current_depth - 1, current_index)

    add_spheres(0, 0, 0, 1, depth)
    return np.array(points), radii, colors

def generate_unit_sphere_mesh(resolution=12):
    phi = np.linspace(0, np.pi, resolution)
    theta = np.linspace(0, 2 * np.pi, resolution)
    phi, theta = np.meshgrid(phi, theta)

    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    vertices = np.stack([x.flatten(), y.flatten(), z.flatten()], axis=1)

    faces = []
    rows, cols = phi.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            a = i * cols + j
            b = a + 1
            c = a + cols
            d = c + 1
            faces.append((a, b, d))
            faces.append((a, d, c))
    return vertices, faces

# Glavna logika
points, radii, color_values = generate_world_inside_one_3d(depth=2)
unit_vertices, unit_faces = generate_unit_sphere_mesh()

# Normalizacija boja
color_values = np.array(color_values)
norm_colors = (color_values - color_values.min()) / (color_values.ptp() + 1e-9)
viridis = cm.get_cmap("viridis")
rgb_colors = [f'rgb({int(r*255)},{int(g*255)},{int(b*255)})' for r, g, b, _ in viridis(norm_colors)]

# Plotly scena
fig = go.Figure()

for (center, radius, color) in zip(points, radii, rgb_colors):
    vx = unit_vertices[:, 0] * radius + center[0]
    vy = unit_vertices[:, 1] * radius + center[1]
    vz = unit_vertices[:, 2] * radius + center[2]

    i, j, k = zip(*unit_faces)
    fig.add_trace(go.Mesh3d(
        x=vx, y=vy, z=vz,
        i=i, j=j, k=k,
        color=color,
        opacity=0.8,
        name='sfera'
    ))

fig.update_layout(
    title='Svaka sfera obojena po udaljenosti od centra',
    scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
    width=1000,
    margin=dict(r=20, l=10, b=10, t=40),
    showlegend=False
)

# Prikaz u Jupyter/Colab okruženju (ako je aktivno)
fig.show()

# ✅ Snimanje u HTML fajl za web prikaz
fig.write_html("svet_unutar_1.html")
print("✅ Fajl 'svet_unutar_1.html' je uspešno snimljen i spreman za otvaranje u pregledaču.")
