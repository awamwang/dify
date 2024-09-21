

import weaviate

# from core.index.vector_index.weaviate_vector_index import WeaviateConfig, WeaviateVectorIndex

# client = weaviate.Client('http://127.0.0.1:8088', timeout_config=(5, 30), auth_client_secret=weaviate.auth.AuthApiKey(api_key='WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih'))
# client = weaviate.Client('http://47.108.30.79:18088', timeout_config=(5, 30), auth_client_secret=weaviate.auth.AuthApiKey(api_key='WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih'), proxies=None, trust_env=False)
# client = weaviate.Client('http://35.220.235.204:8088', timeout_config=(5, 30), auth_client_secret=weaviate.auth.AuthApiKey(api_key='WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih'), proxies=None, trust_env=False)
# client = weaviate.Client('http://34.150.7.139:8088', timeout_config=(5, 30), auth_client_secret=weaviate.auth.AuthApiKey(api_key='WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih'), proxies=None, trust_env=False)
client = weaviate.Client('https://weaviate-ws4wzvbxua-df.a.run.app', timeout_config=(5, 30), auth_client_secret=weaviate.auth.AuthApiKey(api_key='QLrYd6r3SwcAQISxuVXQyltExb8HnurL0BBA'), proxies=None, trust_env=False)
print_type = lambda obj: print(type(obj))
print_type(client.batch)
print(client)

# w = WeaviateVectorIndex(
#     dataset={},
#     config=WeaviateConfig(
#         endpoint='http://47.108.30.79:18088',
#         api_key='WVF5YThaHlkYwhGUSmCRgsX3tD5ngdN8pkih',
#         batch_size=int(100)
#     ),
#     embeddings={},
#     attributes=[]
# )
# print(w._init_client())