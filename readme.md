## Compliance Ambiental

O sistema foi pensado para ajudar no acompanhamento da utilização da frota por meio dos dados das coletas. No código, algumas informações ficam organizadas no `METADADOS_COMPLIANCE`, como o limite da frota e os indicadores ambientais. Dessa forma, esses dados podem ser usados como referência para as decisões relacionadas ao funcionamento do sistema.

A função `calcular_eficiencia_financeira()` verifica o volume coletado e compara esse valor com a capacidade definida para a frota. Quando o volume é muito baixo, o sistema apresenta um alerta sobre o alto custo de ociosidade. Isso pode ajudar a empresa a perceber quando um veículo está sendo utilizado de forma pouco eficiente.

Essa análise também pode ajudar na Governança de TI, pois as decisões passam a ser baseadas nos dados registrados pelo sistema. Em vez de analisar somente de forma manual, os responsáveis podem utilizar as informações geradas para identificar problemas e pensar em melhorias no processo.

A parte ambiental está relacionada ao conceito de Green IT, pois uma melhor organização das coletas pode evitar viagens desnecessárias ou veículos circulando com pouco volume. Com um melhor aproveitamento da frota, existe a possibilidade de diminuir o consumo de combustível e, consequentemente, reduzir a emissão de CO₂.

No código também foram definidos os indicadores `"Reducao CO2"` e `"Economia Combustivel"`. Neste momento, eles estão registrados como indicadores que podem ser utilizados pelo projeto, mas ainda não existe um cálculo específico deles na função. Mesmo assim, eles mostram que a questão ambiental foi considerada na estrutura do sistema.

Portanto, o monitoramento desses dados pode ajudar não somente na parte financeira, mas também na organização das operações e na preocupação com o meio ambiente. A ideia é utilizar a tecnologia para encontrar formas de melhorar o aproveitamento da frota, diminuir desperdícios e contribuir para a redução dos impactos ambientais.

### Relação com o Green IT

* Volume das coletas: ajuda a verificar se a frota está sendo bem aproveitada.
* Capacidade da frota: serve como referência para comparar os volumes coletados.
* Ociosidade: ajuda a identificar situações em que o veículo pode estar sendo pouco utilizado.
* Redução de CO₂: é um indicador ambiental considerado no projeto.
* Economia de combustível: também é considerada como indicador ambiental.

Dessa forma, os dados coletados pelo sistema podem servir como apoio para melhorar as decisões da empresa e buscar uma utilização mais eficiente da frota, contribuindo também para uma operação com menor impacto ambiental.
