class shoes:
    def __init__(self, size=42):
        self.object = 'обувь'
        self.size = size

    def wear(self):
        print('не забудьте надеть обувь перед выходом на улицу')

    def torn(self):
        print('ваша обувь порвалась')


class winter_shoes(shoes):
    def __init__(self):
        super().__init__()
        self.property = ['тёплые', 'тяжёлые']

    def action(self):
        print('греет ноги')


class summer_shoes(shoes):
    def __init__(self):
        super().__init__()
        self.property = ['лёгкие', 'открытые']

    def action(self):
        print('с ними легко передвигаться')


class valenki(winter_shoes):
    def __init__(self):
        super().__init__()
        self.price = 3000
        self.material = 'шерсть'

    def song(self):
        print('валенки, валенки, не подшиты, стареньки')


class bertsy(winter_shoes):
    def __init__(self):
        super().__init__()
        self.price = 2000
        self.material = 'кожа'

    def dirt(self):
        print('ходить по грязи')


class slates(summer_shoes):
    def __init__(self):
        super().__init__()
        self.price = 200
        self.material = 'резина'

    def beach(self):
        print('ходить на пляж')


class sneakers(summer_shoes):
    def __init__(self):
        super().__init__()
        self.price = 3500
        self.material = 'cloth'

    def run(self):
        print('БЕГИ, ФОРЕСТ, БЕГИ')


if __name__ == "__main__":
    a=sneakers()
    a.wear()
    a.run()
    a.size=45
    print(a.size)
    b = valenki()
    b.action()
    print(b.size)
