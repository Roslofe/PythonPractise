"""
Instructions:
Write a program for a gold club that reads each player's name and gold score as keyboard input, then save these records in a file named golf.txt
(Each record will have a field for the player's name and a field for the player's score.)
"""

def golfRecorder():
    print("Welcome to golfRecorder. Here you can store your name and score.")
    try:
        targetFile = open('golf.txt', 'a')
        wantToContinue = "Yes"
        while wantToContinue == "Yes":
            playerName = str(input("Enter your name: "))
            playerScore = int(input("Enter your score: "))
            targetFile.write(playerName + "\n")
            targetFile.write(str(playerScore) + "\n")
            wantToContinue = str(input("Do you want to enter more people? "))
        print("All values were saved in 'golf.txt'")
    except ValueError:
        print("The name must be in letters, and score in integers.")
    except IOError:
        print("Error with finding the file")
    except:
        print("Something went wrong")
    finally:
        targetFile.close
        
golfRecorder()