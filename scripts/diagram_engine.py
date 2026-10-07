import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Setel tipografi standar akademik
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'DejaVu Serif']

class DiagramEngine:
    """
    DiagramEngine:
    Pustaka pembuat diagram teknis beresolusi tinggi (300 DPI) untuk dokumen ilmiah.
    """
    @staticmethod
    def draw_system_architecture(layers, output_path, title="Arsitektur Sistem"):
        """
        Membuat diagram arsitektur berlapis (Multi-tier Architecture).
        layers: list of dict, misal: [{'name': 'Presentation Layer', 'components': ['Web Client', 'Mobile App']}, ...]
        """
        n_layers = len(layers)
        fig, ax = plt.subplots(figsize=(9, max(4, n_layers * 1.3)), dpi=300)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, n_layers * 2 + 1)
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontweight='bold', pad=15)

        palette = ['#e3f2fd', '#e8f5e9', '#fff3e0', '#f3e5f5', '#ede7f6']
        border_palette = ['#1565c0', '#2e7d32', '#ef6c00', '#7b1fa2', '#4527a0']

        for i, layer in enumerate(reversed(layers)):
            y = i * 2 + 0.6
            color = palette[i % len(palette)]
            border = border_palette[i % len(border_palette)]

            # Gambar layer box
            rect = patches.FancyBboxPatch((0.8, y), 8.4, 1.4, boxstyle="round,pad=0.1",
                                          facecolor=color, edgecolor=border, lw=1.8)
            ax.add_patch(rect)

            layer_name = layer.get('name', f'Layer {i+1}')
            comps = ", ".join(layer.get('components', []))
            text_str = f"{layer_name}\n({comps})" if comps else layer_name
            ax.text(5, y + 0.7, text_str, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111111')

            # Panah penghubung antar-layer
            if i < n_layers - 1:
                ax.annotate('', xy=(5, y + 1.55), xytext=(5, y + 1.95),
                            arrowprops=dict(arrowstyle='<->', color='#444444', lw=1.5))

        plt.tight_layout()
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
        return output_path

    @staticmethod
    def draw_flowchart(steps, output_path, title="Diagram Alur Proses"):
        """
        Membuat diagram alir (Flowchart) horizontal atau vertikal.
        steps: list of str, misal: ['Mulai', 'Input Data', 'Validasi', 'Simpan ke DB', 'Selesai']
        """
        n = len(steps)
        fig, ax = plt.subplots(figsize=(max(8, n * 2), 3), dpi=300)
        ax.set_xlim(-0.5, n * 2.2)
        ax.set_ylim(-1, 2)
        ax.axis('off')
        ax.set_title(title, fontsize=11, fontweight='bold', pad=10)

        for i, step in enumerate(steps):
            x = i * 2.2 + 0.5
            box = patches.FancyBboxPatch((x - 0.8, 0.2), 1.6, 0.8, boxstyle="round,pad=0.1",
                                         facecolor='#f0f4f8', edgecolor='#333333', lw=1.5)
            ax.add_patch(box)
            ax.text(x, 0.6, step, ha='center', va='center', fontsize=8.5, fontweight='bold', color='#111111')

            if i < n - 1:
                ax.annotate('', xy=(x + 1.4, 0.6), xytext=(x + 0.85, 0.6),
                            arrowprops=dict(arrowstyle='->', color='#333333', lw=1.8))

        plt.tight_layout()
        plt.savefig(output_path, bbox_inches='tight')
        plt.close()
        return output_path

if __name__ == "__main__":
    out_dir = r"d:\semester5\doc-standards\examples"
    os.makedirs(out_dir, exist_ok=True)
    f1 = DiagramEngine.draw_flowchart(['Input Query', 'Parser', 'Optimizer', 'Execution', 'Output'],
                                      os.path.join(out_dir, 'sample_flowchart.png'))
    print("Contoh flowchart berhasil dibuat:", f1)
