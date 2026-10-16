
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        try:
            math = int(request.form.get("math", ""))
            phy = int(request.form.get("phy", ""))
            chem = int(request.form.get("chem", ""))

            if not name:
                error = "Please enter the student name."
            elif any(mark < 0 or mark > 100 for mark in [math, phy, chem]):
                error = "Marks must be between 0 and 100."
            else:
                total = math + phy + chem
                average = total / 3

                if min(math, phy, chem) < 35:
                    grade = "Fail"
                    status = "Fail"
                elif average >= 75:
                    grade = "Distinction"
                    status = "Pass"
                elif average >= 60:
                    grade = "First Class"
                    status = "Pass"
                else:
                    grade = "Pass"
                    status = "Pass"

                result = {
                    "name": name,
                    "total": total,
                    "average": round(average, 2),
                    "grade": grade,
                    "status": status
                }

        except ValueError:
            error = "Please enter valid whole-number marks."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
