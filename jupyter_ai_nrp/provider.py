from os import getenv

from langchain_openai import ChatOpenAI, OpenAI, OpenAIEmbeddings

from jupyter_ai import EnvAuthStrategy, Field
from jupyter_ai_magics import BaseProvider, BaseEmbeddingsProvider, Persona

class NRPProvider(BaseProvider, OpenAI):
    id = "nrp"
    name = "NRP"
    models = [
        "llama3",
    ]
    help = "Click here for more details on [NRP](https://docs.nrp.ai/userdocs/ai/llm-managed/)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="NRP_API_KEY", keyword_param="openai_api_key",
    )
    # openai_api_key = getenv("NRP_API_KEY", '')
    openai_api_base = getenv("NRP_API_BASE", 'https://llm.nrp-nautilus.io/v1')
    openai_organization = "NRP"
    persona = Persona(name="NRP", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an NRP API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class ChatNRPProvider(BaseProvider, ChatOpenAI):
    id = "nrp-chat"
    name = "NRP"
    models = [
        "llama3",
    ]
    help = "Click here for more details on [NRP](https://docs.nrp.ai/userdocs/ai/llm-managed/)"
    model_id_key = "model_name"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="NRP_API_KEY", keyword_param="openai_api_key",
    )
    openai_api_base = getenv("NRP_API_BASE", 'https://llm.nrp-nautilus.io/v1')
    openai_organization = "NRP"
    persona = Persona(name="NRP", avatar_route="api/ai/static/jupyternaut.svg")

    @classmethod
    def is_api_key_exc(cls, e: Exception):
        """
        Determine if the exception is an NRP API key error.
        """
        import openai

        if isinstance(e, openai.AuthenticationError):
            error_details = e.json_body.get("error", {})
            return error_details.get("code") == "invalid_api_key"
        return False


class NRPEmbeddingsProvider(BaseEmbeddingsProvider, OpenAIEmbeddings):
    id = "nrp-embeddings"
    name = "NRP"
    models = [
        "embed-mistral",
    ]
    help = "Click here for more details on [NRP](https://docs.nrp.ai/userdocs/ai/llm-managed/)"
    model_id_key = "model"
    model_id_label = "Model ID"
    # registry = False
    pypi_package_deps = ["langchain_openai"]
    auth_strategy =  EnvAuthStrategy(
        name="NRP_API_KEY", keyword_param="openai_api_key",
    )
    openai_api_base = getenv("NRP_API_BASE", 'https://llm.nrp-nautilus.io/v1')
    openai_organization = "NRP"
    persona = Persona(name="NRP", avatar_route="api/ai/static/jupyternaut.svg")
