prompts = {
    "ExtractFeatureListOld":
        [
            {"role": "user",
                     "content": "Review the software release notes provided and list only the core names of features, "
                                "including significant updates or fixes to existing features"
                                "Exclude any introductory phrases, descriptions, statuses, and categorizations. Focus "
                                "on the concise names or terms that directly denote new or updated features, "
                                "functionalities, significant changes, or important fixes. Your response should be a single dimension"
                                "json array with the key 'core', with no sub-lists, headings or extra dimensions. "
                                "--"
                                "{CONTENT}"
             },
            {"role": "user",
             "content": "For each of the feature names extracted from the last prompt, research them in the provided "
                        "software notes to write a summary and any relevant keywords associated with that feature. "
                        "your response should be a json object of key value pairs where the key is the feature name from the last prompt. "
                        "Work through this one feature at a "
                        "time and do not include information that is not part of the software release notes I provided. "
             }
        ],
    "ExtractFeatureList":
        [
            {"role": "user",
                     "content": "Analyze the provided software release notes to extract only the names of new or "
                                "significantly updated features. Omit introductory text, detailed descriptions, "
                                "implementation statuses, and category labels. Concentrate solely on succinctly "
                                "identifying each feature or major enhancement by its name or key term. Present your "
                                "findings in a JSON array titled 'core', maintaining a flat structure without nested "
                                "lists, headings, or additional dimensions. "
                                "--"
                                "{CONTENT}"
             },
            {"role": "user",
             "content": "Examine the provided software release notes and compile a list of all mentioned features, "
                        "including minor updates, enhancements, and fixes, in addition to the core features "
                        "previously identified. Exclude any ancillary information such as introductory remarks, "
                        "detailed descriptions, headers, labels, and categorization labels. Focus exclusively on the "
                        "names or key identifiers of each feature, regardless of its significance. Present the "
                        "comprehensive list in a JSON array with the key 'all_features', ensuring a single-layer "
                        "structure with no sub-lists or additional formatting. "
             },
            {"role": "user",
             "content": "Merge these json objects into the same json object. They keys should be each indiviual "
                        "feature names. For each feature object, add a key value pair that says if it's a core "
                        "feature. Every feature from those 2 results must be included in the final output. "
             }
        ],
    "ResearchFeatures":
        [
            {"role": "user",
             "content": "Provided is a software release article and then(Seperated by '***' a set of features "
                        "extracted from that software release. For each feature (list item), give me a detailed "
                        "overview of it's involvement in this software release. Make sure your answer is factual and "
                        "avoid filler words, be straight to the point and construct dense summaries. Make sure that "
                        "all features from the provided list and returned in the output."
                        "--"
                        "{CONTENT}"
             }
        ],
    "ResearchFeature":
        [
            {"role": "user",
             "content": "{CONTENT} : Provided is a feature. In the context of Dynamics 365 Finance and the feature"
                        "provided, research the feature. Step by step, work out what the feature is, "
                        "what it does, and how it's used. Dump all knowledge that you can discover. "
             }
        ],
    "ResearchFeature3":
        [
            {"role": "user",
             "content": "Provided is a feature. In the context of Dynamics 365 Finance and the feature"
                        "provided, research the feature. Step by step, work out what the feature is, "
                        "what it does, and how it's used. Dump all knowledge that you can discover. "
                        "--"
                        "{CONTENT}"
             }
        ],
    "GenerateGlobalSummary":
        [
            {"role": "system",
             "content": "You're a Micrsoft Dynamics 365 Finance Specialist who has a large following for sharing "
                        "insightful, unbiased,"
                        "detailed information about Microsoft Dynamics 365 Finance. You do not work for Microsoft and "
                        "your writing must always be neutral and in a academic paper like tone/writing style."
             },
            {"role": "user",
             "content": "Provided is a json object of changes to software and some information about those features ("
                        "what they do). Use "
                        "these to construct the perfect software release notes overview article. "
                        "For each feature use the provided research to determine what the feature does and then "
                        "combine that with the release notes summary to provide a detailed, paragraph-form summary "
                        "about that feature. "
                        "--"
                        "{CONTENT}"
             }
        ],
    "GeneratePersonalSummary":
        [
            {"role": "system",
             "content": "You're a Micrsoft Dynamics 365 Finance Specialist who has a large following for sharing "
                        "insightful, unbiased,"
                        "detailed information about Microsoft Dynamics 365 Finance. You do not work for Microsoft."
             },
            {"role": "user",
             "content": "Summarize the provided Dynamics 365 Finance & Operations release notes , concentrating "
                        "specifically on updates and changes that impact financial management and accounting "
                        "workflows. As a Finance Manager, I am interested in understanding how these changes will "
                        "affect financial reporting, budgeting, compliance, and overall financial operations within "
                        "my organization. Exclude any information not directly related to financial management "
                        "functions. Provide a concise overview that includes new features, enhancements, "
                        "or any removed functionalities relevant to my role. Highlight any adjustments or actions I "
                        "might need to consider to adapt to these updates effectively. Only include things that are "
                        "in my control as a finance manager and that affect my day to day running."
                        "--"
                        "{CONTENT}"
             }
        ],
    "Markdown":
        [
            {"role": "user",
             "content": "Convert the following JSON file to markdown. Include all of the content in the "
                        "releaseNotesSummary seciton of each feature, do not include the 'researched' section, "
                        "do not skip "
                        "anything or add additional information. "
                        "Once complete, evaluate your markdown response and ensure that you did not miss anything. "
                        "--"
                        "{CONTENT}"
             }
        ]
}
