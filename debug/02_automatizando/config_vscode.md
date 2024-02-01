## Rodando os testes no VS Code
O VS Code tem um menu exclusivo para visualizar e executar os testes, que funciona com várias linguagens. Por lá, você pode ver cada um dos testes, executar um teste individual ou um conjunto de testes em específico, ou até mesmo abrir o debugger direto em um teste.

Para integrar corretamente o pytest com o VS Code, você precisa da extensão do Python instalada. Para termos uma melhor experiência com essa feature do VS Code, vamos também fazer alguns ajustes no arquivo de configurações do próprio editor. Para isso, você pode abrir seu arquivo de configurações por meio do atalho F1 e digitar no campo que aparece: “Preferences: Open User Settings (JSON)“ (ou “Preferências: Abrir as Configurações do Usuário (JSON), se seu VS Code estiver em português). Basta pressionar a tecla enter e adicionar os seguintes pares de chave/valor no arquivo que irá aparecer:

```
{ // Chave de abertura das configurações. Apague caso vá copiar para um arquivo existente
    "python.testing.pytestEnabled": true, // Habilita o pytest
    "python.testing.pytestArgs": [ // Argumentos do pytest
        "--doctest-modules", // Procura por doctests em arquivos .py
        "-vv", // Aumenta o nível de verbosidade
    ],
} // Chave de fechamento das configurações.
```

Para rodar somente um dos testes, basta clicar no botão triangular ao lado deste teste, já para rodar todos os testes no arquivo, você deve clicar no botão triangular em cima do nome do arquivo. Da mesma forma, se você desejar rodar todos os testes do projeto, deve clicar no botão em cima do nome do projeto. Isso é muito útil em projetos complexos com vários testes, inclusive alguns que demoram muito para rodar.

É possível observar outros dois botões, sendo o segundo um triângulo com um inseto (bug), que indica que você pode abrir o debugger naquele teste (ou naquele conjunto de testes) e, por último, um ícone de arquivo, que abre o arquivo do teste já na linha do teste.

Na visão do arquivo, as opções de rodar um teste, rodar o debugger no teste ou adicionar breakpoints podem ser vistas em testes individuais ao clicar com o botão direito em cima do triângulo ao lado de cada teste no arquivo.