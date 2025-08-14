import sqlite3

conn = sqlite3.connect("Videos_DB")

cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTs Videos(id INTEGER PRIMARY KEY , name CHAR NOT NULL, time CHAR NOT NULL )")

def List_videos():
    cursor.execute("SELECT * FROM Videos")
    data = cursor.fetchall()
    for id,name,time in data:
        print(f"{id}. Name :- {name.upper()} ,Time :- {time}")
    if (not data):
        print("You have not added any video yet ")

   
def add_videos():
    name = input("enter the video name : ")
    duration = input("enter the video duration : ")
    cursor.execute("INSERT INTO Videos (name , time) VALUES(?,?)",(name,duration))
    conn.commit()

    

def update_videos():
    id = int(input("enter the id of video which has to be updated : "))
    name = input("enter the video name : ")
    duration = input("enter the video duration : ")
    cursor.execute("UPDATE Videos SET name = ? , time = ? WHERE id = ?",(name,duration,id))
    conn.commit()
    


def delete_videos():
    id = int(input("enter the id of video which has to be updated : "))
    cursor.execute("DELETE FROM Videos WHERE id = ?",(id,))
    conn.commit()
    
    

def main():
    while True:
        print("1.List all videos")
        print("2.add videos")
        print("3.update videos")
        print("4.delete videos")
        print("5.Exit the app")
        print("\n")
        choice = input("enter your choice:- ")

        match choice:
            case "1":
                List_videos()
            case "2":
                add_videos()
            case "3":
                update_videos()
            case "4":
                delete_videos()
            case "5":
                break
            case _:
                print("invalid choice")
    conn.close()

if __name__ == "__main__":
    main()


            



    
    
