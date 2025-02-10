# TPC1 - Semana 03 a 07 fevereiro

## Enunciado

O problema dado consiste na remoção de linhas repetidas de um ficheiro ou do standard input, terminal.

## Solução

A solução passa por ler as linhas e verificar a sua singularidade, armazenando-as numa estrutura adequada. 

Uma abordagem mais automática passa pela inserção imediata das linhas num `set`. No entanto, esta aboradagem compromete a compreensão do texto, uma vez que não preserva a ordem original das linhas.

A alternativa implementada consite num processo iterarivo onde a singularidade das linhas é verificada antes de serem armazenadas num `array`.

## Exemplos de utilização

Comandos
```bash
 python3 tpc1.py <caminho do ficheiro> 
 python3 tpc1.py ```



