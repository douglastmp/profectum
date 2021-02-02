# profectum
Profectum teste
De acordo com o meu entendimento a respeito do problema, resolvi dividir a resolução em 4 funções, sendo 3 para a primeira etapa e 1 para a segunda

# 1ª Etapa 

### Requisitar informações de todos os cards no Pipefy e retornar em 3 formatos diferentes. 

Foi criado uma função onde dado uma lista de cards, ele retorna as informações solicitadas, sendo cada função diferindo apenas no formato de retorno conforme solicitado, sendo elas: 
- retorna_lista_cards:      Recebe uma lista Id de cartões e devolve as informações em formato de lista
- retorna_dict_cards:       Recebe uma lista Id de cartões e devolve as informações em formato de dictionary
- retorna_dataframe_cards:  Recebe uma lista Id de cartões e devolve as informações em formato de dataframe

Ponto de melhoria: Caso fosse informado o Id do container (não encontrei essa informação no descritivo) seria possível passar para as funções todos os cards existentes ao invés de ter que fazer manualmente.

# 2ª Etapa 

### Preencher um formulário com as informações solicitadas. 
Foi criada uma função para fazer o que foi solicitado, onde a mesma recebe o id do card, extrai as informações solicitadas e envia as informações para o formulário destino: 
- retorna_dataframe_cards: Recebe um Id de cartão, extrai as informações e envia para o formulário.
