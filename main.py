commands = []
while (i := input()) != 'close':
    commands.append(i)
d = []
for command in commands:
    match command.split():
        case ['pop']:
            pop = d.pop()
            print(pop)
        case ['head']:
            head = d[-1]
            print(head)
        case 'add', path:
            d.append(path)