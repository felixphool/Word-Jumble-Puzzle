from flask import Flask, render_template, url_for, redirect, request, session
from forms import RegisterForm, Scenario, Guess1


app = Flask(__name__)
app.config['SECRET_KEY'] = '091758b379d1163b1cf3cfac'

# import random module/library
import random


def formal():
    # list of words, their meanings and related sentences
    words1 = ['enquire', 'verify', 'utilize', 'deficiency', 'demonstrate', 'notion', 'principally', 'futile',
              'apologize', 'fabricate', 'nevertheless', 'indicate', 'consult', 'tolerate', 'concerning', 'commence',
              'prudent', 'disclose', 'evade', 'comprehend', 'avid', 'modify', 'contradict', 'establish', 'liberty']
    meanings1 = ['to ask', 'to check', 'to use', 'lack', 'show', 'idea', 'mainly', 'hopeless', 'say sorry', 'make up',
                 'anyways', 'to point out', 'refer to', 'put up', 'about', 'begin', 'wise', 'to tell', 'avoid',
                 'understand', 'eager', 'change', 'negation', 'set up', 'freedom']
    sentences1 = ['I want to enquire about the language courses',
                  'You should verify your information before submitting a form', 'We should utilize our time wisely',
                  'Vitamin deficiency may lead to illness', 'The results demonstrate that our campaign is working',
                  'I have a vague notion of what she does for a living',
                  'The money is principally invested in stocks and shares', 'It will be futile to protest',
                  'She apologized for the inconvenience', 'He was accused of fabricating data',
                  'Nevertheless,we will do everything', 'The wind indicates that a storm is coming',
                  'You should consult the manager about the matter', 'She refused to tolerate being called a liar',
                  'I spoke to him concerning his behaviour', 'Your training will commence tomorrow',
                  'He wondered if the decision had been prudent one',
                  'I cannot disclose the details of the transaction', 'They evade paying taxes by living abroad',
                  'He fails to comprehend their attitude', 'We took avid interest in the project',
                  'The design was modified to add another window', 'The facts seem to contradict this view',
                  'She established a reputation as a hard worker', 'People often have to fight for their liberty']
    selected_word1 = random.choice(words1)
    index = words1.index(selected_word1)
    session['formal_meanings_index'] = meanings1[index]
    session['formal_sentences_index'] = sentences1[index]
    return selected_word1


def informal():
    # list of words, their meanings and related sentences
    words2 = ['hacker', 'assemble', 'compose', 'erect', 'evolve', 'forge', 'designer', 'artist', 'contrive', 'develop',
              'fingale', 'hogger', 'swindle', 'operate', 'manage', 'scheme', 'Gobsmacked', 'analysis', 'catalogue',
              'appraise']
    meanings2 = ['a person who illegally gains access to and sometimes tampers with information in a computer system',
                 'gather together', 'constitute or make up', 'to raise',
                 'to develop or to make something develop gradually, from a simple to a more advanced form',
                 'a place where objects are made by heating and shaping metal', 'to originator who create something',
                 'inventor or a person who creates art', 'to manage to do something, although there are difficulties',
                 'to grow slowly', 'act in a dishonest or devious manner',
                 'a person who takes or uses most or all of a particular thing in an unfair or selfish way',
                 'to trick somebody in order to get money', 'to work, or to make something work',
                 'to be incharge or control of something',
                 'an official plan or system for doing or organizing something',
                 'to be amazed',
                 'the careful examination of the different parts or details of something',
                 'a list of all the things that you can buy, see, etc. somewhere', 'to set a value on']
    sentences2 = ['A hacker had managed to get into the system.', 'Assemble your papers and put them in the file.',
                  'Advait composes music.',
                  'I like to erect towers out of blocks and then knock them over.', 'Any evolved gas must be examined.',
                  'A forge for making weapons was found there.', 'The designer came in for a lot of criticism.',
                  'He was a master printer and an artist of the first order.',
                  'I decided to contrive a meeting between the two of them.', 'Please develop this project.',
                  'The fingale factor is still at work.', 'I was always a spotlight hogger.',
                  'He used to swindle people out of their land.', 'We must operate immediately.',
                  'I manage the destinies of billions of the living.', 'The scheme is also open to non-members.',
                  'People were gobsmacked by seeing the project',
                  'The analysis of what kind of temperament you possess is vital.',
                  'The catalogue is updated every year.', 'Appraise the evidence in a systematic way together.']
    selected_word2 = random.choice(words2)
    index = words2.index(selected_word2)
    session['informal_meanings_index'] = meanings2[index]
    session['informal_sentences_index'] = sentences2[index]
    return selected_word2


def public():
    # list of words, their meanings and related sentences
    words3 = ['elocution', 'summary' , 'success', 'learning']
    meanings3 = ['expert manner of speaking', 'gist']
    sentences3 = ['He did take part in an elocution competition', 'You can write a summary about the key components']
    selected_word3 = random.choice(words3)
    index = words3.index(selected_word3)
    session['public_meanings_index'] = meanings3[index]
    session['public_sentences_index'] = sentences3[index]
    return selected_word3


def any():
    # list of words, their meanings and related sentences
    words4 = ['midnight', 'civilian', 'success', 'learning']
    meanings4 = ['twelve at night', 'a person not in the armed services or the police force']
    sentences4 = ['We used to go for a midnight walk', 'Every effort is being made to minimize civilian casualties']
    selected_word4 = random.choice(words4)
    index = words4.index(selected_word4)
    session['any_meanings_index'] = meanings4[index]
    session['any_sentences_index'] = sentences4[index]
    return selected_word4


# Function for jumbling the characters of the chosen word.
def jumble(word):
    # sample() function jumbling the characters of the word
    random_word = random.sample(word, len(word))

    # join() function join the elements
    # of the iterator(e.g. list) with particular character .
    jumbled = ''.join(random_word)
    return jumbled


@app.route('/rules')
def rules():
    return render_template('rules.html')



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
    if request.form.get("submit1"):
        return redirect(url_for('jwords_formal'))
    elif request.form.get("submit2"):
        return redirect(url_for('jwords_informal'))
    elif request.form.get("submit3"):
        return redirect(url_for('jwords_public'))
    elif request.form.get("submit4"):
        return redirect(url_for('jwords_any'))
    return render_template('displaynames.html', form=form, user1=user1, user2=user2)


@app.route('/scenario1', methods=['GET', 'POST'])
def jwords_formal():
    form = Guess1()
    error = ""
    meaning = ""
    sentence = ""
    wrong_guess = ""
    wrong_test = ""
    test = ""
    meaning_intro = ""
    sentence_intro = ""
    i = ""
    user1 = session['data1']  # Set values
    user2 = session['data2']  # Set values
    message = 'Good Luck!'
    currentUser = user1

    if session.get('CURRENTPLAYER') is None:
        session['CURRENTPLAYER'] = user1
        acutal_word = formal()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word
        session['counter_user2'] = 0
        session['counter_user1'] = 0

    if request.method == 'POST':
        if session['CURRENTPLAYER'] == user1:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                session['counter_user1'] = session['counter_user1'] + 1
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user2
            session['CURRENTPLAYER'] = user2
        elif session['CURRENTPLAYER'] == user2:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                session['counter_user2'] = session['counter_user2'] + 1
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['formal_meanings_index']
                sentence = session['formal_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user1
            session['CURRENTPLAYER'] = user1

        acutal_word = formal()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word

    return render_template("formal.html", form=form, currentUser=currentUser, x=session['picked_word'], message=message,
                           picked_word=session['picked_word'],
                           acutal_word=session['acutal_word'], score1=session['counter_user1'],
                           score2=session['counter_user2'], error=error, meaning=meaning, sentence=sentence,
                           wrong_guess=wrong_guess, test=test, wrong_test=wrong_test, i=i, meaning_intro=meaning_intro,
                           sentence_intro=sentence_intro, user1=user1, user2=user2)


@app.route('/scenario2', methods=['GET', 'POST'])
def jwords_informal():
    form = Guess1()
    error = ""
    meaning = ""
    sentence = ""
    wrong_guess = ""
    wrong_test = ""
    test = ""
    meaning_intro = ""
    sentence_intro = ""
    i = ""
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
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['informal_meanings_index']
                sentence = session['informal_sentences_index']
                session['counter_user1'] = session['counter_user1'] + 1
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['informal_meanings_index']
                sentence = session['informal_sentences_index']
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user2
            session['CURRENTPLAYER'] = user2
        elif session['CURRENTPLAYER'] == user2:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                session['counter_user2'] = session['counter_user2'] + 1
                meaning = session['informal_meanings_index']
                sentence = session['informal_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['informal_meanings_index']
                sentence = session['informal_sentences_index']
                if session['counter_user2'] == 3:
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
                           score2=session['counter_user2'], error=error, meaning=meaning, sentence=sentence,
                           wrong_guess=wrong_guess, test=test, wrong_test=wrong_test, i=i, meaning_intro=meaning_intro,
                           sentence_intro=sentence_intro, user1=user1, user2=user2)


@app.route('/scenario3', methods=['GET', 'POST'])
def jwords_public():
    form = Guess1()
    error = ""
    meaning = ""
    sentence = ""
    wrong_guess = ""
    wrong_test = ""
    test = ""
    meaning_intro = ""
    sentence_intro = ""
    i = ""
    user1 = session['data1']  # Set values
    user2 = session['data2']  # Set values
    message = 'Good Luck!'
    currentUser = user1

    if session.get('CURRENTPLAYER') is None:
        session['CURRENTPLAYER'] = user1
        acutal_word = public()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word
        session['counter_user2'] = 0
        session['counter_user1'] = 0

    if request.method == 'POST':
        if session['CURRENTPLAYER'] == user1:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['public_meanings_index']
                sentence = session['public_sentences_index']
                session['counter_user1'] = session['counter_user1'] + 1
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['public_meanings_index']
                sentence = session['public_sentences_index']
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user2
            session['CURRENTPLAYER'] = user2
        elif session['CURRENTPLAYER'] == user2:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                session['counter_user2'] = session['counter_user2'] + 1
                meaning = session['public_meanings_index']
                sentence = session['public_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['public_meanings_index']
                sentence = session['public_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user1
            session['CURRENTPLAYER'] = user1

        acutal_word = public()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word

    return render_template("formal.html", form=form, currentUser=currentUser, x=session['picked_word'], message=message,
                           picked_word=session['picked_word'],
                           acutal_word=session['acutal_word'], score1=session['counter_user1'],
                           score2=session['counter_user2'], error=error, meaning=meaning, sentence=sentence,
                           wrong_guess=wrong_guess, test=test, wrong_test=wrong_test, i=i, meaning_intro=meaning_intro,
                           sentence_intro=sentence_intro, user1=user1, user2=user2)


@app.route('/scenario4', methods=['GET', 'POST'])
def jwords_any():
    form = Guess1()
    error = ""
    meaning = ""
    sentence = ""
    wrong_guess = ""
    wrong_test = ""
    test = ""
    meaning_intro = ""
    sentence_intro = ""
    i = ""
    user1 = session['data1']  # Set values
    user2 = session['data2']  # Set values
    message = 'Good Luck!'
    currentUser = user1

    if session.get('CURRENTPLAYER') is None:
        session['CURRENTPLAYER'] = user1
        acutal_word = any()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word
        session['counter_user2'] = 0
        session['counter_user1'] = 0

    if request.method == 'POST':
        if session['CURRENTPLAYER'] == user1:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['any_meanings_index']
                sentence = session['any_sentences_index']
                session['counter_user1'] = session['counter_user1'] + 1
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['any_meanings_index']
                sentence = session['any_sentences_index']
                if session['counter_user1'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user2
            session['CURRENTPLAYER'] = user2
        elif session['CURRENTPLAYER'] == user2:
            chance1 = form.chance1.data
            if chance1 == session['acutal_word']:
                error = 'Congratulations !!'
                test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                session['counter_user2'] = session['counter_user2'] + 1
                meaning = session['any_meanings_index']
                sentence = session['any_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            else:
                error = 'Better Luck next time...'
                wrong_guess = "The word was "
                wrong_test = session['acutal_word']
                meaning_intro = "The meaning of the word "
                i = "is : "
                sentence_intro = "The sentence associated with the word "
                meaning = session['any_meanings_index']
                sentence = session['any_sentences_index']
                if session['counter_user2'] == 3:
                    return redirect(url_for('result', user=session['CURRENTPLAYER'], error=error))
            currentUser = user1
            session['CURRENTPLAYER'] = user1

        acutal_word = any()
        picked_word = jumble(acutal_word)
        session['acutal_word'] = acutal_word
        session['picked_word'] = picked_word

    return render_template("formal.html", form=form, currentUser=currentUser, x=session['picked_word'], message=message,
                           picked_word=session['picked_word'],
                           acutal_word=session['acutal_word'], score1=session['counter_user1'],
                           score2=session['counter_user2'], error=error, meaning=meaning, sentence=sentence,
                           wrong_guess=wrong_guess, test=test, wrong_test=wrong_test, i=i, meaning_intro=meaning_intro,
                           sentence_intro=sentence_intro, user1=user1, user2=user2)


@app.route('/result/<user>')
def result(user):
    return render_template("successful.html", user=user)

