from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
{
  "id": 1,
  "title": "Data Analyst",
  "location": "Bengluru,India",
  "salary": 'Rs. 10,00,000'
},
{
  "id": 2,
  "title": "Data Scientist",
  "location": "Delhi,India",
  "salary": 'Rs. 18,00,000'
},
{
  "id": 3,
  "title": "Software Developer",
  "location": "Mumbai,India",
  "salary": 'Rs. 30,00,000'
},
{
  "id": 4,
  "title": "Software Tester",
  "location": "Remote",
  "salary": 'Rs 20,00,000'
}
]


@app.route("/")
def hello():
  return render_template("home.html",
                         jobs=JOBS,
                        company_name="CareerPoint")


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
