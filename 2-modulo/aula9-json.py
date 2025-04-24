import json

pessoa = '{"nome" : "Ruan", "linguagens" : ["PL/SQL", "Python"]}'
pessoa_dic = json.loads(pessoa)
print(pessoa_dic)
print(pessoa_dic["linguagens"])

#Convertendo dicionario para JSON
pessoa_json = json.dumps(pessoa_dic)
print(pessoa_json)
print(type(pessoa_dic))
print(type(pessoa_json))

#Formatando JSON
print(json.dumps(pessoa_dic, indent=4, sort_keys=True))

#Salvando JSON em TXT
with open("pessoa.txt", "w") as json_file:
    json.dump(pessoa_json, json_file)
    