Renomeador de Arquivos

Descrição

Este aplicativo Python é uma ferramenta simples para renomear arquivos de imagem em um diretório específico, utilizando uma lista de nomes fornecida pelo usuário. É útil para organizar arquivos de forma sistemática, como em situações de formaturas, onde os arquivos de imagem podem ser renomeados com os nomes dos alunos.

Como Funciona
Configuração do Diretório: O usuário deve especificar o caminho do diretório onde os arquivos de imagem estão localizados. Isso é feito na variável directory.
Lista de Nomes:

O aplicativo utiliza uma lista de nomes que serão usados para renomear os arquivos. O usuário deve personalizar essa lista conforme necessário.
Renomeação de Arquivos:

O aplicativo itera sobre a lista de nomes e tenta renomear arquivos com base em um padrão. O formato do nome original dos arquivos é esperado como:

arquivo_original_01.jpg, arquivo_original_02.jpg, etc.

Para cada nome na lista, o aplicativo verifica se o arquivo original existe. Se existir, ele tenta renomeá-lo para o novo nome especificado.
Caso o novo nome já exista, o aplicativo avisa o usuário e não realiza a renomeação. 

Se o arquivo original não for encontrado, também é informado ao usuário.

Requisitos
Python 3.x && Permissões de escrita no diretório especificado
