Steps to deploy a static Flask website to Heroku:

1. Create an account on www.heroku.com if you don't have one already.
2. Download and install Heroku Toolbelt from https://devcenter.heroku.com/articles/heroku-cli
3. Install gunicorn with "pip install gunicorn". Make sure you're using pip from your virtual environment if you have one.
4. Create a requirement.txt file in the main app directory where the main Python app file is located. You can create that file by running "pip freeze > requirements.txt" in the command line. Make sure you're using pip from your virtual environment if you have one. The requirement.txt file should now contain a list of Python packages.
5. Create a file named "Procfile" in the main app directory. The file should not contain any extension. Then type in this line inside: "web: gunicorn script1:app" where "script1" should be replaced with the name of your Python script and "app" with the name of the variable holding your Flask app.
6. Create a runtime.txt file in the main app directory and type "python-3.5.1" inside.
If you're using Python 2, you may want to type in "python-2.7.11" instead.
7. Open your computer terminal/command line to point to the directory where the Python file containing your app code is located.
8. Using the terminal, log in to Heroku with "heroku login"
9. Enter your Heroku email address
10. Enter your Heroku password
11. Create a new Heroku app with "heroku create myawesomeappname"
17. Initialize a local git repository with "git init"
18. Add your local application files to git with "git add ."
19. Tell git your email address with "git config --global user.email "myemail@hotmail.com"". Make sure the email address is inside quotes here. 
20. Tell git your username (just pick whatever username) with "git config --global user.name "whateverusername"". The username should be in quotes.
21. Commit the changes with "git commit -m "first commit"". Make sure "first commit" is inside quotes.
22. Before pushing the changes to Heroku, tell heroku the name of the app you want to use with "heroku git:remote --app myawesomeappname"
23. Push the changes to Heroku with "git push heroku master"
26. That should do it. Go ahead and open your app with "heroku open".

Updating the app data:
Currently, the data is being saved to a public repo at https://raw.githubusercontent.com/srinu5019/mypublicdata/master/Intents.txt. Please reachout to Sreenivas Gundala for further edits on this page. 
Note:This is tempoary. The file will be deleted from GitHub later and then you refer to static content in this repo.
Edit guide lines:
Example:
For user selection of 3 on CCLBot home screen:
3 <If user selects this; below info will be displayed>
Check the following:<br>1) Is correct code file assigned to lane?<br>2) Is the Pinpad properly connected?<br>3) Are all the required code files downloaded?<br> Need more help? yes/no
3.yes <If user selects yes in above step, this info will be displayed>
1) Ensure your code file is latest to 20.6 <br>2) Ensure your lane does not have multiple or contradictory files assigned at once <br>3) Verify SVCJournal log to see if code file is downloaded<br>Do you have anything else to help with? yes/no
3.no <if user selects no in first step, support data will be displayed>
support
3.yes.yes <if user selects yes in second step, he will be routed to home>
home
3.yes.no <if user selects no in second step, conversation will be end with thanks info>
thanks