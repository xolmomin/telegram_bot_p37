from models import Film

if __name__ == '__main__':
    menu = """
    1. film read
    2. film update (universal)
    3. film delete
    4. film create
    5. exit
            """

    while True:
        key = input(menu)
        if key == '1':
            print('All films')
            films = Film.get_all()
            for film in films:
                print(film)
        elif key == '2':
            _id = input('Enter film id: ')
            film_name = input('Enter film name: ')
            Film.update(_id, **{'name': film_name})
            print('Successfully updated film')
        elif key == '3':
            _id = input('Enter film id: ')
            Film.delete(_id)
            print('Successfully deleted film')
        elif key == '4':
            film_name = input('Enter film name: ')
            Film.create(**{'name': film_name})
            print('Successfully created film')
