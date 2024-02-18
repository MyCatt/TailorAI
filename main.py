import os

from auth.githubauth import GitHubAuth
from auth.openaiauth import OAIAuth
from helpers.instancelogger import InstanceLogger
from dotenv import load_dotenv

if __name__ == '__main__':
    # First, we Init an instance for logging
    logger = InstanceLogger("structure-testing")

    # Second We Authenticate
    load_dotenv()
    github = GitHubAuth(logger, os.environ.get("GithubKey"))
    openai = OAIAuth(logger, os.environ.get("OpenAIKey"))

    # Next, we give it article data
    # creating a pdf file object
    source = open("InputDir/whats-new-platform-updates-10-0-39.txt", 'rb')
    content = str(source.read())

    # Try a Prompt
    print("> EXTRACTING FEATURES")
    feature_list = openai.prompt("ExtractFeatureList", content)

    print("> RESEARCHING FEATURES")
    summarised_feature_list = openai.prompt("ResearchFeatures", content + "\n***\n" + feature_list)

    print("> GENERATING SUMMARY")
    article = openai.prompt("GenerateGlobalSummary", summarised_feature_list)

    print("> GENERATING PERSONAL")
    article = openai.prompt("GeneratePersonalSummary", summarised_feature_list)