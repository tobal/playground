import oi


def main():
    program = oi.Program('my program', 'ipc:///tmp/oi-ulamyzfdwb.sock')
    program.add_command('ping', lambda: 'pong')
    program.add_command('state', lambda: program.state)
    program.run()

if __name__ == '__main__':
    main()
