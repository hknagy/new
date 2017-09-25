from flask import Flask, render_template, request
from distance import hamming, jaccard, levenshtein
from model import InputForm
from wtforms.validators import ValidationError    
app = Flask(__name__)

@app.route('/calculator', methods=['GET', 'POST'])
def create_app():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        metrics = form.metrics.data
        str1 = form.str1.data
        str2 = form.str2.data
        form.validate_length(str1, str2, metrics)
        if metrics == 'hamming':
           result = hamming(str1, str2)
        elif metrics == 'jaccard':
            result = jaccard(str1, str2)
        elif metrics == 'levenshtein':
            result = levenshtein(str1, str2)
    else:
        result = None
    return render_template("view.html", form=form, result=result)


if __name__ == '__main__':
    app.run(debug=False)
