from flask import Flask, render_template, request

app = Flask(__name__)


def get_grade_point(grade):
    grade_points = {
        'A++': 10,
        'A+': 9,
        'A': 8,
        'B+': 7,
        'B': 6,
        'C+': 5,
        'C': 4
    }
    return grade_points.get(grade.upper(), 0)


@app.route('/', methods=['GET', 'POST'])
def index():
    sgpa = None
    if request.method == 'POST':
        grades_subjects = [
            request.form.get('dsp'),
            request.form.get('es'),
            request.form.get('dc'),
            request.form.get('em'),
            request.form.get('dsa'),
            request.form.get('fna')
        ]

        grades_labs = [
            request.form.get('dsp_lab'),
            request.form.get('es_lab'),
            request.form.get('dc_lab'),
            request.form.get('mp_lab')
        ]

        total_credits = 22
        subject_credits = 3
        lab_credits = 1

        total_points = sum(get_grade_point(grade) * subject_credits for grade in grades_subjects)
        total_points += sum(get_grade_point(grade) * lab_credits for grade in grades_labs)

        sgpa = total_points / total_credits

    return render_template('index.html', sgpa=sgpa)


if __name__ == '__main__':
    app.run(debug=True)