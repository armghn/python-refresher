database = {
    1: "Armaghan",
    2: "Ali",
    3: "Sara"
}


def get_user_from_db(user_id):
    return database.get(user_id)