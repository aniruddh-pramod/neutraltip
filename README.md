# NT - transparency

## Credits
 - Django Framework
 - Pillow library
 - Markdownify library - https://django-markdownify.readthedocs.io/en/latest/
 - Jdenticon library - https://jdenticon.com/
 - Hitcount library - https://django-hitcount.readthedocs.io/en/latest/
 - Simple is better than complex - https://simpleisbetterthancomplex.com/


## TODOs
 - https://fcm-django.readthedocs.io/en/latest/
 - https://jinja.palletsprojects.com/en/3.0.x/switching/#django
 - add tags in easier way
 - create tnc, privacy policies, publish policies page
 - create blog as seperate timeline articles
 - create about, contact, credits, FAQ page
  
  Advanced TODOs:
 - previous and next articles must be of same category
 - prevent spam when registering user (use IP address)
 - add neutrality meter
  
  Optional TODOs:
 - change 'Display Profile' to 'Go Anonymous'
 - create custom contact model and functionality
 - make cards in category list, with images, description
 - create admin page


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