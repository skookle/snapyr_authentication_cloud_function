import snapyr

def on_error(error, items):
    print("An error occurred:", error)


snapyr.write_key = 'wBADJyEQIL00nBJRKuRHP8pQ9vAXHEkZ'
snapyr.debug = True
snapyr.on_error = on_error

snapyr.identify('a@alumni.brown.edu', {
    'email': 'a@alumni.brown.edu',
    'name': 'a O\'Neill',   
})
        
snapyr.track('bone@alumni.brown.edu', 'Hand Played', {
    'pot': 1050.00,
    'hand': 'AS,KH',
    'river': '6H,2H,2D',
    'action': 'raise',
    'amount': 50.00
})
