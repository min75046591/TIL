from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed
from faker import Faker
from books.models import Book
from accounts.models import User


user = User.objects.get(pk=1)  # book 생성자

# python manage.py seed - books
class Command(BaseCommand):
    help = "이 커멘드는 book을 생성합니다"

    def add_arguments(self, parser):
        parser.add_argument("--total", type=int, help='몇 개의 데이터를 생성할지 결정')

    # handel --> 이 커멘드가 호출 됐을 때 실행할 로직
        # handle 메소드는 커맨드가 실행될 때 실행되는 메소드입니다.
    # self는 Command 클래스의 인스턴스를 의미합니다.
    # *args는 임의의 개수의 인자를 받을 수 있습니다.
    # **options는 임의의 키워드 인자를 받을 수 있습니다.
    
    def handle(self, *args, **options):
        total = options.get("total")
        faker = Faker(["ko_KR"])

        # faker.unique.bs()는 랜덤한 문장을 생성합니다.
        # unique는 중복되지 않는 값을 생성합니다.
        # bs()는 랜덤한 문장을 생성합니다.
        # Book.objects.create()를 통해 Book 객체를 생성하고 데이터베이스에 저장할 수 있습니다.
        # isbn = faker.unique.bs()[:9]를 통해 9자리의 랜덤한 숫자를 생성하고, ABC123123123 OR 123123123DEF -> 12자리의 ISBN을 생성합니다.
        isbn_list = [f'ABC{faker.unique.random_int(min=100000000, max=999999999)}',
                     f'{faker.unique.random_int(min=100000000, max=999999999)}ABC'
                     ]
        categories = (
            # ('저장될 값', '화면에 보여질 값')
            ('programming', '프로그래밍'),
            ('essay', '에세이'),
            ('novel', '소설'),
            ('science', '과학'),
        )
        for _ in range(total):
            Book.objects.create(
                title=faker.unique.bs(),
                description=faker.unique.bs(),
                page_count=faker.random_int(min=1, max=1000),
                price=faker.random_int(min=1000, max=100000),
                isbn=isbn_list[faker.random_int(min=0, max=1)],
                category=faker.random_element(elements=categories)[0],
                author=user,
            )
        # seeder = Seed.seeder()
        # seeder.add_entity(Book, total, {
        #     "title": lambda x: seeder.faker.sentence(),
        #     "content": lambda x: seeder.faker.text(),
        #     "user": user,
        # })
        # seeder.execute() # seeder.execute()를 통해 데이터베이스에 데이터를 저장할 수 있습니다.
        self.stdout.write(self.style.SUCCESS(f"{total}개 의 도서 데이터가 생성되었습니다."))