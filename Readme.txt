Little Lemon Web Application API Endpoints

To test this API via Insomnia:
1. User Registration: POST http://127.0.0.1:8000/auth/users/
2. Token Generation: POST http://127.0.0.1:8000/auth/token/login/
3. Menu Items List: GET / POST http://127.0.0.1:8000/restaurant/menu/
4. Single Menu Item: GET / PUT / DELETE http://127.0.0.1:8000/restaurant/menu/<id>
5. Bookings (Token Auth Required): GET / POST http://127.0.0.1:8000/restaurant/booking/tables/