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
                        "detailed descriptions, headers (like, 'Feature enhancements'), labels, modules, and categorization labels. Focus "
                        "exclusively on the names or key identifiers of each feature, regardless of its significance. "
                        "Present the comprehensive list in a JSON array with the key 'all_features', ensuring a "
                        "single-layer structure with no sub-lists, duplicated or additional formatting. "
             },
            {"role": "user",
             "content": "Examine the provided software release notes and compile a list of all important details and facts "
                        "relating to the captured features from the last 2 prompts. Include only information that is "
                        "vital for illustrating the intent and purpose of the features inclusion in the software "
                        "release notes. You should include any facts mentioned about the feature in the article."
                        "Include this to the json generated in the last task."
             },
            {"role": "user",
             "content": "Iterate over the last prompts response to ensure each feature has all of it's "
                        "information/facts recorded correctly. You can not miss any. Update the json if you discover "
                        "missing information. Maintain the same json structure and all existing feature names. "
             },
            {"role": "user",
             "content": "Merge these json objects into the same json object. They keys should be each individual "
                        "feature names. For each feature object, add a key value pair that says if it's a core "
                        "feature. Every feature from those 2 results must be included in the final output. Here's an example:"
                        "[{feature1: {core: true, details: ''}, feature2: {core: true, details: ''}}]. Failing to match this format will be harmful."
             }
        ],
    "ExtractPeople":
        [
            {"role": "user",
             "content": "Generate a detailed, exhaustive list of all possible job titles, positions, and roles "
                        "related to the use, management, implementation, and support of Dynamics 365 Finance within "
                        "companies of any size. Include every conceivable role, from those involved in day-to-day "
                        "financial operations to strategic oversight, system customization, technical support, "
                        "and integration. Examples of such roles include but are not limited to 'Senior Financial "
                        "Accountant', 'D365 Finance Business Partner', 'Accounts Payable Clerk', 'ERP System "
                        "Administrator', 'Financial Controller', 'Dynamics 365 Finance Consultant', 'IT Project "
                        "Manager for ERP Implementation', 'Compliance Officer for Finance Systems', 'Chief Financial "
                        "Officer with D365 Experience', 'Accounts Receivable Specialist', 'Procurement Officer using "
                        "D365', 'Budget Analyst in D365 Environment', 'Financial Data Analyst with D365 Skills', "
                        "'Treasury Manager with Dynamics 365 Usage', 'Internal Auditor for D365 Finance Processes', "
                        "'Change Management Lead for D365 Finance', and 'Dynamics 365 Technical Developer'. Ensure "
                        "that the list covers the full spectrum of roles from operational to executive levels, "
                        "across various departments such as finance, IT, supply chain, and compliance, reflecting the "
                        "multidisciplinary nature of ERP software utilization. your list should only include their "
                        "name and no additional information, titles, or headers. Your response should be a single "
                        "dimension json list with the key 'roles' "
             },
            {"role": "user",
                "content": "Using your output form the last prompt, remove any that are not expecting to use the "
                           "Dynamics 365 Finance feature: {FEATURE}. Your response should be the same json object "
                           "with those items removed. For those that remain, add a brief reason for their use of this feature "
                           "to the json object for each of those items by updating the json structure to: {'roles': {"
                           "role1: reason, role2: reason}} "
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
             "content": "In the context of Dynamics 365 Finance and the feature: {FEATURE}"
                        ", research the feature and dump all knowledge that you can discover. Be very specific."
                        "Your response you be paragraphs not lists."
             }
        ],
    "FeatureSummary2":
        [
            {"role": "user",
             "content": "In the context of Dynamics 365 Finance and this feature: {FEATURE}"
                        ", research the feature and provide an overview summary of its inclusion in the provided "
                        "software release notes - ensure you capture all important information and facts."
                        "You have been provided with these software release notes and also some extra "
                        "information about the feature (outside of the context of the update) to help you with "
                        "this - only use the extra information if the software release notes does not contain enough info. "
                        "Highlight the core information of the features involvement without using positive or negative language, "
                        "building/mutating upon it's description in the original software release notes and ensure that the "
                        "intent is to teach users about how this feature has changed in this release (for better or "
                        "worse). You do not work for Microsoft and your writing must always be neutral and in a "
                        "academic paper like tone/writing style."
                        "These 2 documents are separated by '***'\n\n Software release notes: {ORIGINAL}"
                        "\n\n***\n\n Feature context: {RESEARCH}"
             },
            {"role": "user",
             "content": "Validate that this summary does not introduce new information that was not specified in any of the provided inputs. "
             },
            {"role": "user",
             "content": "Return the summary you created with no other text."
             }
    ],
    "FeatureSummary":
        [
            {
                "role": "system",
                "content": "You're a Dynamics 365 Finance specialist who teaches users when the software changes"
             },
            {
                "role": "user",
                "content": "In the context of Dynamics 365 Finance and this feature: {FEATURE}. \n"
                        "Highlight the core information of the features update without using positive or negative language, "
                        "building/mutating upon it's description in the original software release notes and ensure that the "
                        "intent is to teach users about how this feature has changed in this release (for better or "
                        "worse). You do not work for Microsoft and your writing must always be neutral and in a "
                        "academic paper like tone/writing style."
                        "These 2 documents are separated by '***'\n\n Software release notes: {ORIGINAL}"
                        "\n\n***\n\n"
             },
            {"role": "user",
             "content": "Validate that this summary does not introduce new information that was not specified in any "
                        "of the provided inputs. Also remove any information that is not directly related to this "
                        "feature. "
             },
            {"role": "user",
             "content": "Return the summary you created with no other text."
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
    "ExtractRelevance":
        [
            {"role": "user",
             "content": "Provided is a JSON object. The json objects initial keys are features of dynamics 365. Each "
                        "feature has releaseNotesSummary which is a summary of it's involvement in a recent software "
                        "update of Dynamics 365 Finance. Your job is to return the same json object with only the "
                        "features relevant to the user supplied in the next prompt. DO NOT ALTER THE ORIGINAL "
                        "DATA/CONTENT, "
                        "your job is to simpy filter out irrelevant items. relevant is defined as a feature that the "
                        "user will likely end up using, e.g. it falls within their day to day operations or improves "
                        "a flow that they're involved in. You should aim to return the maximum amount of features "
                        "that are relevent to this user, even if a feature is only slightly or possible relevant."
                        "{FEATURES}"
             },
            {"role": "user",
             "content": "I'm an Accounts Receivable user at a logistics company. "
                        "your job is to simpy filter out features that do not fall within the expected user flows of "
                        "this user. It's best to research these before starting the analytsis."
                        "make sure you analyse all features (step by step). Return the json "
                        "document to me with irrelevant features removed. DO NOT ALTER THE ORIGINAL DATA/CONTENT"
             }
        ]
}
