import functools
from jsonobject.properties import *

Property = JsonProperty
SchemaProperty = ObjectProperty
SchemaListProperty = ListProperty
StringListProperty = functools.partial(ListProperty, unicode)
SchemaDictProperty = DictProperty

dict_to_json = None
list_to_json = None
value_to_json = None
value_to_python = None
dict_to_python = None
list_to_python = None
convert_property = None
value_to_property = None
LazyDict = None
LazyList = None
LazySet = None
