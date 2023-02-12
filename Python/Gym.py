class Member:
    def __init__(self, name, ID, weight, height, bench_press, squat, deadlift):
        self.name = name
        self.ID = ID
        self.weight = weight
        self.height = height
        self.bench_press = bench_press
        self.squat = squat
        self.deadlift = deadlift


class GymProgressionApp:
    def __init__(self):
        self.members = []

    def add_member(self, name, ID, weight, height, bench_press, squat, deadlift):
        member = Member(name, ID, weight, height, bench_press, squat, deadlift)
        self.members.append(member)
        print("Member information added successfully.")

    def view_progression(self, ID):
        for member in self.members:
            if member.ID == ID:
                print("Name: ", member.name)
                print("Weight: ", member.weight)
                print("Height: ", member.height)
                print("Bench Press: ", member.bench_press)
                print("Squat: ", member.squat)
                print("Deadlift: ", member.deadlift)
                break
        else:
            print("Member not found.")


app = GymProgressionApp()
while True:
    print("Enter 1 to add member information")
    print("Enter 2 to view progression")
    print("Enter 3 to exit")
    choice = int(input())

    if choice == 1:
        name = input("Enter member name: ")
        ID = int(input("Enter member ID: "))
        weight = float(input("Enter weight: "))
        height = float(input("Enter height: "))
        bench_press = int(input("Enter bench press: "))
        squat = int(input("Enter squat: "))
        deadlift = int(input("Enter deadlift: "))
        app.add_member(name, ID, weight, height, bench_press, squat, deadlift)
    elif choice == 2:
        ID = int(input("Enter member ID: "))
        app.view_progression(ID)
    elif choice == 3:
        break
    else:
        print("Invalid option selected. Please try again.")
