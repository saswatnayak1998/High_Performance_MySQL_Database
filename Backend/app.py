from flask import Flask, render_template, request, jsonify

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlDatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9436068918@localhost/trial'

db = SQLAlchemy(app)

class Files(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(200), nullable=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    parent = db.Column(db.Integer, nullable=False)
    def __repr__(self): 
        return '<Task %r>' % self.id

class Permissions(db.Model):
    perm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    file_id = db.Column(db.Integer, db.ForeignKey('files.id'), nullable=False)
    r_perm = db.Column(db.Boolean, nullable=False)
    w_perm = db.Column(db.Boolean, nullable=False)
    a_perm = db.Column(db.Boolean, nullable=False)


@app.route('/files', methods=['GET'])
def get_files():
    files = Files.query.all()
    output = []
    for file in files:
        file_data = {}
        file_data['id'] = file.id
        file_data['name'] = file.name
        file_data['data'] = file.data
        file_data['created'] = file.created
        file_data['updated'] = file.updated
        file_data['parent'] = file.parent
        output.append(file_data)
    return jsonify({'files': output})

@app.route('/permissions', methods=['GET'])
def get_permissions():
    permissions = Permissions.query.all()
    output = []
    for permission in permissions:
        perm_data = {}
        perm_data['perm_id'] = permission.perm_id
        perm_data['user_id'] = permission.user_id
        perm_data['file_id'] = permission.file_id
        perm_data['r_perm'] = permission.r_perm
        perm_data['w_perm'] = permission.w_perm
        perm_data['a_perm'] = permission.a_perm
        output.append(perm_data)
    return jsonify({'Permissions': output})

@app.route("/files", methods=['POST'])
def createFile():

    # access data submitted with HTTP request
    fileInfo = request.json

    # create file object with request data
    newFile = Files(
        name=fileInfo['name'], 
        data=fileInfo['data'], 
        created=fileInfo['created'], 
        updated=fileInfo['updated'], 
        parent=fileInfo['parent'])

    # check that user has write permissions to the parent directory using the following SQL query:
    # SELECT w_perm 
    # FROM Permissions 
    # WHERE Permissions.user_id = myUserID 
    # AND Permissions.file_id = fileID

    # id below is supposed to reference primary key of Files model table. 

    ###Create some dumy permission data so that this works
    # writePermission = db.session.execute(db.select(w_perm).where(user_id == myUserID and file_id == id)).scalar()
    # if not writePermission:
    #     return({'message': 'You do not have write permissions for this directory'})

    # add new file object to database
    db.session.add(newFile)
    db.session.commit()
    return jsonify({'message': 'File created'})

@app.route('/permissions', methods=['POST'])
def create_permissions():
    # Assume the request will contain a list of permissions
    permissions_info = request.json  # This should be a list of dictionaries

    for perm_info in permissions_info:
        new_permission = Permissions(
            user_id=perm_info['user_id'],
            file_id=perm_info['file_id'],
            r_perm=perm_info['r_perm'],
            w_perm=perm_info['w_perm'],
            a_perm=perm_info['a_perm']
        )
        db.session.add(new_permission)

    # Commit all new permissions at once
    db.session.commit()

    return jsonify({'message': f'{len(permissions_info)} permissions created'}), 201


@app.route('/user_permissions', methods=['GET'])
def user_file_permissions():
    # Query to fetch users with read permissions
    permissions = db.session.query(
        Permissions.user_id, Files.name
    ).join(Files, Permissions.file_id == Files.id).filter(Permissions.r_perm == True).all()

    output = {}
    for user_id, file_name in permissions:
        if user_id in output:
            output[user_id].append(file_name)
        else:
            output[user_id] = [file_name]

    return jsonify(output)


@app.route('/files/<int:id>', methods=['PUT'])
def update_file(id):
    # Update logic goes here
    file = Files.query.get(id)
    if not file:
        return jsonify({'message': 'No file found'}), 404

    data = request.json
    file.name = data.get('name', file.name)
    file.data = data.get('data', file.data)
    db.session.commit()
    return jsonify({'message': 'File updated'}), 200

@app.route('/files/<int:id>', methods=['DELETE'])
def delete_file(id):
    file = Files.query.get(id)
    if not file:
        return jsonify({'message': 'No file found'}), 404

    db.session.delete(file)
    db.session.commit()
    return jsonify({'message': 'File deleted'}), 200

@app.route('/registerPage.html', methods = ['POST', 'GET'])
def registerPage():
    return render_template('registerPage.html')

@app.route('/fileSystemHomePage.html', methods = ['POST', 'GET'])
def fileSystemHome():
    return render_template('fileSystemHomePage.html')

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('loginPage.html')

with app.app_context(): 
    db.create_all()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

#Get comments 
    





