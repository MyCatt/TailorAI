import json

from openai import OpenAI, AsyncOpenAI
import tiktoken
from prompts import structures


class OAIAuth:
    def __init__(self, logger, access_token, model="gpt-3.5-turbo-0125", embedding_model="text-embedding-3-small", token_limit=1000000000000000):
        self.logger = logger
        self.model = model
        self.embedding_model = embedding_model
        self.access_token = access_token
        self.auth = OpenAI(api_key=self.access_token)
        self.asyncAuth = AsyncOpenAI(api_key=self.access_token)
        self.token_limit = token_limit
        self.model_cost = {"gpt-3.5-turbo-0125": 0.0005, "gpt-4-0125-preview": 0.01}  # cost per 1k
        self.runtime_usage = {"gpt-3.5-turbo-0125": 0, "gpt-4-0125-preview": 0}  # Token Usage
        self.__log_session()

    def __log_session(self):
        self.logger.log_meta("OAIAuth", "Authenticated ✅")

    def change_model(self, model):
        self.model = model

    def tokenize(self, text):
        enc = tiktoken.encoding_for_model(self.model)
        tokens = enc.encode(text)
        return tokens

    def chunkenize(self, chunk_size, tokenized):
        enc = tiktoken.encoding_for_model(self.model)
        chunks = [
            tokenized[i: i + chunk_size]
            for i in range(0, len(tokenized), chunk_size)
        ]
        # Decode token chunks back to strings
        chunks = [enc.decode(chunk) for chunk in chunks]
        return chunks

    def num_tokens_from_string(self, text) -> int:
        """Returns the number of tokens in a text string."""
        num_tokens = len(self.tokenize(text))
        if num_tokens > self.token_limit:
            raise Exception("[CUSTOM EXCEPTION] YOU'RE TOO POOR FOR THIS TRANSACTION. YOUR TOKEN LIMIT IS SET ("
                            "OPENAIAUTH.PY) TO " + str(self.token_limit))
        return num_tokens

    def calc_cost(self, tokens):
        cost = (tokens / 1000) * self.model_cost[self.model]
        return cost

    def calc_runtime_cost(self):
        total_cost = self.runtime_usage
        for model in self.runtime_usage.keys():
            total_cost[model] = "$" + str((self.runtime_usage[model] / 1000) * self.model_cost[model])

        self.logger.log_standard("OpenAI", "Total Runtime Cost: " + str(total_cost))
        print("Total Runtime Cost: " + str(total_cost))

    def accrue_tokens(self, token_count):
        self.runtime_usage[self.model] = self.runtime_usage[self.model] + token_count

    def create_embedding(self, input):
        self.logger.log_raw_data("Embeddings", "Embedding Token Usage", str(self.num_tokens_from_string(input)) + "\n\n" + input)

        response = self.auth.embeddings.create(
            input=input,
            model=self.embedding_model
        )
        embedding_array = response.data[0].embedding

        self.logger.log_raw_data("Embeddings", "Embedding Vertex Array", str(embedding_array))

        return embedding_array

    def prompt(self, prompt, response_format="text"): #str(article)

        # Roughly count tokens, exception raised if limit is hit.
        self.num_tokens_from_string(str(prompt))

        if response_format == "json_object":
            prompt = [{"role": "system", "content": "Your response must be in json object format"}] + prompt

        response = self.auth.chat.completions.create(messages=prompt, model="gpt-3.5-turbo", response_format={"type": response_format})
        response_message = response.choices[0].message.content

        if response_message.strip().startswith("{"):
            self.logger.log_code("OpenAI", "json", response_message)
        else:
            self.logger.log_standard("OpenAI", response_message)

        total_tokens = response.usage.total_tokens
        self.logger.log_standard("OpenAI", "Model: " + self.model + "\nTokens Used: " + str(total_tokens) + "\n" + "Cost: $" + str(self.calc_cost(total_tokens)))
        self.accrue_tokens(total_tokens)

        return response_message

