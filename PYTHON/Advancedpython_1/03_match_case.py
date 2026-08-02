def check_status(status):
    match status:#same as switch case statement in C
        case 200:
            return "Success"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"
print(check_status(int(input("Check a status(200/404/500): "))))