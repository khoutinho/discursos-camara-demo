import json

def export_dashboard(evo, espectro, partidos, output="dashboard_data.json"):
    dashboard = {
        "evolucao_temporal": evo.to_dict("records"),
        "espectro_por_ano": espectro.to_dict("records"),
        "top_partidos": partidos.to_dict("records")
    }

    with open(output, "w", encoding="utf-8") as f:
        json.dump(dashboard, f, ensure_ascii=False, indent=2)
