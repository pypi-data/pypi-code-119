# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['ledger_importer']

package_data = \
{'': ['*']}

install_requires = \
['typer>=0.4.1,<0.5.0']

setup_kwargs = {
    'name': 'ledger-importer',
    'version': '0.3.0',
    'description': 'ledger_importer is a csv-to-ledger importer that can be configured in Python.',
    'long_description': '# ledger_importer [![CircleCI](https://circleci.com/gh/volnt/ledger_importer.svg?style=shield&circle-token=afb73aed03518c8658de39f5d61ec3bfdf50d57c)](https://app.circleci.com/settings/project/github/volnt/ledger_importer)\n\nledger_importer is a csv-to-[ledger](https://www.ledger-cli.org/3.0/doc/ledger3.html) importer that can be configured in Python.\n\nThe key features are:\n\n* **Customization**: Designed to fit your specific needs perfectly.\n* **Auto-completion**: The confirmation step is auto-completed.\n* **Integration**: Easy to integrate with your pipeline.\n\nledger_importer main selling point is that if you know Python, you can write complex rules to match & parse accounts / target_accounts. All other tools try to be smart about the target_account matching part but offer very little customization (regex matching is the best I\'ve seen).\n\nAnother cool feature is that if you have several bank accounts, you can concatenate their csv exports and ledger_importer will de-duplicate transactions between them. The de-duplication rule can be customized to your needs.\n\n## Installation\n\n```sh\n$ pip install ledger-importer\n```\n\n## Configure\n\nledger_importer works by using the configuration file as the entrypoint. The `ledger_importer.runner` function is the function that should be called when you want to run the program.\n\nThe `runner` function takes a Config as the first argument.\n\nA Config instance can be created by creating a new class that inherits `ledger_importer.runner`. This new class must implement the following methods:\n\n* `parse_date(self, fields: tuple) -> datetime.datetime`\n* `parse_description(self, fields: tuple) -> str`\n* `parse_amount(self, fields: tuple) -> Decimal`\n* `format_amount(self, amount: Decimal) -> str`\n* `parse_target_account(self, fields: tuple) -> str`\n* `parse_account(self, fields: tuple) -> str`\n\nThe argument `fields: tuple` will be the csv row, with each column as an element of the tuple.\n\n\nExample configuration file:\n\n```py\n#!/usr/bin/env python\nfrom __future__ import annotations\n\nimport datetime\nimport re\nfrom decimal import Decimal\n\nfrom ledger_importer import Config, runner\n\n# Custom ledger importer configuration\nclass LedgerImporterConfig(Config):\n    # Define the number of lines that needs to be skipped at the beginning of the file.\n    # This is usefull if the csv has a line with the column names for example.\n    skip_lines: int = 1\n\n    # The argument `fields` given in all parse_* methods contains a whole csv row in a tuple\n    # Each element of the tuple is a string representation of the column\n\n    def parse_date(self, fields: tuple) -> datetime.datetime:\n        return datetime.datetime.strptime(fields[0], "%m-%d-%Y")\n\n    def parse_description(self, fields: tuple) -> str:\n        return fields[2]\n\n    def parse_amount(self, fields: tuple) -> Decimal:\n        return Decimal(re.sub("[€$, ]", "", fields[3]))\n\n    def format_amount(self, amount: Decimal) -> str:\n        return f"${amount}"\n\n    def parse_target_account(self, fields: tuple) -> str:\n        if self.parse_amount(fields) > 0:\n            return "Income"\n\n        return "Expenses"\n\n    def parse_account(self, fields: tuple) -> str:\n        return "Assets:Checking"\n\n\n# The next lines are required to run ledger_importer\n# when the config file is executed.\nif __name__ == "__main__":\n    runner(LedgerImporterConfig())```\n\n## Run\n\nTo run leger_importer, run the configuration module:\n\n```sh\n$ python my_importer.py bank-statement.csv --journal-path journal.ledger\n\n|        Account         |    Date    |  Amount  |     Description     |\n| Assets:Account:Florent | 2021/07/29 | 1234.56€ | VIR LOLE FOOB A.R.L |\n\nWhich account provided this income? ([Income:Salary]/[q]uit/[s]kip)\n\n\n|        Account         |    Date    |  Amount |         Description          |\n| Assets:Account:Florent | 2021/08/02 | -11.77€ | CARD  27/07/21 SWILE XX*XXXX |\n\nTo which account did this money go? ([Expenses:Restaurant]/[q]uit/[s]kip)\n\n\n|        Account         |    Date    |   Amount  |               Description               |\n| Assets:Account:Florent | 2021/08/03 |  -784.00€ | VIR Save some € Mr.      Florent        |\n\nTo which account did this money go? ([Expenses]/[q]uit/[s]kip)\nAssets:Savings\n\n\n|        Account         |    Date    |  Amount |          Description          |\n| Assets:Account:Florent | 2021/08/03 | -58.63€ | CARD  08/03/21 PAYPAL XX*XXXX |\n\nTo which account did this money go? ([Expenses:Shopping]/[q]uit/[s]kip)\nq\n```\n\n## Usage\n\n```sh\n$ python my_importer.py --help\nUsage: my_importer.py [OPTIONS] CSV_PATH\n\nArguments:\n  CSV_PATH  Path to the bank statement to import.  [required]\n\nOptions:\n  --journal-path PATH             Path a ledger journal to write & learn\n                                  accounts from.\n  --install-completion [bash|zsh|fish|powershell|pwsh]\n                                  Install completion for the specified shell.\n  --show-completion [bash|zsh|fish|powershell|pwsh]\n                                  Show completion for the specified shell, to\n                                  copy it or customize the installation.\n  --help                          Show this message and exit.\n```\n',
    'author': 'Florent Espanet',
    'author_email': 'florent.esp@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/volnt/ledger_importer',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
