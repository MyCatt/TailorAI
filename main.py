import copy
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
from prompts.promptbuilder import build_prompt


def main():
    # First, we Init an instance for logging
    logger = InstanceLogger("structure-testing")

    # Second We Authenticate
    load_dotenv()
    # github = GitHubAuth(logger, os.environ.get("GithubKey"))
    openai = OAIAuth(logger, os.environ.get("OpenAIKey"))

    # Next, we give it article data
    # creating a pdf file object
    source = open("InputDir/whats-new-changed-10-0-39.md", 'rb')
    markdown_string = source.read().decode("utf-8")

    # Try a Prompt
    print("> EXTRACTING FEATURES")
    openai.change_model("gpt-4-0125-preview")
    extract_feature_list = build_prompt("ExtractFeatureList", CONTENT=markdown_string)
    feature_list = openai.prompt(extract_feature_list, "json_object")  # Json Object Returned
    feature_json = json.loads(feature_list)

    openai.change_model("gpt-3.5-turbo-0125")

    # raise Exception

    print("> RESEARCHING FEATURES")
    openai.change_model("gpt-4-0125-preview")
    researched = {}
    i = 0

    for feature in feature_json:
        print(">>", feature)

        research = ""
        researched[feature] = feature_json[feature]

        # Format the prompt
        feature_summary_prompt = build_prompt("FeatureSummary", FEATURE=feature, ORIGINAL=markdown_string, RESEARCH=research)
        # Execute Prompt
        summarised = openai.prompt(feature_summary_prompt)

        # Add to the final dict
        researched[feature]['releaseNotesSummary'] = summarised
        researched[feature]['research'] = research

        # Format the prompt
        #people_types_prompt = build_prompt("ExtractPeople", FEATURE=json.dumps(feature))

        # Execute Prompt / Not working well 20/02 , needs work.
        #people_types = openai.prompt(people_types_prompt, "json_object")
        #researched[feature]['people'] = people_types


    print("> GENERATING SUMMARY")
    openai.change_model("gpt-3.5-turbo-0125")

    output = ""
    for feature in researched.keys():
        output += feature + "\n\n"
        output += researched[feature]['releaseNotesSummary'] + "\n\n\n\n---\n\n\n"

    logger.log_raw_data("main", "final article", output)

    raise Exception()

    print("> GENERATING PERSONAL")
    # Format the prompt
    personal_summary_prompt = build_prompt("ExtractRelevance", FEATURES=json.dumps(researched))

    personal_summary = json.loads( openai.prompt(personal_summary_prompt, "json_object") )

    output = ""
    for feature in personal_summary.keys():
        output += feature + "\n\n"
        output += researched[feature]['releaseNotesSummary'] + "\n\n\n\n---\n\n\n"

    logger.log_raw_data("main", "final article", output)

    openai.calc_runtime_cost()


if __name__ == '__main__':
    main()
