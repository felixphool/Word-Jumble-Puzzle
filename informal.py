from flask import Flask, render_template, url_for, redirect, request, session
from forms import RegisterForm, Scenario, Guess1
from maker import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '091758b379d1163b1cf3cfac'

# import random module/library
import random


def informal():
    # list of words, their meanings and related sentences
    words = ['hello', 'noob']#, 'success', 'learning']
    meanings = ['hello m', 'noob m']
    sentences = ['hello s', 'noob s']
    selected_word = random.choice(words)
    index = words.index(selected_word)
    session['formal_meanings_index'] = meanings[index]
    session['formal_sentences_index'] = sentences[index]
    return selected_word


# Function for jumbling the characters of the chosen word.
def jumble(word):
    # sample() function jumbling the characters of the word
    random_word = random.sample(word, len(word))

    # join() function join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    #    messageforP = '.'
    if request.method == 'POST':
        user1 = form.user1.data
        user2 = form.user2.data
        session['data1'] = user1  # Set values
        session['data2'] = user2  # Set value
        session['counter_user2'] = 0
        session['counter_user1'] = 0
        session.pop('CURRENTPLAYER', None)
        return redirect(url_for('displaynames'))
    return render_template('register.html', form=form)


@app.route('/displaynames', methods=['GET', 'POST'])
def displaynames():
    form = Scenario()
    user1 = session['data1']  # Set values
    user2 = session['data2']  # Set values
    if request.method == 'POST':
        return redirect(url_for('jwords'))
    return render_template('displaynames.html', form=form, user1=user1, user2=user2)


@app.route('/scenario1', methods=['GET', 'POST'])
def jwords():
    form = Guess1()
    error = ""
    meaning = ""
    sentence = ""
    user1 = session['data1']  # Set values
    user2 = session['data2']  # Set values
    message = 'Good Luck!'
    currentUser = user1

    if session.get('CURRENTPLAYER') is None:
        session['CURRENTPLAYER'] = user1
        acutal_word = informal()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word
        session['counter_user2'] = 0
        session['counter_user1'] = 0

    if request.method == 'POST':
        if session['CURRENTPLAYER'] == user1:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'congo'
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                session['counter_user1'] = session['counter_user1'] + 1
            else:
                error = 'Better Luck next time...'
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                if session['counter_user2'] == 10:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user2
            session['CURRENTPLAYER'] = user2
        elif session['CURRENTPLAYER'] == user2:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'congo'
                session['counter_user2'] = session['counter_user2'] + 1
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
            else:
                error = 'Better Luck next time...'
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                if session['counter_user2'] == 10:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user1
            session['CURRENTPLAYER'] = user1

        acutal_word = informal()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word

    return render_template("formal.html", form=form, currentUser=currentUser, x=session['picked_word'], message=message,
                           picked_word=session['picked_word'],
                           acutal_word=session['acutal_word'], score1=session['counter_user1'],
                           score2=session['counter_user2'], error=error, meaning=meaning, sentence=sentence)


@app.route('/result/<user>')
def result(user):
    return render_template("successful.html", user=user)
