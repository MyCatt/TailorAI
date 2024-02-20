import json
import os
import time
from asyncio import run

import spacy as spacy
# spacy.cli.download("en_core_web_trf")

from auth.githubauth import GitHubAuth
from auth.openaiauth import OAIAuth
from dotenv import load_dotenv
from helpers.instancelogger import InstanceLogger

from prompts import structures


def main():
    # First, we Init an instance for logging
    logger = InstanceLogger("structure-testing")

    # Second We Authenticate
    load_dotenv()
    github = GitHubAuth(logger, os.environ.get("GithubKey"))
    openai = OAIAuth(logger, os.environ.get("OpenAIKey"))

    # Next, we give it article data
    # creating a pdf file object
    source = open("InputDir/whats-new-changed-10-0-39.md", 'rb')
    markdown_string = source.read().decode("utf-8")

    # Try a Prompt
    print("> EXTRACTING FEATURES")
    openai.change_model("gpt-4-0125-preview")
    feature_list = openai.prompt("ExtractFeatureList", markdown_string, "json_object")  # Json Object Returned
    feature_json = json.loads(feature_list)

    openai.change_model("gpt-3.5-turbo-0125")

    # raise Exception

    print("> RESEARCHING FEATURES")
    openai.change_model("gpt-4-0125-preview")
    researched = {}
    for feature in feature_json:
        print(">>", feature)
        researched[feature] = feature_json[feature]
        research = openai.raw_prompt([  # Feeding prompt() with same key results in the content being static to key1
            {"role": "user",
             "content": "In the context of Dynamics 365 Finance and the feature: " + feature +
                        ", research the feature and dump all knowledge that you can discover. Be very specific."
                        "Your response you be paragraphs not lists."
             }
        ], )
        researched[feature]['research'] = research
        summarised = openai.raw_prompt([  # Feeding prompt() with same key results in the content being static to key1
            {"role": "user",
             "content": "In the context of Dynamics 365 Finance and this feature: " + feature +
                        ", research the feature and provide an overview summary of its inclusion in the provided "
                        "software release notes - ensure you capture all important information and facts."
                        "You have been provided with these notes and also some extra "
                        "information about the feature (outside of the context of the update) to help you with "
                        "this. Highlight the core information without using positive or negative language, "
                        "building/mutating upon it's description in the original notes and ensure that the "
                        "intent is to teach users about how this feature has changed in this release (for better or "
                        "worse). You do not work for Microsoft and your writing must always be neutral and in a "
                        "academic paper like tone/writing style."
                        "These 2 documents are separated by '***'\n\n" + markdown_string +
                        "\n\n***\n\n" + research
             }
        ], )
        researched[feature]['releaseNotesSummary'] = summarised
        break  # Testing first feature to save $$$$

    print("> GENERATING SUMMARY")
    openai.change_model("gpt-3.5-turbo-0125")
    # article = openai.prompt("GenerateGlobalSummary", researched)
    #article = openai.prompt("Markdown", researched)
    output = ""
    for feature in researched.keys():
        output += feature + "\n"
        output += researched[feature]['releaseNotesSummary'] + "\n\n\n"

    logger.log_raw_data("main", "final article", output)

    # print("> GENERATING PERSONAL")
    # article = openai.prompt("GeneratePersonalSummary", summarised_feature_list)

    openai.calc_runtime_cost()


if __name__ == '__main__':
    main()
