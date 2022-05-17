import snapyr

def on_error(error, items):
    print("An error occurred:", error)


snapyr.write_key = 'wBADJyEQIL00nBJRKuRHP8pQ9vAXHEkZ'
snapyr.debug = True
snapyr.on_error = on_error

def manipulate(event, context):
  formatted = {
  'user_id': event['uid'],
  'email': event['email'],
  'name': event['displayName'],
}
  return(formatted)

def hello_auth(event, context):
  formatted_data = manipulate(event, context)
  print(formatted_data)
  print('$####$##$#$#$A#$#$$$#$#$#$#$#$#$#$')
  print('a@alumni.brown.edu', {
    'email': 'a@alumni.brown.edu',
    'name': 'a O\'Neill',   
})
  snapyr.identify(event['uid'], formatted_data)
    


