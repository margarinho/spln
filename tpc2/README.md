# Repetidas - Remover Linhas Repetidas de um Programa

Este script tem como objetivo remover linhas repetidas de um arquivo ou da entrada padrão. Ele permite configurar várias opções de comportamento, como manter espaços em branco, remover linhas vazias ou adicionar um `#` às linhas vazias.

## Utilização

### Sintaxe

```bash
repetidas -f arquivo* [opções]
```

### Opções

- `-s`, `--spaces`  
  Mantém os espaços em branco nas linhas.

- `-e`, `--empty`  
  Remove as linhas vazias.

- `-h`, `--hash`  
  Coloca um `#` nas linhas vazias.

- `-f`, `--file`  
  Especifica o arquivo de entrada. Caso não seja especificado, o script irá ler da entrada padrão (stdin).

## Exemplos de Uso

1. **Remover linhas repetidas com a entrada do arquivo**:

    ```bash
    python repetidas.py -f arquivo.txt
    ```

2. **Remover linhas repetidas, mantendo os espaços**:

    ```bash
    python repetidas.py  -f arquivo.txt -s
    ```

3. **Remover linhas repetidas e adicionar `#` em linhas vazias**:

    ```bash
    python repetidas.py  -f arquivo.txt -h
    ```

4. **Remover linhas repetidas, removendo linhas vazias**:

    ```bash
    python repetidas.py  -f arquivo.txt -e
    ```

## Funcionamento

1. O script começa por processar as opções fornecidas e preparar os flags que definem o comportamento desejado.
2. O arquivo especificado ou a entrada padrão é lida linha por linha.
3. As linhas repetidas são removidas, de acordo com as opções passadas.
4. Se a opção `-h` for usada, as linhas vazias são precedidas por um `#`.
5. O resultado é impresso no terminal, com as linhas únicas e, conforme as opções, espaços e linhas vazias tratados de acordo.

