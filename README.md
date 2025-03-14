# **Calculadora em Python com Interface Gráfica**

Este projeto é uma **calculadora simples** desenvolvida em **Python** usando a biblioteca **CustomTkinter** para a interface gráfica. A calculadora permite realizar operações matemáticas básicas, como soma, subtração, multiplicação, divisão e porcentagem. Além disso, a interface suporta interação tanto por clique nos botões quanto por teclas do teclado.

## **Requisitos**
Este projeto foi desenvolvido em **Python** e requer algumas dependências para funcionar corretamente. Certifique-se de que sua versão do Python seja compatível com o código utilizado.

- Python 3.13 ou superior.
- **Bibliotecas necessárias**:  
  - **customtkinter**: Para criar interfaces gráficas com aparência moderna.

### **Instalação de dependências (se necessário):**
Instale as dependências executando o seguinte comando:
```bash
pip install -r requirements.txt
```

**Obs:** Certifique-se de ter a biblioteca **customtkinter** instalada.

## **Estrutura dos Arquivos**
1. **Script Principal (`calculadora.py`)**:  
   Arquivo responsável por iniciar a interface gráfica da calculadora. Contém a lógica de exibição dos botões e a interação com o usuário para realizar os cálculos.

## **Como Executar**
1. **Rodando a Calculadora**:  
   Para rodar o aplicativo, execute o comando abaixo:
   ```bash
   python calculadora.py
   ```
   Isso abrirá a interface gráfica da calculadora.

2. **Tela da Calculadora**:  
   Ao iniciar o aplicativo, você verá uma interface com botões para números e operações matemáticas. Você pode interagir com a calculadora de duas formas:
   - **Clique nos botões** para realizar as operações.
   - **Utilize o teclado** para inserir números e operadores (por exemplo, use `+`, `-`, `*`, `/` para realizar operações e `Enter` para calcular).

3. **Operações Disponíveis**:  
   As operações básicas disponíveis são:
   - **Soma (+)**
   - **Subtração (-)**
   - **Multiplicação (*)**
   - **Divisão (/)**
   - **Porcentagem (%)**

4. **Teclas de Ação**:
   - **C**: Limpa a tela da calculadora.
   - **⌫**: Apaga o último caractere inserido.
   - **Enter**: Realiza o cálculo da expressão inserida.

## **Fluxo de Funcionamento**
1. **Inserção de Números**: O usuário pode clicar nos botões de números ou digitar diretamente no teclado.
2. **Operações Matemáticas**: O usuário pode clicar nos botões de operações para adicionar, subtrair, multiplicar ou dividir.
3. **Cálculo**: Quando o usuário clicar em `=`, o cálculo é realizado e o resultado é mostrado na tela.
4. **Limpar e Apagar**: O botão `C` limpa completamente a tela, enquanto o botão `⌫` apaga o último caractere inserido.

## **Personalização**
Você pode personalizar a calculadora conforme suas necessidades, como:
- Alterar a interface gráfica.
- Adicionar mais operações matemáticas ou funcionalidades adicionais.
- Ajustar o tema para outras preferências (como claro ou escuro).

Para personalizar, basta modificar o arquivo `calculadora.py` de acordo com sua necessidade.
