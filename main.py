import connectionDB as cnx
from fastapi import FastAPI

#
app = FastAPI()

#decorator to make a route !
@app.get("/")
def read_data():
    return {"YOU":"Whalecom !"}
#-------------------------------------------------
#show all employes
@app.get("/employees")
def get_all_employees():
    sql="select * from employees"
    data=cnx.getData(sql)
    return data
#-------------------------------------------------
#
@app.get("/employees/{myid}")
def get_employees_byId(myid:int):
    sql=f"select * from employees where id={myid}"
    data=cnx.getData(sql)
    return data
#-------------------------------------------------
#
@app.delete("/employees/delete/{myid}")
def delete_employee(myid:int):
    sql=f"delete from employees where id={myid}"
    cnx.setData(sql)
    data = cnx.getData("select * from employees")
    return {
        "message":"Deleted successsfully",
        "employees after delete":data
    }

@app.post("/employees/create")
def create_employee(mydata:dict):
    name =mydata["name"]
    age=mydata["age"]
    dep=mydata["departement"]
    sql=f"insert into employees (name,age,departement)values ('{name}',{age},'{dep}')"
    cnx.setData(sql)
    return {
        "message":"Added successsfully",
    }

@app.put("/employees/update/{_id}")
def update_employee(mydata:dict,_id:int):
    name =mydata["name"]
    age=mydata["age"]
    dep=mydata["departement"]
    sql=f"update employees set name='{name}' , age={age} , departement='{dep}' where id={_id};"
    cnx.setData(sql)
    return {
        "message":"Updated successsfully",
    }