import requests
import logging

class Rest(object):
    """This class offers the flexibility to use the rest methods."""
    
    def get(self, url, **kwargs):
        """
        Helps to retrieve the entities
         Args:
            url(str):- API url which performs the get operation
            kwargs(dict) : - Info which is required to retrive the information from server.
         returns:-
           Response
        """
        try:
            logging.Info(f"Making the get request with {url} with the provided data {kwargs}")
            request = requests.get(url=url)
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'Unexpected error occurred: {err}')
        pass
    
    def patch(self, url, **kwargs):
        """Helps to patch the entities"""
        pass

    def post(self, url, **kwargs):
        """
        Helps to send the entities to server
        Args:
            url(str):- API url which performs the post operation
            kwargs(dict) : - Info which needs to be sent to the server.
        returns:-
           Response
        """
        headers = {'content-type': 'application/json'}
        try:
          logging.Info(f"Making the post request with {url} with the provided data {kwargs}")
          request = requests.post(url=url, headers=headers, data=kwargs)
          if request.text is not u'':
            return request.json()
          else:
            
        return request.text
          return request.response()
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'Unexpected error occurred: {err}')  

    def put(self, url, **kwargs):
         """
         Helps to update the entities in server
         Args:
            url(str):- API url which performs the update operation
            kwargs(dict) : - Info which is required to update the entities.
         returns:-
           Response
         """
        headers = {'content-type': 'application/json'}
        try:
          logging.Info(f"Making the put request with {url} with the provided data {kwargs}")
          request = requests.put(url=url)
        except HTTPError as http_err:
            logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            logging.error(f'Unexpected error occurred: {err}')
    
    def delete(self, url, **kwargs):
         """
         Helps to update the entities in server
         Args:
            url(str):- API url which performs the delete operation
            kwargs(dict) : - Info which is required to delete the entities.
         returns:-
           Response
         """
        try:
           logging.Info(f"Making the delete request with {url} with the provided data {kwargs}")
           request = requests.delete(url=url)
        except HTTPError as http_err:
           logging.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
           logging.error(f'Unexpected error occurred: {err}')  


   

rest = Rest()

