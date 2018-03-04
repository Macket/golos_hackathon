from blockchain import login, User


def main():
    user = login('poster', 'qwerty12345')
    video = user.get_video('videopotest', '/Users/alexander/potest.mp4')
    print(1)


if __name__ == '__main__':
    main()
