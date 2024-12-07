from flask import Flask, render_template, request, redirect, url_for
from Linked_list import LinkedList

app = Flask(__name__)

Linked_list = LinkedList()

@app.route('/')
def index():
    return render_template('Linked_list.html', linked_list=Linked_list.print_list())

@app.route('/update', methods=['POST'])
def update():
    operation = request.form['operation']
    data = request.form.get('data', None)

    if operation == "insert_beginning" and data:
        Linked_list.insert_at_beginning(data)
    elif operation == "insert_end" and data:
        Linked_list.insert_at_end(data)
    elif operation == "remove_beginning":
        Linked_list.remove_beginning()
    elif operation == "remove_end":
        Linked_list.remove_end()
    elif operation == "remove_at" and data:
        Linked_list.remove_at(data)

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
