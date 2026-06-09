for i in range(0, 15):
    generated_password = name + r.choice(separators) + r.choice(first) + r.choice(separators) + r.choice(second) + r.choice(separators) + r.choice(third)
    t.cprint(' | %-35s| %-20s|' % (generated_password, (log(82)/log(2)) * len(generated_password)), 'green')