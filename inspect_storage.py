import django.core.files.storage as st
print(dir(st))
# Also check for functions that may retrieve storage class
# Look for 'DefaultStorage' maybe
print('\nDefaultStorage:', st.DefaultStorage)
print('default_storage alias?', st.default_storage)

# Let's inspect the DefaultStorage class
print('\nDefaultStorage source:')
import inspect
print(inspect.getsource(st.DefaultStorage))
