from fastapi import FastAPI

app = FastAPI()

@app.get("/developer/profile")
def get_profile():
    return {
        "name": "Full-Stack Developer",
        "day": 133,
        "editor": "Visual Studio Code",
        "status": "Active"
    }

from fastapi import FastAPI

app = FastAPI()

# Activity 1
@app.get("/developer/profile")
def get_profile():
    return {
        "name": "Full-Stack Developer",
        "day": 133,
        "editor": "Visual Studio Code",
        "status": "Active"
    }

# Activity 2
@app.get("/developer/custom")
def get_custom_profile(name: str = "Developer", role: str = "Full-Stack"):
    return {
        "user": name,
        "role": role,
        "status": "Active"
    }
# Activity 3
@app.get("/developer/day/{day_number}")
def get_day_info(day_number: int):
    return {
        "day": day_number,
        "topic": "FastAPI & Building REST APIs",
        "completed": day_number <= 133,
        "message": f"Bạn đang xem thông tin học tập của ngày {day_number}"
    }