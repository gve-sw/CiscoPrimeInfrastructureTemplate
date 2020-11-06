from flask import Flask, request
from flask import render_template
from flask import json

from get_inventory import inventory, get_prime
from create_job import deploy_template, add_template

from database_connection import get_templates, get_template
from env_var import prime_list

app = Flask(__name__)

@app.route("/")
def templates():
    all_templates = get_templates()
    return render_template("conf_templates.html", content=[{"templates": all_templates}])

@app.route("/templates/<id>")
def template_details(id):
    template = get_template(id)
    return render_template("conf_template_details.html", content=template)

@app.route("/prime")
def prime_instance():
    return render_template("prime_instance.html", content=prime_list, page='prime', msg='view the inventory for')

@app.route("/prime/<id>")
def server(id):
    devices = inventory(id)
    return render_template("devices.html", content=[{"devices": devices}], pi=get_prime(int(id)))

@app.route("/deploy")
def choose_prime():
    return render_template("prime_instance.html", content=prime_list, page='deploy', msg='make changes to')

@app.route("/deploy/<id>/", methods=['GET', 'POST'])
def deploy_templates(id):
    devices = inventory(id)
    all_templates = get_templates()
    if request.method == 'POST':
        form_data = request.form
        try:
            device = form_data['servers']
        except:
            device = ''
        try:
            template_id = form_data['templates']
        except:
            template_id = ''
        name = get_template(template_id)['name']
        return render_template("selection.html", pi=id, servers=device, templates={'id': template_id, 'name': name})

    return render_template("deploy_templates.html", pi=id, servers=devices, templates=all_templates)

@app.route('/deploy/<id>/selection', methods=['POST'])
def review_selection(id):
    form_data = request.form
    servers = form_data['servers']
    template_id = form_data['templates']
    template_name = get_template(template_id)['name']
    try:
        print('starting deploy template')
        result = deploy_template(id, servers, template_id, template_name)
    except Exception as e:
        message = e
        return render_template("error.html")
    return render_template("selection.html", pi=id, servers=servers, templates={'id': template_id, 'name': template_name}, message=result)

@app.route("/create")
def choose_prime_2():
    return render_template("prime_instance2.html", content=prime_list, page='create', msg='insert a template to')

@app.route("/create/<id>/", methods=['GET', 'POST'])
def create_template(id):
    all_templates = get_templates()
    if request.method == 'POST':
        form_data = request.form
        try:
            template_id = form_data['templates']
        except:
            template_id = ''
        name = get_template(template_id)['name']
        return render_template("selection2.html", pi=id, templates={'id': template_id, 'name': name})
    return render_template("create_templates.html", pi=id,  templates=all_templates)

@app.route('/create/<id>/selection', methods=['POST'])
def review_selection2(id):
    form_data = request.form
    template_id = form_data['templates']
    template_name = get_template(template_id)['name']
    try:
        result = add_template(id,template_id)
        #result = create_template(id, template_id)
    except Exception as e:
        message = e
        return render_template("error.html")

    return render_template("selection2.html", pi=id,  templates={'id': template_id, 'name': template_name}, message=result)

if __name__ == "__main__":
    app.run(debug=True)
