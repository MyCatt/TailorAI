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
    print("EXTRCTING FEATURES")
    feature_list = openai.prompt("AnalyzeThenExtract", content)

    raise Exception()

    print("RESEARCHING FEATURES")
    for file in os.listdir("InputDir/references/"):
        filename = os.fsdecode(file)
        print("|")
        print("|-- ", filename, sep="")
        source = open(f"InputDir/references/{filename}", 'rb')
        content = str(source.read())
        feature_list = openai.prompt("ImproveFeature2", feature_list + "\n\n#?#\n\n" + content)

    print("GENERATING SUMMARY")
    article = openai.prompt("Summarise", feature_list)

