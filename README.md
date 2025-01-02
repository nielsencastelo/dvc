# Projeto Simples de Treinamento de um Modelo Linear com o DVC

Este projeto demonstra como utilizar o framework **DVC** (Data Version Control) para gerenciar dados e resultados no treinamento de um modelo de regressão linear.

## Pré-requisitos
Certifique-se de que os seguintes softwares estão instalados:
- **DVC**: [Documentação oficial](https://dvc.org/doc)
- **Git**: [Guia de instalação](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- **Python**: Versão 3.7 ou superior.

---

## Etapas do Projeto

1. **Gerar dados de entrada**: Criação de um conjunto de dados para o treinamento do modelo.
2. **Treinar o modelo**: Construção de um modelo simples de regressão linear.
3. **Gerenciar arquivos com DVC**: Controle dos arquivos de dados e dos resultados do experimento.

---

## Configuração do Ambiente

Instale as dependências e configure o Git no diretório do projeto:

```bash
pip install dvc
git init

Inicialização do DVC

Inicie o controle do projeto com o DVC:

dvc init
git add .dvc .gitignore
git commit -m "Inicializa o DVC no projeto"

Fluxo de Trabalho com o DVC
Adicionar Arquivos ao DVC

Adicione os arquivos gerenciados pelo DVC, como datasets ou modelos:

dvc add data/dataset.csv
git add data/dataset.csv.dvc
git commit -m "Adiciona o dataset ao DVC"

Rastrear Resultados de Experimentos

Após o treinamento do modelo, rastreie os arquivos de saída:

dvc add outputs/model.pkl
git add outputs/model.pkl.dvc
git commit -m "Adiciona o modelo treinado ao DVC"

Compartilhar Dados e Resultados

Sincronize os dados com um remote (como Google Drive ou S3):

dvc remote add -d storage gdrive://<link-do-seu-repositorio>
dvc push

Executar o Projeto

    Configure o ambiente e instale as dependências.
    Inicie o controle de versão com o Git e o DVC.
    Adicione e rastreie os arquivos de dados e resultados.
    Sincronize os dados para facilitar a colaboração.

Referências

    DVC - Documentação Oficial
    Git - Guia de Instalação
    Python - Documentação Oficial
```
## Arquivo principal
 Execute o arquivo dvc.ipynb