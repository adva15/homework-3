# start

volume_level: int = int(input("enter a volume_level:"))

match volume_level:
    case 1:
        print("mute")
    case 2:
        print("very quiet")
    case 3:
        print("very quiet")
    case 4:
        print("moderately quiet")
    case 5:
        print("medium")
    case 6:
        print("moderately loud")
    case 7:
        print("loud")
    case 8:
        print("very loud")
    case 9:
        print("extremely loud")
    case _:
        print("extremely loud")

# end