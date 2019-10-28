# EP1

Grupo:	Alexandre Ota
		Luciano Martins
		Milton J. Barbosa


Extrair os produtos da API de Produtos do Spree

docker com docker-compose

Servi�os Utilizados
        MongoDB - O MongoDB � um programa de banco de dados orientado a documentos de plataforma cruzada gratuito e de c�digo aberto. Classificado como um programa de banco de dados NoSQL, o MongoDB usa documentos semelhantes a JSON com esquemas. O MongoDB � desenvolvido pela MongoDB Inc. e � publicado sob uma combina��o da Licen�a P�blica do Lado do Servidor e da Licen�a Apache.
			Reposit�rio: https://hub.docker.com/_/mongo

		Spreecommerce - O Spree � uma solu��o completa de com�rcio eletr�nico de c�digo aberto criada com o Ruby on Rails.
			Reposit�rio: https://hub.docker.com/r/spreecommerce/spree
			Nesse processo utilizaremos a API desenvolvida para a listagem de produtos. Documenta��o encontra-se em https://guides.spreecommerce.org/api/products.html

	
Servi�o Principal:
	Foi criado na linguagem Python 3, onde tudo foi carregado dentro do docker, inclusive as bibliotecas: Flask, pymongo e requests. 

	Fluxo:
		Carregamento do docker:
			> docker-compose up			

		Aguardar carregamento dos servi�os do MongoDB e do Spree
			Para ter certeza que o Spree subiu...acesse a p�gina: o http://localhost:3000
						
		Acessar p�gina web 
			> http://localhost:5000

		Fazer carregamento de produtos da API
			Inserir um identificador e <clicar o bot�o>
			Nesse momento o programa faz uma chamada na api do Spree, via "requests", e trazemos todos os produtos listados. 
			Sele��o dos atributos: id, name e price
			Inclui o timestamp e o identificador digitado
			Inclus�o dos valores no Mongo (dentro do docker)
			Redirecionamento de pagina e apresenta��o dos dados inclu�dos.
			Voc� poder� incluir v�rias vezes, mas, n�o h� um controle do identificador.

		Sair do conteiner
			CTRL + C


N�o h� exclus�o de valores inclu�dos.


Problemas encontrados:

	De alguma forma o aplicativo spree n�o derruba ao sair....fica dando erro no servidor do �Ruby�.
	Uma forma para contornar o problema foi remover os containers (docker-compose rm) e montar de novo (docker-compose up).




