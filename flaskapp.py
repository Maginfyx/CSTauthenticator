from flask import Flask

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'GET':
        msg = "this is a response to roblox instance, sent from python"
        print("SENT >>", msg)
        return msg
    print("RECEIVED >>",list(request.form))
    return render_template('index.html')
