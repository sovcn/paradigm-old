from django import forms
from django.utils.safestring import mark_safe
from django.utils.encoding import StrAndUnicode, force_unicode

from django.forms.util import flatatt

class jQueryDateField(forms.DateInput):
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        return mark_safe(u'<input%s />' % flatatt(final_attrs))