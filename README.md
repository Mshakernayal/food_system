# Food System

A restaurant/food ordering backend built with **FastAPI**, **SQLAlchemy**, and **Jinja2** templates.

## Features

- **Auth**: Register/login with bcrypt password hashing and JWT tokens
- **Product Catalog**: Browse products in a card grid, view details
- **Shopping Cart**: Client-side cart with quantity controls, fly animation, and dropdown summary
- **Checkout (Demand)**: Client-only button that creates a Bill with all cart items
- **Purchase History**: Client-only page showing all bills (newest first) with itemized details
- **Role-based Sidebar**: Different menu items for `client` and `business_owner` users

## User Types

| Type | Sidebar Access | Cart Action |
|---|---|---|
| `client` | Latest Purchases, The Most Famous, Recommended | Demand (checkout) |
| `business_owner` | The Most Famous, Add Product, Show Business Analytics | None |

## Tech Stack

- **Python 3.10+ / 3.13**
- **FastAPI** — web framework
- **SQLAlchemy 2.0+** — ORM
- **SQLite** — database
- **Jinja2** — server-side templates
- **bcrypt** — password hashing
- **python-jose** — JWT tokens
- **Pydantic v2** — request/response validation

## Project Structure

```
food_system/
├── app/
│   ├── main.py                  # App entry, static mounts, router includes
│   ├── config.py                # DATABASE_URL, SECRET_KEY
│   ├── database.py              # SQLAlchemy engine & session
│   ├── models/                  # SQLAlchemy models (User, Product, Bill, BillDetail)
│   ├── schemas/                 # Pydantic request/response schemas
│   ├── services/                # Business logic layer
│   ├── controllers/             # HTTP layer (validation, error handling)
│   ├── routes/                  # FastAPI route definitions
│   ├── templates/               # Jinja2 HTML templates
│   ├── utils/                   # Security helpers (bcrypt, JWT)
│   └── data/
│       ├── images/              # Product PNG images
│       └── records/t.py         # SQL seed data
├── food_system.db               # Pre-populated SQLite database
├── requirements.txt
└── .env                         # Environment configuration
```

## API Routes

| Method | Path | Description |
|---|---|---|
| GET | `/` | Auth page (login/register) |
| GET | `/home` | Product grid |
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Log in |
| GET/POST | `/products` | List / create products |
| GET | `/products/{id}` | Product detail (JSON) |
| GET | `/products/{id}/detail` | Product detail (HTML) |
| POST | `/bills` | Create bill from cart |
| GET | `/purchases/latest` | Purchase history (HTML) |

## Getting Started

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

Visit `http://localhost:8000` to access the app.

## Test Accounts

All users have the password `0000`.

| Username | Type | Email |
|---|---|---|
| nayyal | client | client@email.com |
| shaker | business_owner | bso@email.com |
