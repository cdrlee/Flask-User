# -*- coding: utf-8 -*-

try:
    from flask_babelex import Domain

except ImportError:
    def gettext(string, **variables):
        return string % variables

    def ngettext(singular, plural, num, **variables):
        variables.setdefault('num', num)
        return (singular if num == 1 else plural) % variables

    def lazy_gettext(string, **variables):
        return gettext(string, **variables)

    class Translations(object):
        """dummy Translations class, no translation support"""

        def gettext(self, string):
            return string

        def ngettext(self, singular, plural, n):
            return singular if n == 1 else plural
else:
    from flask_user import translations

    class CustomDomain(Domain):
        def __init__(self):
            super(CustomDomain, self).__init__(translations.__path__[0], domain='flask_user')

        def get_translations_path(self, ctx):
            return super(CustomDomain, self).get_translations_path(ctx)


    domain = CustomDomain()

    gettext = domain.gettext
    ngettext = domain.ngettext
    lazy_gettext = domain.lazy_gettext
