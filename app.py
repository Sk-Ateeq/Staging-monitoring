from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Welcome Anime Fans!</h1>
    <p>Hello Everyone, I am a huge fan of <strong>L. Lawliet</strong>, <strong>Monkey D. Luffy</strong>, and <strong>Levi Ackerman</strong>.</p>
    <p>Feel free to explore different sections based on my favorite anime!</p>
    <ul>
        <li><a href="/onepiece">One Piece</a></li>
        <li><a href="/deathnote">Death Note</a></li>
        <li><a href="/aot">Attack on Titan</a></li>
    </ul>
    '''

@app.route('/onepiece')
def onepiece():
    return '''
    <h1>One Piece Discussion</h1>
    <p>Garp is a little bit overrated. While he is strong and an absolute legend in the Marines, some people place him on a pedestal higher than he deserves.</p>
    <p>However, his role in the story, his relationship with Luffy, and his past battles make him an unforgettable character!</p>
    '''

@app.route('/deathnote')
def deathnote():
    return '''
    <h1>Death Note Thoughts</h1>
    <p>I like <strong>L</strong> more than <strong>Kira</strong> because L had no supernatural powers and still managed to be an extraordinary detective.</p>
    <p>His intellect, quirky behavior, and deep commitment to justice made him one of the best characters in the anime.</p>
    '''

@app.route('/aot')
def attack_on_titan():
    return '''
    <h1>Attack on Titan: My Favorite Character</h1>
    <p>I prefer <strong>Levi Ackerman</strong> over Eren. While Eren’s journey is incredible, Levi stands out as an unmatched warrior.</p>
    <p>His skills in battle, his leadership, and his backstory make him an absolute beast. His ability to stay composed and fight against Titans, even when everything seems hopeless, is what makes him one of the greatest characters in AoT.</p>
    '''

if __name__ == '__main__':
    app.run(debug=True)

