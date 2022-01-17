from src.menu import menu


def main():
    '''
    Application entry point, show interactive menu
    '''
    try:
        menu()
    except KeyboardInterrupt:
        print(' Good bye...')
    except Exception as err:  # Gracefully exit the app
        err  # Could save it to a file
        input('Something went wrong. 😥')


main()
