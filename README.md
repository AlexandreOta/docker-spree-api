# EP1

Grupo:	Alexandre Ota
		Luciano Martins
		Milton J. Barbosa


Extrair os produtos da API de Produtos do Spree

docker com docker-compose

Serviços Utilizados
        MongoDB - O MongoDB é um programa de banco de dados orientado a documentos de plataforma cruzada gratuito e de código aberto. Classificado como um programa de banco de dados NoSQL, o MongoDB usa documentos semelhantes a JSON com esquemas. O MongoDB é desenvolvido pela MongoDB Inc. e é publicado sob uma combinação da Licença Pública do Lado do Servidor e da Licença Apache.
			Repositório: https://hub.docker.com/_/mongo

		Spreecommerce - O Spree é uma solução completa de comércio eletrônico de código aberto criada com o Ruby on Rails.
			Repositório: https://hub.docker.com/r/spreecommerce/spree
			Nesse processo utilizaremos a API desenvolvida para a listagem de produtos. Documentação encontra-se em https://guides.spreecommerce.org/api/products.html

	
Serviço Principal:
	Foi criado na linguagem Python 3, onde tudo foi carregado dentro do docker, inclusive as bibliotecas: Flask, pymongo e requests. 

	Fluxo:
		Carregamento do docker:
			> docker-compose up			

		Aguardar carregamento dos serviços do MongoDB e do Spree
			Para ter certeza que o Spree subiu...acesse a página: o http://localhost:3000
						
		Acessar página web 
			> http://localhost:5000

		Fazer carregamento de produtos da API
			Inserir um identificador e <clicar o botão>
			Nesse momento o programa faz uma chamada na api do Spree, via "requests", e trazemos todos os produtos listados. 
			Seleção dos atributos: id, name e price
			Inclui o timestamp e o identificador digitado
			Inclusão dos valores no Mongo (dentro do docker)
			Redirecionamento de pagina e apresentação dos dados incluídos.
			Você poderá incluir várias vezes, mas, não há um controle do identificador.

		Sair do conteiner
			CTRL + C


Não há exclusão de valores incluídos.


Problemas encontrados:

	De alguma forma o aplicativo spree não derruba ao sair....fica dando erro no servidor do “Ruby”.
	Uma forma para contornar o problema foi remover os containers (docker-compose rm) e montar de novo (docker-compose up).




