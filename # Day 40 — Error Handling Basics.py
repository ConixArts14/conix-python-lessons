def safe_average(scores):
    try:
        average = sum(scores) / len(scores)
        return {"Average": average}
    except ZeroDivisionError:
        return {"Error": "No scores provided"}

# Test
print(safe_average([85, 90, 78, 88]))   # normal case
print(safe_average([]))                 # error case

def safe_average(scores):
    try:
        average = sum(scores) / len(scores)
        return {"Average": average}
    except ZeroDivisionError:
        return {"Error": "No scores provided"}
    except TypeError:
        return {"Error": "Scores must be numbers"}

# Test
print(safe_average([85, 90, 78, 88]))   # normal case
print(safe_average([]))                 # empty list
print(safe_average([85, "A", 90]))      # invalid type

class InvalidScoreError(Exception):
    pass

def safe_average(scores):
    try:
        if not all(isinstance(s, (int, float)) for s in scores):
            raise InvalidScoreError("Scores must be numbers")
        average = sum(scores) / len(scores)
        return f"Average: {average}"
    except ZeroDivisionError:
        return "Error: No scores provided"
    except InvalidScoreError as e:
        return f"Error: {e}"

# Test
print(safe_average([85, 90, 78, 88]))   # normal case
print(safe_average([]))                 # empty list
print(safe_average([85, "A", 90]))      # custom error


class InvalidScoreError(Exception):
    pass

def safe_average(scores):
    try:
        if not scores:
            raise ZeroDivisionError
        if not all(isinstance(s, (int, float)) for s in scores):
            raise InvalidScoreError("Scores must be numbers")
        return sum(scores) / len(scores)
    except (ZeroDivisionError, InvalidScoreError):
        return None

def class_summary(database):
    valid_reports = [r for r in database if r["Average"] is not None]
    if not valid_reports:
        return {"Error": "No valid student data"}

    total_average = sum(r["Average"] for r in valid_reports) / len(valid_reports)
    honors_count = sum(1 for r in valid_reports if r["Status"] == "Honors")
    eligible_count = sum(1 for r in valid_reports if r["Status"] == "Eligible")
    probation_count = sum(1 for r in valid_reports if r["Status"] == "Probation")
    not_eligible_count = sum(1 for r in valid_reports if r["Status"] == "Not Eligible")

    return {
        "Class Average": total_average,
        "Honors Count": honors_count,
        "Eligible Count": eligible_count,
        "Probation Count": probation_count,
        "Not Eligible Count": not_eligible_count
    }

# Example usage
students = {
    "Conix": ([95, 92, 89, 96], 92),
    "Leonald": ([70, "A", 80, 72], 75),
    "Alex": ([], 70)
}

database = []
for name, (scores, attendance) in students.items():
    avg = safe_average(scores)
    if avg is None:
        status = "Not Eligible"
    elif avg >= 90 and attendance >= 90:
        status = "Honors"
    elif avg >= 75 and attendance >= 80:
        status = "Eligible"
    elif avg >= 60 and attendance < 80:
        status = "Probation"
    else:
        status = "Not Eligible"
    database.append({"Name": name, "Average": avg, "Attendance": attendance, "Status": status})

summary = class_summary(database)
print(summary)
