import sqlite3


class Computer:
    def __init__(self, name='', ipv4='', ipv6=''):
        self.name = name
        self.ipv4 = ipv4
        self.ipv6 = ipv6

    def ping(self):
        pass

    def add(self):
        with sqlite3.connect('./db/network.db') as conn:
            cur = conn.cursor()
            res = cur.execute(f'INSERT INTO computers(name, ipv4, ipv6) VALUES ("{self.name}", "{self.ipv4}", "{self.ipv6}");')
            conn.commit()
        return res

    @classmethod
    def select_all(self):
        with sqlite3.connect('./db/network.db') as conn:
            cur = conn.cursor()
            res = cur.execute('SELECT * FROM computers')
            conn.commit()
        return res

    def edit(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    comp = Computer(name='server1', ipv4='0.0.0.0')
    print(comp.add())

