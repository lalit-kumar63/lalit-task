 Authentication

  1. Register a new user

   * Endpoint: POST /api/auth/register/
   * Description: Creates a new user.
   * Sample Request Body:

   1     {
   2         "email": "testuser@example.com",
   3         "username": "testuser",
   4         "password": "testpassword",
   5         "first_name": "Test",
   6         "last_name": "User"
   7     }
   * Sample Response (201 Created):

   1     {
   2         "id": 1,
   3         "email": "testuser@example.com",
   4         "username": "testuser",
   5         "first_name": "Test",
   6         "last_name": "User"
   7     }

  2. Login

   * Endpoint: POST /api/auth/login/
   * Description: Authenticates a user and returns a JWT token pair (access and refresh).
   * Sample Request Body:

   1     {
   2         "email": "testuser@example.com",
   3         "password": "testpassword"
   4     }
   * Sample Response (200 OK):

   1     {
   2         "access": "your_access_token",
   3         "refresh": "your_refresh_token"
   4     }

  Feeds

  3. List all feeds

   * Endpoint: GET /api/feeds/
   * Description: Returns a list of all feeds.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     [
    2         {
    3             "id": 1,
    4             "text_content": "This is my first post!",
    5             "is_hidden": false,
    6             "author": {
    7                 "id": 1,
    8                 "email": "testuser@example.com",
    9                 "username": "testuser",
   10                 "first_name": "Test",
   11                 "last_name": "User"
   12             },
   13             "images": [
   14                 {
   15                     "id": 1,
   16                     "image_url": "http://cloudinary.com/your_image_url.jpg",
   17                     "created_at": "2025-10-13T12:00:00Z"
   18                 }
   19             ],
   20             "comments": [],
   21             "created_at": "2025-10-13T12:00:00Z",
   22             "updated_at": "2025-10-13T12:00:00Z"
   23         }
   24     ]

  4. Create a new feed

   * Endpoint: POST /api/feeds/
   * Description: Creates a new feed post.
   * Authentication: JWT authentication required.
   * Sample Request Body:

   1     {
   2         "text_content": "Just enjoying a beautiful day!"
   3     }
   * Sample Response (201 Created):

    1     {
    2         "id": 2,
    3         "text_content": "Just enjoying a beautiful day!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [],
   13         "comments": [],
   14         "created_at": "2025-10-13T12:05:00Z",
   15         "updated_at": "2025-10-13T12:05:00Z"
   16     }

  5. Retrieve a specific feed

   * Endpoint: GET /api/feeds/{id}/
   * Description: Retrieves a specific feed by its ID.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     {
    2         "id": 1,
    3         "text_content": "This is my first post!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [
   13             {
   14                 "id": 1,
   15                 "image_url": "http://cloudinary.com/your_image_url.jpg",
   16                 "created_at": "2025-10-13T12:00:00Z"
   17             }
   18         ],
   19         "comments": [],
   20         "created_at": "2025-10-13T12:00:00Z",
   21         "updated_at": "2025-10-13T12:00:00Z"
   22     }

  6. Update a feed

   * Endpoint: PUT /api/feeds/{id}/ or PATCH /api/feeds/{id}/
   * Description: Updates a feed. Only the author of the feed can update it.
   * Authentication: JWT authentication required.
   * Sample Request Body (for PATCH):

   1     {
   2         "text_content": "This is an updated post!"
   3     }
   * Sample Response (200 OK):

    1     {
    2         "id": 1,
    3         "text_content": "This is an updated post!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [],
   13         "comments": [],
   14         "created_at": "2025-10-13T12:00:00Z",
   15         "updated_at": "2025-10-13T12:10:00Z"
   16     }

  7. Delete a feed

   * Endpoint: DELETE /api/feeds/{id}/
   * Description: Deletes a feed. Only the author of the feed can delete it.
   * Authentication: JWT authentication required.
   * Sample Response: (204 No Content)

  8. Upload an image to a feed

   * Endpoint: POST /api/feeds/upload-image/
   * Description: Uploads an image and associates it with a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body (form-data):
       * image: (file) your_image.jpg
       * feed: (integer) 1
   * Sample Response (201 Created):

   1     {
   2         "id": 2,
   3         "image_url": "http://cloudinary.com/new_image_url.jpg",
   4         "created_at": "2025-10-13T12:15:00Z"
   5     }

  Comments

  9. List all comments for a feed

   * Endpoint: GET /api/comments/?feed_id={feed_id}
   * Description: Returns a list of all comments for a specific feed.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     [
    2         {
    3             "id": 1,
    4             "text_content": "Great post!",
    5             "author": {
    6                 "id": 2,
    7                 "email": "anotheruser@example.com",
    8                 "username": "anotheruser",
    9                 "first_name": "Another",
   10                 "last_name": "User"
   11             },
   12             "created_at": "2025-10-13T12:20:00Z",
   13             "updated_at": "2025-10-13T12:20:00Z"
   14         }
   15     ]

  10. Create a new comment

   * Endpoint: POST /api/comments/
   * Description: Creates a new comment on a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body:
   1     {
   2         "text_content": "I agree!",
   3         "feed": 1
   4     }
   * Sample Response (201 Created):

    1     {
    2         "id": 2,
    3         "text_content": "I agree!",
    4         "author": {
    5             "id": 1,
    6             "email": "testuser@example.com",
    7             "username": "testuser",
    8             "first_name": "Test",
    9             "last_name": "User"
   10         },
   11         "created_at": "2025-10-13T12:25:00Z",
   12         "updated_at": "2025-10-13T12:25:00Z"
   13     }

  Reports

  11. Report a feed

   * Endpoint: POST /api/reports/
   * Description: Reports a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body:
   1     {
   2         "feed": 1
   3     }
   * Sample Response (201 Created):

   1     {
   2         "id": 1,
   3         "reporter": 1,
   4         "feed": 1,
   5         "created_at": "2025-10-13T12:30:00Z"
   6     }

                                       


                                       ===========================================================================================================================



                                        Authentication

  1. Register a new user

   * Endpoint: POST /api/auth/register/
   * Description: Creates a new user.
   * Sample Request Body:

   1     {
   2         "email": "testuser@example.com",
   3         "username": "testuser",
   4         "password": "testpassword",
   5         "first_name": "Test",
   6         "last_name": "User"
   7     }
   * Sample Response (201 Created):
   1     {
   2         "id": 1,
   3         "email": "testuser@example.com",
   4         "username": "testuser",
   5         "first_name": "Test",
   6         "last_name": "User"
   7     }

  2. Login

   * Endpoint: POST /api/auth/login/
   * Description: Authenticates a user and returns a JWT token pair (access and refresh).
   * Sample Request Body:

   1     {
   2         "email": "testuser@example.com",
   3         "password": "testpassword"
   4     }
   * Sample Response (200 OK):

   1     {
   2         "access": "your_access_token",
   3         "refresh": "your_refresh_token"
   4     }

  Feeds

  3. List all feeds

   * Endpoint: GET /api/feeds/
   * Description: Returns a list of all feeds.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     [
    2         {
    3             "id": 1,
    4             "text_content": "This is my first post!",
    5             "is_hidden": false,
    6             "author": {
    7                 "id": 1,
    8                 "email": "testuser@example.com",
    9                 "username": "testuser",
   10                 "first_name": "Test",
   11                 "last_name": "User"
   12             },
   13             "images": [
   14                 {
   15                     "id": 1,
   16                     "image_url": "http://cloudinary.com/your_image_url.jpg",
   17                     "created_at": "2025-10-13T12:00:00Z"
   18                 }
   19             ],
   20             "comments": [],
   21             "created_at": "2025-10-13T12:00:00Z",
   22             "updated_at": "2025-10-13T12:00:00Z"
   23         }
   24     ]

  4. Create a new feed

   * Endpoint: POST /api/feeds/
   * Description: Creates a new feed post.
   * Authentication: JWT authentication required.
   * Sample Request Body:
   1     {
   2         "text_content": "Just enjoying a beautiful day!"
   3     }
   * Sample Response (201 Created):

    1     {
    2         "id": 2,
    3         "text_content": "Just enjoying a beautiful day!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [],
   13         "comments": [],
   14         "created_at": "2025-10-13T12:05:00Z",
   15         "updated_at": "2025-10-13T12:05:00Z"
   16     }

  5. Retrieve a specific feed

   * Endpoint: GET /api/feeds/{id}/
   * Description: Retrieves a specific feed by its ID.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     {
    2         "id": 1,
    3         "text_content": "This is my first post!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [
   13             {
   14                 "id": 1,
   15                 "image_url": "http://cloudinary.com/your_image_url.jpg",
   16                 "created_at": "2025-10-13T12:00:00Z"
   17             }
   18         ],
   19         "comments": [],
   20         "created_at": "2025-10-13T12:00:00Z",
   21         "updated_at": "2025-10-13T12:00:00Z"
   22     }

  6. Update a feed

   * Endpoint: PUT /api/feeds/{id}/ or PATCH /api/feeds/{id}/
   * Description: Updates a feed. Only the author of the feed can update it.
   * Authentication: JWT authentication required.
   * Sample Request Body (for PATCH):

   1     {
   2         "text_content": "This is an updated post!"
   3     }
   * Sample Response (200 OK):

    1     {
    2         "id": 1,
    3         "text_content": "This is an updated post!",
    4         "is_hidden": false,
    5         "author": {
    6             "id": 1,
    7             "email": "testuser@example.com",
    8             "username": "testuser",
    9             "first_name": "Test",
   10             "last_name": "User"
   11         },
   12         "images": [],
   13         "comments": [],
   14         "created_at": "2025-10-13T12:00:00Z",
   15         "updated_at": "2025-10-13T12:10:00Z"
   16     }

  7. Delete a feed

   * Endpoint: DELETE /api/feeds/{id}/
   * Description: Deletes a feed. Only the author of the feed can delete it.
   * Authentication: JWT authentication required.
   * Sample Response: (204 No Content)

  8. Upload an image to a feed

   * Endpoint: POST /api/feeds/upload-image/
   * Description: Uploads an image and associates it with a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body (form-data):
       * image: (file) your_image.jpg
       * feed: (integer) 1
   * Sample Response (201 Created):

   1     {
   2         "id": 2,
   3         "image_url": "http://cloudinary.com/new_image_url.jpg",
   4         "created_at": "2025-10-13T12:15:00Z"
   5     }

  Comments

  9. List all comments for a feed

   * Endpoint: GET /api/comments/?feed_id={feed_id}
   * Description: Returns a list of all comments for a specific feed.
   * Authentication: JWT authentication required.
   * Sample Response (200 OK):

    1     [
    2         {
    3             "id": 1,
    4             "text_content": "Great post!",
    5             "author": {
    6                 "id": 2,
    7                 "email": "anotheruser@example.com",
    8                 "username": "anotheruser",
    9                 "first_name": "Another",
   10                 "last_name": "User"
   11             },
   12             "created_at": "2025-10-13T12:20:00Z",
   13             "updated_at": "2025-10-13T12:20:00Z"
   14         }
   15     ]

  10. Create a new comment

   * Endpoint: POST /api/comments/
   * Description: Creates a new comment on a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body:
   1     {
   2         "text_content": "I agree!",
   3         "feed": 1
   4     }
   * Sample Response (201 Created):

    1     {
    2         "id": 2,
    3         "text_content": "I agree!",
    4         "author": {
    5             "id": 1,
    6             "email": "testuser@example.com",
    7             "username": "testuser",
    8             "first_name": "Test",
    9             "last_name": "User"
   10         },
   11         "created_at": "2025-10-13T12:25:00Z",
   12         "updated_at": "2025-10-13T12:25:00Z"
   13     }

  Reports

  11. Report a feed

   * Endpoint: POST /api/reports/
   * Description: Reports a feed.
   * Authentication: JWT authentication required.
   * Sample Request Body:

   1     {
   2         "feed": 1
   3     }
   * Sample Response (201 Created):

   1     {
   2         "id": 1,
   3         "reporter": 1,
   4         "feed": 1,
   5         "created_at": "2025-10-13T12:30:00Z"
   6     }


========================================================================================
This application uses JWT (JSON Web Token) for authentication. Here’s
  how you can authenticate in Postman and send a request:

  1. Obtain Authentication Credentials (Access Token)

  You first need to get an access token by sending a POST request to the
  login endpoint.

   * Endpoint: http://127.0.0.1:8000/api/login/
   * Method: POST
   * Body: raw (JSON)

  Request Body:

   1 {
   2     "username": "your_username",
   3     "password": "your_password"
   4 }

  The server will respond with an access and refresh token.

  2. Use the Access Token in Postman

  Now, to access protected endpoints (like creating a feed), you must
  include the access token in the Authorization header of your request.

   1. Go to the Authorization tab in Postman.
   2. Select Bearer Token from the Type dropdown.
   3. Paste the access token you received in the Token field on the right.

  3. Create a Feed (Sample Request)

  Here is how you can send a request to create a new feed:

   * Endpoint: http://127.0.0.1:8000/api/feeds/
   * Method: POST
   * Authorization: Make sure you have set the Bearer Token as described
     above.
   * Body: raw (JSON)

  Sample Data:

   1 {
   2     "content": "This is my first feed!"
   3 }

  The author will be automatically set to the authenticated user you
  used to log in.

