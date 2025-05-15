# What is a delegator?

Delegators are this project's means of interacting with external sources. More succinctly, a delegator sends and receives data with an external source.

# How do I use a delegator?
In order to interact with the external source, a delegator must be initialized with some information. For this project, we send in a map of credentials. For simplicity's sake, I am using the "reddit" and "ssd" mappings in the `configurations.json` file found at the root directory `src/main/configurations.json`. Since the .gitignore prevents my credentials from being uploaded, you as the reader will want to modify the `configurations.json.template` for your own application and then rename it, removing the `.template` extension.

When the mappings are extracted from the JSON file and converted to a Python dictionary, some part of the dictionary is sent to the delegator's constructor. (e.g., the "reddit" mapping goes to RedditDelegator)

# What is important to know about the delegators?
Each delegator sends and retrieves data from the external source and then returns the data to the method caller as a dictionary. For the returned dictionary, the key may be specific to the application, but the value mapped to that key will be _unmodified_.
