from flask import Flask , render_template, request
import json , requests

app = Flask(__name__)

@app.route('/search')
def search_endpoint():
    
    province = request.args.get('province')
    year = request.args.get('year')

    with open('D:\KarachiAi\Data Acquisation and Orchestration\Week2 (apis and flask)\Assignment\code\compile_data.json', 'r') as f:
        elections = json.load(f)
    
    print(elections[:2])  
    
    display = []
    
    if province and not year:
        for items in elections:
            if items.get('province') == province:   
                display.append(items)
        
        return render_template('election.html', elections=display)
    
    elif year and not province:
        for items in elections:
            if items.get('year') == year:   
                display.append(items)
        
        return render_template('election.html', elections=display)
    
    elif province and year:
        for items in elections:
            if items.get('year') == year and items.get('province') == province:   
                display.append(items)
        
        return render_template('election.html', elections=display)
    
    else:
        return render_template('election.html', elections=elections)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)
