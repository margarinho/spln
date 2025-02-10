# TPC1 - Semana 03 a 07 fevereiro

## Enunciado

O problema dado consiste na remoção de linhas repetidas de um ficheiro ou do standard input, terminal.

## Solução

A solução passa por ler as linhas e verificar a sua singularidade, armazenando-as numa estrutura adequada. 

Uma abordagem mais automática passa pela inserção imediata das linhas num `set`. No entanto, esta aboradagem compromete a compreensão do texto, uma vez que não preserva a ordem original das linhas.

A alternativa implementada consite num processo iterarivo onde a singularidade das linhas é verificada antes de serem armazenadas num `array`.

## Funcionalidade Extra (Ficheiros)

Foi adicionada a possibilidade de filtragem por palavra-chave. Caso o utilizador forneça um segundo argumento ao executar o programa, apenas as linhas que contenham essa palavra serão apresentadas. Isto permite uma análise mais específica dos dados.

## Exemplos de utilização

Comandos
```bash
 python3 tpc1.py <caminho do ficheiro>
 python3 tpc1.py
 ```
Executa a remoção de linhas duplicadas sem filtragem.

```bash
 python3 tpc1.py <caminho do ficheiro> <palavra-chave>
 ```
Executa a remoção de duplicados e exibe apenas as linhas que contêm a palavra-chave fornecida.
