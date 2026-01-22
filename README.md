🎟️ BookMyShow Clone

A BookMyShow-inspired web application that allows users to browse movies, view show timings, select seats, and book tickets online.
Built to practice full-stack development and real-world booking workflows.

🚀 Features

🔐 User Authentication (Login / Signup)

🎬 Browse Movies & Events

🕒 View Show Timings

💺 Seat Selection

🎟️ Ticket Booking

📱 Responsive Design

🧾 Booking History

🛠️ Admin Panel (Add Movies, Shows, Theatres) (optional)

🛠️ Tech Stack
Frontend

HTML5

CSS3 / Tailwind CSS

JavaScript

React.js

Backend

Python

Django / Django REST Framework

Database

SQLite / PostgreSQL / MySQL

Tools & Services

Git & GitHub

EmailJS / SMTP (for booking confirmation)

JWT / Session Authentication

📂 Project Structure
bookmyshow/
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── pages/
│   └── assets/
│
├── backend/
│   ├── manage.py
│   ├── bookings/
│   ├── users/
│   └── movies/
│
├── README.md
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/bookmyshow-clone.git
cd bookmyshow-clone

2️⃣ Backend Setup
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

3️⃣ Frontend Setup
cd frontend
npm install
npm start

🌐 Environment Variables

Create a .env file in backend:

SECRET_KEY=your_secret_key
DEBUG=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_email_password


🎯 Future Improvements

💳 Online Payment Gateway (Razorpay / Stripe)

📍 Location-based Theatres

⭐ Movie Ratings & Reviews

📊 Admin Analytics Dashboard

🎫 QR Code Ticket Generation

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a pull request.
