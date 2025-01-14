from g4f import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str
    class gpt_4:
        name: str = 'gpt-4'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Bing
        best_providers: list = [Provider.Bing]

 
    
class ModelUtils:
    convert: dict = {
        'gpt-4': Model.gpt_4
    }
