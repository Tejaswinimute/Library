from Book.models import Book

#Read
'''b = Book.objects.all()
print(type(b))
print(list(b))
b1 = Book.objects.get(id=3)
print(type(b1))'''

#Create
'''b4=Book(name="Shala", author="Satish Kumar", qty=60,price=300)
b4.save()
#or
Book.objects.create(name="The Legend Bhagat Singh", author='Raj Guru', qty=90,price=500,is_publish=True)'''

#Update
'''b4=Book.objects.get(id=3)
print(b4)
b4.price = 491
b4.save()'''

#Delete
'''b1=Book.objects.get(id=1)
b1.delete()'''

'''b2=Book.objects.get(id=2)
print("Book Name: ", b2.name)
print("Is_Publish: ", b2.is_publish)'''

'''all = Book.objects.all()
for i in all:
    print(i.__dict__)'''

'''all = Book.objects.all().values('id', 'name', 'author')
for i in all:
    print(i)'''

'''all = Book.objects.all().values_list('id', 'name', 'author')
for i in all:
    print(i)'''

#To Fill Random Data In Database
import random

for i in range(0,36):
    b = Book( name=(chr(random.randint(65,90))*2), author='ABC', qty=random.randint(10,85), price=random.randint(200,900))
    b.save()


