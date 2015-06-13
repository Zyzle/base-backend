# Base2 Setup

settings for this module are divided into 2 files production.py and development.py
development simply imports production and overrides where necessary to switch
between the two we use `os.environ` settings

Remove the following from `settings.py` and `manage.py`

```python

os.environ.setdefault("DJANGO_SETTINGS_MODULE", <default settings>)

```

then to the virtualenv's activate script add:

```bash

export DJANGO_SETTINGS_MODULE=base.settings.development

```

and to the deactivate command in the same file

```bash

unset DJANG_SETTINGS_MODULE

```
