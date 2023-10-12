# In this lab we will write a module to interact with the API I created at
# http://andrewbeatty1.pythonanywhere.com/books

# Import requests library
import requests

# Define the base URL for the API
URL = "http://andrewbeatty1.pythonanywhere.com/books"

# Test to see if requests is working for you
response = requests.get("http://google.com")
print(response.status_code) # Should print 200 if successful

# Write the code to get the books from http://andrewbeatty1.pythonanywhere.com/books
response = requests.get(URL)
print(response.json()) # Should print a list of books in JSON format

# Convert that into a function and call it from inside a if __name__ == "__main__":
def readbooks():
    response = requests.get(URL)
    # we could do checking for correct response code here
    return response.json()

if __name__ == "__main__":
    print(readbooks()) # Should print the same list of books as before

# Write the function for find by id and test it (you need to write the testing code)
def readbook(id):
    geturl = URL + "/" + str(id)
    response = requests.get(geturl)
    # we could do checking for correct response code here
    return response.json()

# Testing the readbook function with id 1
print(readbook(1)) # Should print the book with id 1 in JSON format

# write the code to create and test it (you need to write your own testing code)
def createbook(book):
    response = requests.post(URL, json=book)
    # should check we have the correct status code here
    return response.json()

# Testing the createbook function with a sample book
sample_book = {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams", "price": 9.99}
print(createbook(sample_book)) # Should print the created book with an id in JSON format

# write the update function
def updatebook(id, book):
    puturl = URL + "/" + str(id)
    response = requests.put(puturl, json=book)
    return response.json()

# Testing the updatebook function with a new price for the sample book
new_price = {"price": 7.99}
print(updatebook(4, new_price)) # Assuming the sample book has id 4, should print the updated book in JSON format

# Write the delete function
def deletebook(id):
    deleteurl = URL + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# Testing the deletebook function with the sample book id
print(deletebook(4)) # Assuming the sample book has id 4, should print a message indicating success or failure in JSON format

# Write a program in another file that works out the average book price from all the books on the server
# Assuming we have saved this module as books_api.py, we can import it in another file and use its functions
import books_api

# Get all the books from the server
books = books_api.readbooks()

# Calculate the sum of all book prices
total_price = 0
for book in books:
    total_price += book["price"]

# Calculate the average price by dividing by the number of books
average_price = total_price / len(books)

# Print the average price with two decimal places
print(f"The average book price is {average_price:.2f} euros")