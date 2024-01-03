from bs4 import BeautifulSoup

def get_form_from_response(response_content):
    # Create a BeautifulSoup object from the response content
    soup = BeautifulSoup(response_content, 'html.parser')

    # Your implementation of extracting the form from the soup goes here
    # This function should return the form element
    return soup.find('form')
