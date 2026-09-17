# LaunchLab UniFAP - Desenvolvimento Exclusivo SI
METADADOS_COMPLIANCE = {
    "limite_frota_m3": 50.0,
    "piso_ociosidade_percentual": 0.30,
    "teto_ociosidade_percentual": 0.85,    
    "indicadores_ambientais": ["Reducao CO2", "Economia Combustivel"]
}


def calcular_eficiencia_financeira(volume_final):
    limite = METADADOS_COMPLIANCE["limite_frota_m3"]
    piso_critico = limite * METADADOS_COMPLIANCE["piso_ociosidade_percentual"]
    teto_critico = limite * METADADOS_COMPLIANCE["teto_ociosidade_percentual"]

    if volume_final < piso_critico:
        return "Alerta: Alto Custo de Ociosidade Detectado"

    ocupacao = round(volume_final / limite * 100, 2)

    if volume_final > teto_critico:
        return f"Otimo Aproveitamento da Frota - Ocupacao: {ocupacao}%"

    return f"Eficiencia Economica Aceitavel - Ocupacao: {ocupacao}%"

if __name__ == "__main__":
    coletas = {
        "Cooperativa Norte": 42.0,
        "Cooperativa Leste": 8.5,
        "Cooperativa Sul": 15.0,
        "Cooperativa Oeste": 12.3
    }

    for central, volume in coletas.items():
        print(f"{central:<20} {volume:>5.1f} m3 | {calcular_eficiencia_financeira(volume)}")