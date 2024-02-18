from github import Github


class GitHubAuth:
    def __init__(self, logger, access_token):
        self.logger = logger
        self.access_token = access_token
        self.auth = Github(self.access_token)
        self.__log_session()

    def __log_session(self):
        self.logger.log_meta("GitHubAuth", "Authenticated ✅")
