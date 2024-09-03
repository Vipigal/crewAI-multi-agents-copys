import os
from agents.copywriter import copywriter

# from utils.helper_functions import process_and_format_result

from crewai import Crew, Process

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini-2024-07-18"

# Inputs do usuário ou de algum fluxo de dados
dados_cliente = {
    "nome_loja": "Vorr",
    "segmento": "Loja de moda feminina e masculina. A Vorr une a energia do esporte à criatividade da moda, uma marca autêntica que oferece conforto com estilo.",
    "publico_alvo": "Jovens adultos masculinos e femininos, na faixa dos 18 aos 35 anos.",
    "tom_de_voz": "amigável",
    "objetivo_campanha": "Envio de giftback para todos os clientes que possuem giftback ativo que expira em 30 dias.",
    "tipo_campanha": "Giftback",
}

[
    manager,
    copywriter_data_sazonal,
    copywriter_lancamento_produto,
    copywriter_lancamento_colecao,
    analista_publico_alvo,
    copywriter_giftback,
], [copywriter_task] = copywriter()

crew = Crew(
    agents=[
        copywriter_data_sazonal,
        copywriter_lancamento_produto,
        copywriter_lancamento_colecao,
        analista_publico_alvo,
        copywriter_giftback,
    ],
    tasks=[copywriter_task],
    process=Process.hierarchical,
    manager_agent=manager,
    planning=True,
    verbose=True,
)

resultado_final = crew.kickoff(inputs=dados_cliente)

print(resultado_final)

"""
formatted_result = process_and_format_result(resultado_final, dados_cliente)
print(formatted_result)
"""
