class Config:
    def __init__(self, env):
        self.base_url = {
            'qa': 'https://jlbookstore.qa.com',
            'uat': 'https://jlbookstore.uat.com'
        }[env]

        self.app_port = {
            'qa': '8080',
            'uat': '8080'
        }[env]