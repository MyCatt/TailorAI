import json

from openai import OpenAI
import tiktoken
from prompts import structures


class OAIAuth:
    def __init__(self, logger, access_token, model="gpt-3.5-turbo-0125", embedding_model="text-embedding-3-small", token_limit=10000):
        self.logger = logger
        self.model = model
        self.embedding_model = embedding_model
        self.access_token = access_token
        self.auth = OpenAI(api_key=self.access_token)
        self.token_limit = token_limit
        self.__log_session()

    def __log_session(self):
        self.logger.log_meta("OAIAuth", "Authenticated ✅")

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
            raise Exception("[CUSTOM EXCEPTION] YOU'RE TOO POOR FOR THIS TRANSACTION. YOUR TOKEN LIMIT IS SET (OPENAIAUTH.PY) TO " + str(self.token_limit))
        return num_tokens

    def create_embedding(self, input):
        self.logger.log_raw_data("Embeddings", "Embedding Token Usage", str(self.num_tokens_from_string(input)) + "\n\n" + input)

        response = self.auth.embeddings.create(
            input=input,
            model=self.embedding_model
        )
        embedding_array = response.data[0].embedding

        self.logger.log_raw_data("Embeddings", "Embedding Vertex Array", str(embedding_array))

        return embedding_array

    def get_prompt_from_key(self, key):
        return structures.prompts[key]

    def prompt(self, prompt_key, content): #str(article)
        prompt = self.get_prompt_from_key(prompt_key)
        for i in range(len(prompt)):
            prompt[i]['content'] = prompt[i]['content'].replace("{CONTENT}", f"{content}")

        # Roughly count tokens, exception raised if limit is hit.
        self.num_tokens_from_string(str(prompt))

        response = self.auth.chat.completions.create(messages=prompt, model="gpt-3.5-turbo")
        response_message = response.choices[0].message.content

        if response_message.strip().startswith("{"):
            self.logger.log_code("OpenAI", "json", response_message)
        else:
            self.logger.log_standard("OpenAI", response_message)

        return response_message
