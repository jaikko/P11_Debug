import json
import datetime
from flask import Flask, render_template, request, redirect, flash, url_for, abort


def loadClubs():
    with open('clubs.json') as c:
        listOfClubs = json.load(c)['clubs']
        return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
        listOfCompetitions = json.load(comps)['competitions']
        return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary', methods=['POST'])
def showSummary():
    club = [club for club in clubs if club['email'] == request.form['email']]
    if club:
        return render_template('welcome.html', club=club[0], competitions=competitions)
    else:
        flash("Sorry, that email wasn't found")
        return render_template('index.html')


@app.route('/book/<competition>/<club>')
def book(competition, club):
    foundClub = [c for c in clubs if c['name'] == club]
    foundCompetition = [c for c in competitions if c['name'] == competition]
    if foundClub and foundCompetition:
        now = datetime.datetime.now()
        str = foundCompetition[0]['date'].split(" ")[0].split("-")
        compet_date =datetime.datetime(int(str[0]), int(str[1]), int(str[2]))
        if now > compet_date:
            flash("Competition expired")
            return render_template('welcome.html', club=foundClub[0], competitions=competitions)
        else:
            flash("Competition valid")
            return render_template('booking.html', club=foundClub[0], competition=foundCompetition[0])
    else:
        abort(404)


@app.route('/purchasePlaces', methods=['POST'])
def purchasePlaces():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    placesRequired = int(request.form['places'])
    if placesRequired > 12:
        flash("You can't reserve more than 12 places")
        return render_template('booking.html', club=club, competition=competition)
    if placesRequired*3 > int((club['points'])) or placesRequired > int(competition['numberOfPlaces']):
        flash("You don't have enougth point or the number entered is greater than the number of places remaining")
        return render_template('booking.html', club=club, competition=competition)
    competition['numberOfPlaces'] = int(competition['numberOfPlaces'])-placesRequired
    club['points'] = int(club['points'])-placesRequired*3
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display
@app.route('/list')
def list():
    club = [club for club in clubs]
    return render_template('recap.html', club=club)

@app.route('/logout')
def logout():
    return redirect(url_for('index'))
