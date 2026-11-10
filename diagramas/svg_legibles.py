"""Genera las imágenes estáticas del libro desde los flujos validados de Archify.

El visor interactivo conserva sus especificaciones JSON y HTML. Esta adaptación
para lectura en Quarto usa la misma paleta y rótulos más grandes.
"""

from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
COLORS = {
    "database": ("#f0eaff", "#7c3aed"),
    "backend": ("#e8f7ef", "#059669"),
    "security": ("#fff0f3", "#e11d48"),
    "external": ("#f2f4f7", "#64748b"),
    "frontend": ("#e0f7fb", "#0891b2"),
    "messagebus": ("#fff3e8", "#ea580c"),
    "cloud": ("#eaf2ff", "#2563eb"),
}
FONT = "'JetBrains Mono',Menlo,Consolas,monospace"


def header(width: int, height: int, title: str, description: str) -> list[str]:
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" lang="es" '
        'aria-labelledby="diagram-title diagram-desc">',
        f'<title id="diagram-title">{escape(title)}</title>',
        f'<desc id="diagram-desc">{escape(description)}</desc>',
        '<rect width="100%" height="100%" fill="#f8fafc"/>',
    ]


def card(x: int, y: int, w: int, h: int, kind: str, label: str,
         sublabel: str, number: int | None = None) -> list[str]:
    fill, stroke = COLORS[kind]
    title_x = x + (70 if number is not None else 22)
    title_size = 20 if number is not None else 19
    parts = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
    ]
    if number is not None:
        parts.extend([
            f'<circle cx="{x + 35}" cy="{y + h // 2}" r="18" fill="{stroke}"/>',
            f'<text x="{x + 35}" y="{y + h // 2 + 6}" text-anchor="middle" '
            f'fill="#ffffff" font-family="{FONT}" font-size="16" font-weight="700">{number}</text>',
        ])
    parts.extend([
        f'<text x="{title_x}" y="{y + 31}" fill="#0f172a" font-family="{FONT}" '
        f'font-size="{title_size}" font-weight="700">{escape(label)}</text>',
        f'<text x="{title_x}" y="{y + 58}" fill="#475569" font-family="{FONT}" '
        f'font-size="15">{escape(sublabel)}</text>',
    ])
    return parts


def arrow_vertical(x: int, y1: int, y2: int) -> list[str]:
    return [
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 7}" '
        'stroke="#64748b" stroke-width="2.5"/>',
        f'<polygon points="{x - 7},{y2 - 10} {x},{y2} {x + 7},{y2 - 10}" '
        'fill="#64748b"/>',
    ]


def render_flow(name: str) -> None:
    source = json.loads((ROOT / f"{name}.workflow.json").read_text())
    by_id = {node["id"]: node for node in source["nodes"]}
    path = [by_id[node_id] for node_id in source["mainPath"]]
    assert len(path) == 5, f"El flujo {name} debe tener cinco pasos"

    parts = header(680, 568, source["meta"]["title"],
                   "Flujo de cinco pasos para orientar el análisis.")
    for i, node in enumerate(path):
        y = 16 + i * 110
        parts += card(42, y, 596, 78, node["type"], node["label"],
                      node.get("sublabel", ""), i + 1)
        if i < len(path) - 1:
            parts += arrow_vertical(340, y + 78, y + 110)
    parts.append("</svg>")
    (ROOT / f"{name}.svg").write_text("\n".join(parts) + "\n")


def render_three_approaches() -> None:
    source = json.loads((ROOT / "tres-enfoques.workflow.json").read_text())
    nodes = {node["id"]: node for node in source["nodes"]}
    parts = header(680, 366, source["meta"]["title"],
                   "Un problema definido abre tres rutas de prevención que pueden elegirse o combinarse.")
    parts += card(190, 12, 300, 70, nodes["problema"]["type"],
                  nodes["problema"]["label"], "hecho · lugar · momento")
    parts += card(20, 150, 200, 86, nodes["situacion"]["type"],
                  nodes["situacion"]["label"], "oportunidades")
    parts += card(240, 150, 200, 86, nodes["socialprev"]["type"],
                  nodes["socialprev"]["label"], "vulneraciones")
    parts += card(460, 150, 200, 86, nodes["comunidad"]["type"],
                  nodes["comunidad"]["label"], "actores locales")
    parts += card(190, 284, 300, 70, nodes["respuesta"]["type"],
                  nodes["respuesta"]["label"], "responsable · revisión")

    # La bifurcación representa rutas alternativas o complementarias.
    parts += [
        '<line x1="340" y1="82" x2="340" y2="116" stroke="#64748b" stroke-width="2.5"/>',
        '<line x1="120" y1="116" x2="560" y2="116" stroke="#64748b" stroke-width="2.5"/>',
    ]
    for x in (120, 340, 560):
        parts += arrow_vertical(x, 116, 148)
        parts += [
            f'<line x1="{x}" y1="236" x2="{x}" y2="258" '
            'stroke="#64748b" stroke-width="2.5"/>',
        ]
    parts += [
        '<line x1="120" y1="258" x2="560" y2="258" stroke="#64748b" stroke-width="2.5"/>',
        '<line x1="340" y1="258" x2="340" y2="277" stroke="#64748b" stroke-width="2.5"/>',
        '<polygon points="333,274 340,284 347,274" fill="#64748b"/>',
        '</svg>',
    ]
    (ROOT / "tres-enfoques.svg").write_text("\n".join(parts) + "\n")


def main() -> None:
    for name in ("enfoques", "datos", "espacial", "modelamiento"):
        render_flow(name)
    render_three_approaches()


if __name__ == "__main__":
    main()
