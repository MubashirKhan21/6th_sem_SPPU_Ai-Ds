show dbs
use admin
db.emp.insert({id:'1',name:'Prathamesh'})
db.emp.insert({id:'1',name:'Dhoni'})
db.emp.insert({id:'3',name:'Virat'})
db.emp.insert({id:'4',name:'Sachin'})
db.emp.find().pretty()

db.emp.update({name:"Dhoni"},{$set:{id:"2"}})
db.emp.find().pretty()
db.emp.remove({id:"2"})
db.emp.find().pretty()