students = {
    "S001" : {
"name":"Aarav",
"age" : 11,
"class" : "6th",
"marks": { 
    "Maths":90,
   "Science":88,
   "English":94


}
},
"S002" : {
    "name" : "Nameerah"
    "age" : "25"
    "class" : "15th"
    "marks" : {
        "maths" : 84,
        "science" : 92,
        "english" : 96}
},
    }

for student_id, student_data in students.item():

    print("\nStudent ID: ", student_id)
    print("name", student_data["name"])
    print("age", student_data["age"])
    print("class", student_data["class"])
           