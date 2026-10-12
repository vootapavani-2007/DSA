from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware

from database import get_connection

from schemas import (
    RegisterRequest,
    UserResponse,
    LoginRequest,
    Token
)

from security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)


app = FastAPI(
    title="AI Network Intrusion Detection API",
    version="1.0.0"
)


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# ROOT
# --------------------------------------------------

@app.get("/")
def root():
    return {
        "message": "AI Network Intrusion Detection API is running"
    }


# --------------------------------------------------
# HEALTH CHECK
# --------------------------------------------------

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# DATABASE TEST
# --------------------------------------------------

@app.get("/database-test")
def database_test():

    try:
        conn = get_connection()

        if conn is None:
            raise Exception("Database connection failed")

        cursor = conn.cursor()
        cursor.execute("SELECT DATABASE()")
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "status": "success",
            "database": result[0] if result else None,
            "message": "MySQL connection successful!"
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


# --------------------------------------------------
# REGISTER
# --------------------------------------------------

@app.post("/register", response_model=UserResponse)
def register(user: RegisterRequest):

    conn = None
    cursor = None

    try:
        conn = get_connection()

        if conn is None:
            raise HTTPException(
                status_code=500,
                detail="Database connection failed"
            )

        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            "SELECT user_id FROM users WHERE username = %s",
            (user.username,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Username already exists"
            )

        cursor.execute(
            "SELECT user_id FROM users WHERE email = %s",
            (user.email,)
        )

        existing_email = cursor.fetchone()

        if existing_email:
            raise HTTPException(
                status_code=409,
                detail="Email already exists"
            )

        hashed_password = hash_password(user.password)

        cursor.execute(
            """
            INSERT INTO users
            (username, email, password_hash, role)
            VALUES (%s, %s, %s, %s)
            """,
            (
                user.username,
                user.email,
                hashed_password,
                user.role
            )
        )

        conn.commit()

        user_id = cursor.lastrowid

        return {
            "user_id": user_id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }

    except HTTPException:
        raise

    except Exception as e:
        if conn:
            conn.rollback()

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# --------------------------------------------------
# LOGIN
# --------------------------------------------------

@app.post("/login", response_model=Token)
def login(user: LoginRequest):

    conn = None
    cursor = None

    try:
        conn = get_connection()

        if conn is None:
            raise HTTPException(
                status_code=500,
                detail="Database connection failed"
            )

        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT user_id, username, email, password_hash, role
            FROM users
            WHERE username = %s
            """,
            (user.username,)
        )

        db_user = cursor.fetchone()

        if not db_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        if not verify_password(user.password, db_user["password_hash"]):
            raise HTTPException(
                status_code=401,
                detail="Invalid username or password"
            )

        access_token = create_access_token(
            {
                "sub": str(db_user["user_id"]),
                "username": db_user["username"],
                "email": db_user["email"],
                "role": db_user["role"]
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    finally:
        if cursor:
            cursor.close()

        if conn:
            conn.close()


# --------------------------------------------------
# GET CURRENT USER
# --------------------------------------------------

@app.get("/users/me", response_model=UserResponse)
def get_me(current_user=Depends(get_current_user)):

    return {
        "user_id": current_user["user_id"],
        "username": current_user["username"],
        "email": current_user["email"],
        "role": current_user["role"]
    }
