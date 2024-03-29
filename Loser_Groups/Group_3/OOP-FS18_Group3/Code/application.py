from flask import Flask, flash, redirect, render_template, request, session
from helpers import apology, login_required
from controller import Controller
from flask_session import Session
from tempfile import mkdtemp
import re

controller = Controller()

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
@login_required
def index():
    """ Show user's portfolio --> What stocks were bought at what price, at what exchange rate, how the stock price
    has changed since purchase, how much cash the user has left and how valuable the total portfolio is now -->
    differential is indicated"""

    controller.portfolio.update(controller.user)
    rows = controller.portfolio.rows
    length = len(rows)-1
    return render_template("index.html", rows=rows, user=controller.user, length=length)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any userid
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure username exists and password is correct --> Use check function
        username = request.form.get("username")
        password = request.form.get("password")
        check = controller.login(username, password)
        if check is True:
            # Remember which user has logged in
            session["user_id"] = controller.user.ID
            return redirect("/")
        else:
            return apology(check, 403)

    else:
        return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("Missing username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("Missing password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("Please confirm password", 400)

        # Ensure Password and confirmation match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Password and confirmation do not match", 400)

        # Ensure Password has at least 5 characters, contains a number, a capital letter and a symbol
        while True:
            if len(request.form.get("password")) < 5:
                return apology("Password must have at least 5 characters", 400)
            elif re.search("[0-9]", request.form.get("password")) is None:
                return apology("Password must contain a number", 400)
            elif re.search("[A-Z]", request.form.get("password")) is None:
                return apology("Password must contain a capital letter", 400)
            elif re.search("['!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']", request.form.get("password")) is None:
                return apology("Password must contain a symbol", 400)
            else:
                break

        # Ensure username does not already exist --> Use check function
        username = request.form.get("username")
        password = request.form.get("password")
        check = controller.register(username, password)
        if check is True:
            # Remember which user has logged in
            session["user_id"] = controller.user.ID
            return redirect("/")
        else:
            return apology(check, 403)

    else:
        return render_template("register.html")

@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote and news articles to respective company"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        info = controller.lookup(symbol)
        # Check if symbol exists, and if it exists in the currencies that we support
        if info is not True:
            return apology(info, 400)
        return render_template("information.html", stock=controller.stock, articles=controller.articles)
    else:
        return render_template("quote.html")

@app.route("/information", methods=["GET", "POST"])
@login_required
def information():
    """Enables user to buy right after quoting a stock"""

    if request.method == "POST":

        shares = request.form.get("shares")
        enough_cash = controller.buy(controller.stock.symbol, shares)
        # Run checks to ensure user has enough cash
        if enough_cash is not True:
            return apology(enough_cash, 400)
        return redirect("/")
    else:
        return render_template("information.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))
        buy_check = controller.buy(symbol, shares)
        # Checks to see whether symbol is stated correctly, whether it is available in the supported currencies
        # & whether user has enough cash to buy the stock, otherwise render an apology
        if buy_check is not True:
            return apology(buy_check, 400)

        return redirect("/")

    if request.method == "GET":
        # Redirect to landing page
        return render_template("buy.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrieve stock form
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        # Check if User possess the number of shares he wants to sell
        sell_check = controller.sell(symbol, shares)
        if sell_check is not True:
            return apology(sell_check, 400)

        # Display index page --> Portfolio
        return redirect("/")

    else:
        symbols = controller.stock.symbols(controller.user)
        return render_template("sell.html", symbols=symbols)

@app.route("/history")
@login_required
def history():
    """Display all transactions a user conducted, beginning with the most recent"""

    controller.portfolio.get_history(controller.user)
    history = controller.portfolio.history
    length = len(history)
    return render_template("history.html", history=history, user=controller.user, length=length)

@app.route('/leader')
@login_required
def leader():
    """Display leaderboard across all users in database, sorted according to worth of portfolio"""

    controller.leaderboard.get_leader()
    leaders = controller.leaderboard.rows
    return render_template("leader.html", leaders=leaders)


if __name__ == '__main__':
    app.run()
