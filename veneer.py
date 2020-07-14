class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner

  def __repr__(self):
    return ','.join([self.artist, self.title, self.medium, str(self.year), self.owner.name])

class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self):
    self.listings = []

  def show_listings(self):
    for i in self.listings:
      print(i)

class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.location = location
    self.is_museum = is_museum

  def sell_artwork(self, artwork, price):
    if artwork.owner == self:
      l1 = Listing(artwork, price, self)
      veneer.add_listing(l1)

  def buy_artwork(self, artwork):
    if artwork.owner != self:
      for listing in veneer.listings:
        if listing.art == artwork:
          art_listing = artwork
          artwork.owner = self
          veneer.remove_listing()

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller

  def __repr__(self):
    return (self.art.title + str(self.price))

################################################################

veneer = Marketplace()
veneer.show_listings()
edytta = Client(name='Edytta Halpirt', location='LA', is_museum=False)
moma = Client(name='The MOMA', location='New York', is_museum=True)
girl_with_mandolin = Art(artist='Picasso, Pablo', 
                         title='Girl with a Mandolin (Fanny Tellier)', 
                         medium = 'oil on canvas', year=1910, owner=edytta)
edytta.sell_artwork(girl_with_mandolin, 6000000)
veneer.show_listings()
moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)
