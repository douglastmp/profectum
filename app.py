import requests
import time
import json
import pandas

headers = {
'Content-Type': 'application/json',
'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJ1c2VyIjp7ImlkIjozMDEwOTA5ODgsImVtYWlsIjoiZmJub2d1ZWlyYUBwcm9mZWN0dW0uY29tLmJyIiwiYXBwbGljYXRpb24iOjMwMDA3NjY3Mn19.kJFsaS3gYkhX4ORPfidB5bl5YJCAcbvYWecKxhHuXTWky53plE4nkCNdZc0TYee2KuPmj9fsM2fXmPBrPeVhBA'
}

url = "https://api.pipefy.com/graphql"

def buscarcard(idcard):
    query = """
        {
        "query": "{ card(id: $idcard) { id title assignees { id } comments { id } comments_count current_phase { name } done due_date fields { name value } labels { name } phases_history { phase { name } firstTimeIn lastTimeOut } url } }"
        }
    """
    query=query.replace("$idcard",idcard)
    
    try:
        r = requests.post(url,data=query.encode('utf-8'), headers=headers)
        return (r.json()) 
    except:
        r = requests.post(url,data=query.encode('utf-8'), headers=headers)
        return (r.json())
    time.sleep(2)

def retorna_lista_cards(card_list):
    try:
        result_list = []
        for card in card_list:
            card_data = buscarcard(card)
            fields = card_data['data']['card']['fields']
            value_list = [field['value'] for field in fields]
            result_list.extend(value_list)
        return result_list
    except Exception: 
        print(Exception)

def retorna_dict_cards(card_list):
    try:
        result_dict = {}
        index = 0
        for card in card_list:
            index += 1
            card_data = buscarcard(card)
            fields = card_data['data']['card']['fields']
            value_dict = {field['name']:field['value'] for field in fields}
            result_dict = {**result_dict, index: {**value_dict}}
        return result_dict
    except Exception: 
        print(Exception)

def retorna_dataframe_cards(card_list):
    try:
        result_dataframe = []
        for card in card_list:
            card_data = buscarcard(card)
            fields = card_data['data']['card']['fields']
            value_dict = {field['name']:field['value'] for field in fields}
            result_dataframe.append(value_dict)
        print(result_dataframe)
        return pandas.json_normalize(result_dataframe)
    except Exception: 
        print(Exception)

def preenche_formulario(card_id):
    try:
        card_data = buscarcard(card_id)
        url_form = 'https://docs.google.com/forms/d/e/1FAIpQLSemk-UILNlX_XfFcssD7ZJSgC_8EsUoWShxUKHB7_H7ET48mg/formResponse'
        card_fields = {field['name']:field['value'] for field in card_data['data']['card']['fields']}
        form_data = {
            'emailAddress': 'teste@gmail.com',
            'entry.223822337': card_id,
            'entry.1529460179': card_fields['Purpose'],
            'entry.1052047614': card_fields['Project name'],
            'entry.372938265': card_data['data']['card']['url'],
        }
        r = requests.post(url_form, data=form_data)
        return ('Formulário preenchido com sucesso') 
    except Exception as e:  
        print(e)

retorno_lista = retorna_lista_cards(['386750573','386750766','386750876'])
retorno_dict = retorna_dict_cards(['386750573','386750766','386750876'])
retorno_data = retorna_dataframe_cards(['386750573','386750766','386750876'])
print('1 - Retorno em lista ')
print('-------------------- ')
print(retorno_lista)
print('-------------------- ')
print('2 - Retorno em dict ')
print('-------------------- ')
print(retorno_dict)
print('-------------------- ')
print('3 - Retorno em dataframe ')
print('-------------------- ')
print(retorno_data)
print('-------------------- ')
print(preenche_formulario('386750573'))
print(preenche_formulario('386750766'))
print(preenche_formulario('386750876'))