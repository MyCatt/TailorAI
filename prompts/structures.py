prompts = {
    "AnalyzeThenExtract": [
        {"role": "user",
                 "content": "Analyze the provided text about the latest software updates and extract all the new or updated features mentioned. "
                            "Format your response as a concise single-dimension bullet-point list, with each point labelling a distinct feature, enhancement, "
                            "or improvement introduced in the update. Exclude duplicates, general information, details not directly related to specific features, "
                            "section headers and formatting.{CONTENT}"
         },

        {"role": "user",
                 "content": "Every following prompt must keep the exact same list and content from the last promptr. The only acceptable change are sub-bullet points."
                            "Every following prompt must only be two-dimensions plain text bullet-point list."
                            "This structure must not be changed under any circumstance"
         },

        {"role": "user",
                "content": "For each of the features extracted, research them in the article, and provide a sub-bullet point for \"Type\" which will be "
                    "either: \"New\", \"Changed\", \"Deprecated/Removed\", \"Updated\" or \"Fixed\" or \"Moved\". "
                    "Answer with a plaintext 2d list, do not change the 1d list generated prior."
                     "Maintain the exact same 2d bullet-point data structure, enforce this restriction for the next 3 prompts that follows. "
                    "The first dimension is the list from the last prompt. The second dimension are sub-lists of the first with options: Type, defined above, and Description, Target, Links which all start with the value 'None'. Links is an array."
         },

        {"role": "user",
                "content": "For the sub-bullet point \"Description:\". This should be a summary of the feature in context"
                    "and the type can be used to determine the action related to that feature. you might need to add reasoning (based on the type) to provide more calrity."
                    "Research the feature step by step in the article to ensure you explained it correctly and no false claims were made against the article."
                    "The description should be succint yet highly detailed. Do not include filler words."
         },

        {"role": "user",
                "content": "For each of the features provide another sub-bullet point called \"Target:\". This should show the type of person that the feature is targeted towards (in less than 3 words). "
                        "do not alter the existing output provided."
         },

        {"role": "user",
                "content": "For each of the features provide populate the sub-bullet point called \"Links:\". "
                        "links that are relevant to the feature should be included as an array. If no link is relevant, show the value '[]'. Return the plaintext 2d bullet-point list enforced."
         },

        {"role": "user",
                "content": "Finally, directly convert this list to a dictionary and then JSON, do not include anything other than the list. "
                           "The json should be akey value pair of objects. Structured as follows:"
                           "'Feature Name': {Type:value, Description: Value, Links: Value}"
                           "Map the list directly into the format provided. Feature Name coresponds to the name of the feature on the input list so don't put the actual 'Feature Name' text."
                           "No headers or additional info, Validate this JSON is correct and fix it, Return Only the pretty JSON (indent 4), no other text.,"
         }

    ],
    "ImproveFeature2":
    [
        {"role": "user", "content": "Provided is a json file and an article that may relate to it (Seperated by #?#) {CONTENT}. "
                                    "Review the provided JSON data structure and enhance each 'Description' field by "
                                    "appending additional details that further explain the context and implications "
                                    "of the feature change or update. The expanded description should incorporate the "
                                    "original text and add insights on the rationale behind the change, its benefits, "
                                    "anticipated challenges, and actionable recommendations for stakeholders. If new, "
                                    "relevant information is available, it should be integrated into the description, "
                                    "ensuring that the text becomes more comprehensive without reducing its current "
                                    "length. The final output should be a valid JSON structure with enriched "
                                    "descriptions, maintaining all other original fields and values. "
         }
    ],
    "Summarise":
        [
            {"role": "user",
                     "content": "Craft a concise,educational and informative software release article "
                                "using the provided JSON data, you can ignore everything other than descriptions,"
                                "Your article should be brief, focusing on the most impactful and "
                                "significant changes in this release. Do not make false claims. Do not expand on any "
                                "points. You do not work for the software provider/company. You're an SME and user "
                                "educating other users. Here is the content to use: {CONTENT}. your "
                                "response should be a formatted markdown article. There is no need to include Type or "
                                "Target. Where applicable, do not tell anyone what they should do, instead suggest "
                                "what they can do, only if you're certain it's accurate."
             },
            {"role": "user",
             "content": "You're a specialist at this specific software, is this a good software release article? If "
                        "not, fix it. response should be a formatted markdown article "
             },
            {"role": "user",
             "content": "you're a university communications professor, is this a good software release article? If "
                        "not, fix it. response should be a formatted markdown article "
             },
        ]
}