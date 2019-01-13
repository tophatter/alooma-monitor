from api_config import api

if __name__ == '__main__':
    print "Restreaming alooma queue."
    try:
      api.start_restream()
      print "Successfully restreamed alooma queue."
    except Exception as e:
      print e
