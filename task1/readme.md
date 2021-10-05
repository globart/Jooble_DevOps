In this task I have created a Flask app, that implements API with CRUD functionality. <br>
To use it you have to install Postman. You can download it from the official website - https://www.postman.com/. <br>
After you have downloaded it and registered an account, you have to create new HTTP Request: <br>
![](images/img1.png)
![](images/img2.png)
Then, you have to enter following url - https://9a9f-3-69-253-112.ngrok.io <br>
To get all the books, you have to perform a GET request to "/books". You will get a response in JSON format: <br>
![](images/img3.png)
To get the book by id, you have to perform a GET request to "/books/id", where "id" is id of book, you want to get: <br>
![](images/img4.png) <br>
To get last n books, you have to perform a GET request to "/books/last/n", where "n" is number, you want to get: <br>
![](images/img5.png) <br>
To add a new book, you have to perform a POST request to "/books". To provide book parameters, you have to write them in a JSON format. You will get back an id of your book, which is generated automatically: <br>
![](images/img6.png)
To change book info, you have to perform a PUT request to "/books/id", where "id" is id of book, you want to change. You will get back new book data in JSON format: <br>
![](images/img7.png)
To delete a book, you have to perform a DELETE request to "/books/id", where "id" is id of book, you want to delete. You will get back this book data in JSON format: <br>
![](images/img8.png)
