import json
def List_videos(videos):
    data = enumerate(videos , start=1)
    for index,video in data:
        print(f"{index}. {video['name']} {video['time']}")
        print('\n')
    
def add_videos(videos):
    name = input("enter video name :- ")
    time = input("enter duration :- ")
    videos.append({'name':name ,'time':time})
    Save_data(videos)


def update_videos(videos):
    index =int(input("enter index which has to be updated:- "))
    if 1 <= index <= len(videos):
        name = input("enter video name :- ")
        time = input("enter duration :- ")
        videos[index - 1] = {'name':name ,'time':time}
    else:
        print("invalid index")
    Save_data(videos)


def delete_videos(videos):
    index =int(input("enter index which has to be deleted:- "))
    if 1 <= index <= len(videos):
         del videos[index - 1] 
    else:
        print("invalid index")
    Save_data(videos)
    

def Load_data():
    try:
        with open('Youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def Save_data(videos):
        with open('Youtube.txt','w') as file:
           json.dump(videos,file)
    



def main():
    videos = Load_data()
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
                List_videos(videos)
            case "2":
                add_videos(videos)
            case "3":
                update_videos(videos)
            case "4":
                delete_videos(videos)
            case "5":
                break
            case _:
                print("invalid choice")

if __name__ == "__main__":
    main()


            



    
    
