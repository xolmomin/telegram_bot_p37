from models import Region

if __name__ == '__main__':
    data = {
        'name': 'Samarqand'
    }

    Region.create(**data)
    print("Qo'shildi")

"""
Task
1. film read
2. film update
3. film delete
4. film create
5. exit
"""
