from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# メモリ内データベースを作成
engine = create_engine('sqlite:///:memory:', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


# サンプルデータ用のテーブルを定義
class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department")


# テーブルを作成
Base.metadata.create_all(engine)

# サンプルデータを挿入
dept1 = Department(name='HR')
dept2 = Department(name='Engineering')
session.add_all([dept1, dept2])
session.commit()

emp1 = Employee(name='Alice', department_id=dept1.id)
emp2 = Employee(name='Bob', department_id=dept2.id)
emp3 = Employee(name='Charlie', department_id=dept1.id)
session.add_all([emp1, emp2, emp3])
session.commit()

# 等結合のクエリを実行
result = session.query(Employee.name, Department.name).join(Department, Employee.department_id == Department.id).all()

# 結果を表示
for emp_name, dept_name in result:
    print(f'Employee: {emp_name}, Department: {dept_name}')
