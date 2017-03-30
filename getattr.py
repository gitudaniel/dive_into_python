import odbchelper
import types

print odbchelper.buildConnectionString

print getattr(odbchelper, 'buildConnectionString')

object = odbchelper
method = 'buildConnectionString'

print getattr(object, method)

print type(getattr(object, method)) == types.FunctionType

print getattr(object, method).__doc__

print type(getattr(object, method))

print callable(getattr(object, method))
