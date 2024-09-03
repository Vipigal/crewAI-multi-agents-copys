import yaml
from crewai import Agent, Task
from crewai_tools import PDFSearchTool

from dotenv import load_dotenv

load_dotenv()


pdf_tool = PDFSearchTool(pdf="./docs/copy_tecnicas.pdf")


# Carregar arquivo YAML
with open("config/agents.yaml", "r", encoding="utf-8") as file:
    agents_config = yaml.safe_load(file)

with open("config/tasks.yaml", "r", encoding="utf-8") as file:
    tasks_config = yaml.safe_load(file)


def copywriter():
    # Criar agentes e tarefas a partir da configuração YAML
    manager = Agent(
        role=agents_config["manager"]["role"],
        goal=agents_config["manager"]["goal"],
        backstory=agents_config["manager"]["backstory"],
        memory=agents_config["manager"]["memory"],
        verbose=agents_config["manager"]["verbose"],
        stream=agents_config["manager"]["stream"],
    )

    copywriter_data_sazonal = Agent(
        role=agents_config["copywriter_data_sazonal"]["role"],
        goal=agents_config["copywriter_data_sazonal"]["goal"],
        backstory=agents_config["copywriter_data_sazonal"]["backstory"],
        memory=agents_config["copywriter_data_sazonal"]["memory"],
        verbose=agents_config["copywriter_data_sazonal"]["verbose"],
        stream=agents_config["copywriter_data_sazonal"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_giftback = Agent(
        role=agents_config["copywriter_giftback"]["role"],
        goal=agents_config["copywriter_giftback"]["goal"],
        backstory=agents_config["copywriter_giftback"]["backstory"],
        memory=agents_config["copywriter_giftback"]["memory"],
        verbose=agents_config["copywriter_giftback"]["verbose"],
        stream=agents_config["copywriter_giftback"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_lancamento_produto = Agent(
        role=agents_config["copywriter_lancamento_produto"]["role"],
        goal=agents_config["copywriter_lancamento_produto"]["goal"],
        backstory=agents_config["copywriter_lancamento_produto"]["backstory"],
        memory=agents_config["copywriter_lancamento_produto"]["memory"],
        verbose=agents_config["copywriter_lancamento_produto"]["verbose"],
        stream=agents_config["copywriter_lancamento_produto"]["stream"],
        tools=[pdf_tool],
    )

    copywriter_lancamento_colecao = Agent(
        role=agents_config["copywriter_lancamento_colecao"]["role"],
        goal=agents_config["copywriter_lancamento_colecao"]["goal"],
        backstory=agents_config["copywriter_lancamento_colecao"]["backstory"],
        memory=agents_config["copywriter_lancamento_colecao"]["memory"],
        verbose=agents_config["copywriter_lancamento_colecao"]["verbose"],
        stream=agents_config["copywriter_lancamento_colecao"]["stream"],
        tools=[pdf_tool],
    )

    analista_publico_alvo = Agent(
        role=agents_config["analista_publico_alvo"]["role"],
        goal=agents_config["analista_publico_alvo"]["goal"],
        backstory=agents_config["analista_publico_alvo"]["backstory"],
        memory=agents_config["analista_publico_alvo"]["memory"],
        verbose=agents_config["analista_publico_alvo"]["verbose"],
        stream=agents_config["analista_publico_alvo"]["stream"],
    )

    copywriter_task = Task(
        description=tasks_config["copywriter_task"]["description"],
        expected_output=tasks_config["copywriter_task"]["expected_output"],
        human_input=True,
        verbose=True,
    )

    # lancamento_produto_task = Task(
    #     description=tasks_config["lancamento_produto_task"]["description"],
    #     expected_output=tasks_config["lancamento_produto_task"]["expected_output"],
    #     context=[copywriter_task],
    #     verbose=True,
    # )

    # data_sazonal_task = Task(
    #     description=tasks_config["data_sazonal_task"]["description"],
    #     expected_output=tasks_config["data_sazonal_task"]["expected_output"],
    #     context=[copywriter_task],
    #     verbose=True,
    # )

    # lancamento_colecao_task = Task(
    #     description=tasks_config["lancamento_colecao_task"]["description"],
    #     expected_output=tasks_config["lancamento_colecao_task"]["expected_output"],
    #     context=[copywriter_task],
    #     verbose=True,
    # )

    # analise_publico_alvo_task = Task(
    #     description=tasks_config["analise_publico_alvo_task"]["description"],
    #     expected_output=tasks_config["analise_publico_alvo_task"]["expected_output"],
    #     context=[lancamento_produto_task, lancamento_colecao_task, data_sazonal_task],
    #     verbose=True,
    # )

    return [
        manager,
        copywriter_data_sazonal,
        copywriter_lancamento_produto,
        copywriter_lancamento_colecao,
        analista_publico_alvo,
        copywriter_giftback,
    ], [
        copywriter_task,
    ]
