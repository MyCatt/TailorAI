prompts = {
    "ExtractFeatureList":
        [
            {"role": "user",
                     "content": "Review the software release notes provided and list only the core names of features, "
                                "including significant updates or fixes to existing features"
                                "Exclude any introductory phrases, descriptions, statuses, and categorizations. Focus "
                                "on the concise names or terms that directly denote new or updated features, "
                                "functionalities, significant changes, or important fixes. Your response should be a "
                                "bullet point"
                                "list, with no sub-lists or headings."
                                "--"
                                "{CONTENT}"
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
    "GenerateGlobalSummary":
        [
            {"role": "system",
             "content": "You're a Micrsoft Dynamics 365 Finance Specialist who has a large following for sharing "
                        "insightful, unbiased,"
                        "detailed information about Microsoft Dynamics 365 Finance. You do not work for Microsoft."
             },
            {"role": "user",
             "content": "Provided is a list of changes to software. Use these to construct the perfect software "
                        "release notes article."
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
             "content": "Summarize the provided Dynamics 365 Finance & Operations release notes, concentrating "
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
        ]
}
