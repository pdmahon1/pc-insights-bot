class ConfigurationError(Exception):
    def __init__(self, reason:str = None):
        super().__init__(f"There was an error discovered in the configurations \
                         that prevents this application from running correctly. Reason: \
                        {reason if reason is not None else "unknown"}")

    def __str__(self):
        return self.message