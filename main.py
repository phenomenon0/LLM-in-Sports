from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


llm = ChatOpenAI( )

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt = ChatPromptTemplate.from_template("tell me a joke about {foo}")
model = ChatOpenAI()
chain = prompt | model
chain.invoke({"foo": "bears"})

'''
@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="gpt-3.5-turbo-1106",
            prompt=generate_prompt(animal),
            temperature=0.17,
            max_tokens=1000  # Adjust this value as needed
        )
        code = response.choices[0].text.strip()
        
        # Capture the output of the executed code
        import io
        import sys
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        
        try:
            exec(code, globals())
            output = buffer.getvalue()
        except Exception as e:
            output = str(e)
        finally:
            sys.stdout = old_stdout
        
        return redirect(url_for("index", result=output))

    result = request.args.get("result")
    return render_template("index.html", result=result)

#import data from csv
df = pd.read_csv('base.csv' , header=1, index_col=0)




def generate_prompt(animal):
    return """
a dataframe with 20 columns about soccer has an example row  as such 
Rk,Player,Nation,Pos,Squad,Age,Born,MP,Starts,Min,90s,Gls,Ast,G+A,G-PK,PK,PKatt,CrdY,CrdR,xG,npxG,xAG,npxG+xAG,PrgC,PrgP,PrgR,Gls,Ast,G+A,G-PK,G+A-PK,xG,xAG,xG+xAG,npxG,npxG+xAG,Matches,-9999
1,Brenden Aaronson,us USA,MFFW,Leeds United,22-187,2000,32,28,2296,25.5,1,3,4,1,0,0,2,0,3.7,3.7,4.2,7.9,43,84,147,0.04,0.12,0.16,0.04,0.16,0.14,0.17,0.31,0.14,0.31,Matches,5bc43860
 the rows are explained Rk: Rank from top to bottom

 when manchester united is searched the is filtered for Manchester Utd in Squad
 Nott'ham Forest is nottingham forest try to make adjustments for these 
 sometimes tottenham is called spurs and Manchester Utd red devils
Nation: Nationality
Pos: Position played
Age: Current age
Born: Year of birth
MP: Matches played
Starts: Games started
Min: Minutes played
90s: Minutes played divided by 90
Gls: Goals scored
Ast: Assists
G+A: Goals + Assists
G-PK: Non-penalty goals
PK: Penalty kicks made
PKatt: Penalty kicks attempted
CrdY: Yellow cards
CrdR: Red cards
xG: Expected goals
npxG: Non-penalty expected goals
xAG: Expected assisted goals
npxG+xAG: Non-penalty expected goals plus assisted goals
PrgC: Progressive carries
PrgP: Progressive passes
PrgR: Progressive passes received
PPA: passes into the penalty area
1/3: passes into the final third
Goals/90: Goals scored per 90 
G+A/90: Goals and assists per 90 minutes
Non-penalty goals/90:
Non-penalty G+A/90: 
xG/90: Expected goals per 90 minutes
xAG/90: Expected assisted goals per 90 minutes
xG+xAG/90: Expected goals plus assisted goals per 90 minutes
npxG/90: Non-penalty expected goals per 90 minutes
npxG+xAG/90: Non-penalty expected goals plus assisted goals per 90 minutes
Tkl: Number of players tackled.
TklW: Tackles won .
Def 3rd: Tackles in defensive 1/3.
Mid 3rd: Tackles in middle 1/3.
Att 3rd: Tackles in attacking 1/3.
Tkl: Dribblers tackled.
Att: Dribbles challenged.
Tkl%: o f dribblers tackled.
Lost: Challenges lost.
Blocks: Total blocks.
Sh: Shots blocked.
Pass: Passes blocked.
Int: Interceptions.
Tkl+Int: Tackles + interceptions.
Clr: Clearances.
Err: Errors leading to opponent's shot.
PrgDist -- Progressive Passing Distance
Att -- Passes Attempted (Short)
KP -- Key Passes
Cmp% -- Pass Completion %
TotDist -- Total Passing Distance
PPA -- Passes into Penalty Area


Q: Top 5 most goals scored by a defender under 21?\n"
df_defenders_under_21 = df[(df['Pos'].str.contains('DF')) & (df['Age'] < 21)]\n
df_defenders_under_21 = df_defenders_under_21[['Player', 'Squad', 'Pos', 'Age', 'Gls', 'MP']]\n
df_defenders_under_21.sort_values(by='Gls', ascending=False, inplace=True)\n
print(df_defenders_under_21.head(5).to_html(index=False))\n

Q: Top 5 most goals scored by an English midfielder under 21 ?\n
df_midfielders_under_21 = df[(df['Pos'].str.contains('MF')) & (df['Age'] < 21) & (df['Nation'] == 'ENG')]\n
df_midfielders_under_21 = df_midfielders_under_21[['Player', 'Squad', 'Pos', 'Age', 'Gls', 'MP']]\n
df_midfielders_under_21.sort_values(by='Gls', ascending=False, inplace=True)\n
print(df_midfielders_under_21.head(5).to_html(index=False))\n

Q: Top 5 passes into the final third by a midfielder over 30 ?\n
df_midfielders_over_30 = df[(df['Pos'].str.contains('MF')) & (df['Age'] > 30)]\n
df_midfielders_over_30 = df_midfielders_over_30[['Player', 'Squad', 'Pos', 'Age', '1/3', 'MP']]\n
df_midfielders_over_30.sort_values(by='1/3', ascending=False, inplace=True)\n
print(df_midfielders_over_30.head(5).to_html(index=False))\n

Q: Who is the oldest player with an assist\n
df_assist = df[df['Ast'] > 0]\n
df_assist = df_assist[['Player', 'Squad', 'Pos', 'Age', 'Ast', 'MP']]\n
df_assist.sort_values(by='Age', ascending=False, inplace=True)\n
print(df_assist.head(1).to_html(index=False))\n

Q: Who is the top assister amongst these 3 teams, Brighton, Brentford, and Crystal Palace\n
df_teams = df[(df['Squad'] == 'Brighton') | (df['Squad'] == 'Brentford') | (df['Squad'] == 'Crystal Palace')]\n
df_teams = df_teams[['Player', 'Squad', 'Pos', 'Age', 'Ast', 'MP']]\n
df_teams.sort_values(by='Ast', ascending=False, inplace=True)\n
print(df_teams.head(1).to_html(index=False))\n

Q: players with most goals from manchester united\n
df_players = df[df['Squad'] == 'Manchester Utd']\n
df_players.sort_values(by='Gls', ascending=False, inplace=True)\n
print(df_players.head(1).to_html(index=False))\n


Q: {}\n""".format(
    (animal)
    )
'''