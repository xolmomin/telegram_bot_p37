from models import Region

if __name__ == '__main__':
    data = [
        {
            'name': 'Buxoro'
        },
        {
            'name': 'Samarqand'
        }
    ]

    Region.bulk_create(data)
    print("Qo'shildi")
