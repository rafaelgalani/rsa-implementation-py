# RSA - Implementação em Python - EC10

Neste repositório encontra-se uma implementação do sistema criptográfico RSA, feito em Python, utilizando somente algumas bibliotecas padrão fornecidas pela linguagem: `math`, `random`, `time` - usado na seed do random.

## Como usar

Primeiro, faça o clone/fork/baixe o repositório. Feito isso, basta executar a seguinte instrução na linha de comando:

```bash
python "./main.py"
```
Após isso, o programa irá guiar as instruções, conforme a mensagem apresentada após rodar o comando acima:

```bash
Do you want to use your own values?
1 - Yes
2 - No
3 - Quit
```

Selecionando 1, você digitará os valores. 2, o programa irá escolhê-los sozinho, e 3 sairá do programa, e assim sucessivamente nos próximos comandos.

## Especificações

O programa está usando números de 2048 bits para os valores de `p` e `q` no algoritmo RSA. Caso queira trocar esse espectro, basta alterar o valor da constante `BIT_SIZE` no arquivo `rsa.py:5`:

```python
#!/usr/bin/env python3
import primes
from utils import *

BIT_SIZE = 2048 # Valor do tamanho dos números P e Q em bits. É possível alterar este parâmetro. Basta trocar o número.
```

Foi utilizado o algoritmo de [Teste de primalidade de Miller-Rabin](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) na definição de números primos de tamanho muito grande (acima de 1000 bits). É um algoritmo probabilístico e iterativo. O número ideal de iterações é acima de 40, para chaves de 2048 bits. A explicação utilizada como referencial pode ser encontrada [aqui](https://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes).    
  
Um exemplo de como rodar o programa pode ser:
- Seleciono os valores (ou eu, ou o programa, tanto faz);
- Seleciono a opção `1 - Encrypt`;
- Digito a palavra;
- **Copio** os valores obtidos, conforme [este link](http://prntscr.com/rhi0bf);
- Seleciono a opção `1 - Encrypt`;
- **Colo** os valores obtidos, conforme [este link](http://prntscr.com/rhi0gz).  
  
Podemos ver que a palavra digitada e o resultado final têm o comportamento esperado.

## Membros
RA 082150282 - Rafael Galani  
RA 082150320 - Renan Dias