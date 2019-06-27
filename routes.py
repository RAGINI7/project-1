from app import app
@app.route('/')
@app.route('/index')
def index():
    user={'username':'ragini goel'}
    return'''
    <html>
    <head>
     <title>MY APPLICATION</title>
     </head>
     <body bgcolor='cyan'>
     <h1>Hello,'''+user['username']+'''!</h1>
     </body>
     </html>'''