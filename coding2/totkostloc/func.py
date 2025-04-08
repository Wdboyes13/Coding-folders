from fuzzywuzzy import process
class search:
    def __init__(self, data):
          self.data = data
    def flatten_dict(self, d, parent_key=""):
         items = {}
         for k, v in d.items():
              new_key = f"{parent_key}.{k}" if parent_key else k
              if isinstance(v, dict):
                   items.update(self.flatten_dict(v.new_key))
              else:
                   items[new_key] = v
         return items
    def fuzzysearch(self, search_term):
         flat_data = self.flatten_dict(self.data)
         best_match, score = process.extractOne(search_term, flat_data.keys())
         if score > 70:
              return f"Best Match: {best_match} -> {flat_data[best_match]}"
         else: 
              return "No close matches found"