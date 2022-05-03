# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['minos', 'minos.plugins.rabbitmq']

package_data = \
{'': ['*']}

install_requires = \
['aio-pika>=7.1.0,<8.0.0',
 'minos-microservice-common',
 'minos-microservice-networks']

setup_kwargs = {
    'name': 'minos-broker-rabbitmq',
    'version': '0.7.0.dev4',
    'description': 'The rabbitmq plugin of the Minos Framework',
    'long_description': '<p align="center">\n  <a href="https://minos.run" target="_blank"><img src="https://raw.githubusercontent.com/minos-framework/.github/main/images/logo.png" alt="Minos logo"></a>\n</p>\n\n## minos-broker-rabbitmq\n\n[![PyPI Latest Release](https://img.shields.io/pypi/v/minos-broker-rabbitmq.svg)](https://pypi.org/project/minos-broker-rabbitmq/)\n[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/minos-framework/minos-python/pages%20build%20and%20deployment?label=docs)](https://minos-framework.github.io/minos-python)\n[![License](https://img.shields.io/github/license/minos-framework/minos-python.svg)](https://github.com/minos-framework/minos-python/blob/main/LICENSE)\n[![Coverage](https://codecov.io/github/minos-framework/minos-python/coverage.svg?branch=main)](https://codecov.io/gh/minos-framework/minos-python)\n[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-Ask%20a%20question-green)](https://stackoverflow.com/questions/tagged/minos)\n\n## Summary\n\nMinos is a framework which helps you create [reactive](https://www.reactivemanifesto.org/) microservices in Python. Internally, it leverages Event Sourcing, CQRS and a message driven architecture to fulfil the commitments of an asynchronous environment.\n\n## Installation\n\nInstall the dependency:\n\n```shell\npip install minos-broker-rabbitmq\n```\n\nModify `config.yml` file:\n\n```yaml\n...\ninterfaces:\n  broker:\n    port: minos.networks.BrokerPort\n    common:\n      host: localhost\n      port: 5672\n      queue:\n        records: 1000\n        retry: 2\n    publisher:\n      client: minos.plugins.rabbitmq.RabbitMQBrokerPublisher\n      queue: minos.networks.PostgreSqlBrokerPublisherQueue\n    subscriber:\n      client: minos.plugins.rabbitmq.RabbitMQBrokerSubscriber\n      queue: minos.networks.PostgreSqlBrokerSubscriberQueue\n      validator: minos.networks.PostgreSqlBrokerSubscriberDuplicateValidator\n...\n```\n\n## Documentation\n\nThe official API Reference is publicly available at the [GitHub Pages](https://minos-framework.github.io/minos-python).\n\n## Source Code\n\nThe source code of this project is hosted at the [GitHub Repository](https://github.com/minos-framework/minos-python).\n\n## Getting Help\n\nFor usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/tagged/minos).\n\n## Discussion and Development\n\nMost development discussions take place over the [GitHub Issues](https://github.com/minos-framework/minos-python/issues). In addition, a [Gitter channel](https://gitter.im/minos-framework/community) is available for development-related questions.\n\n## License\n\nThis project is distributed under the [MIT](https://raw.githubusercontent.com/minos-framework/minos-python/main/LICENSE) license.',
    'author': 'Minos Framework Devs',
    'author_email': 'hey@minos.run',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://www.minos.run/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
