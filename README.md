# NT - transparency

## Credits
 - Django Framework
 - Pillow library
 - Markdownify library
 - Jdenticon library
 - Hitcount library


## TODOs
 - create category list and page
 - count hitcount and add relevence filter in search
 - create blog as seperate timeline articles
 - create tag list and page
 - create about, contact, credits, FAQ page


## Algolia Setup
`pip install --upgrade 'algoliasearch-django>=2.0,<3.0'`

```
# settings.py

# Algolia setup
# https://www.algolia.com/doc/framework-integration/django/setup/?client=python
ALGOLIA = {
    'APPLICATION_ID': 'XUCZJ001OY',
    'API_KEY': '98fe6217a65a2120831a2958a45ddc89'
}
```

```
# index.py

import algoliasearch_django as algoliasearch

from .models import YourModel

algoliasearch.register(YourModel)
```

```
# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import YourModel

@register(YourModel)
class YourModelIndex(AlgoliaIndex):
    fields = ('name', 'date')
    geo_field = 'location'
    settings = {'searchableAttributes': ['name']}
    index_name = 'my_index'

```