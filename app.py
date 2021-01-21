from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/characters')
def characters():
    return render_template("characters.html")


@app.route('/movies')
def movies():
    return render_template("movies.html")


@app.route('/MyWatchList')
def MyWatchList():
    return render_template("MyWatchList.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run()
