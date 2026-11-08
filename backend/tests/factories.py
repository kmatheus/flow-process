import factory
from app.models.usuario import Usuario
from app.models.operador import Operador
from app.core.security import gerar_hash_senha

class UsuarioFactory(factory.Factory):
    class Meta:
        model = Usuario

    id = factory.Faker('uuid4')
    email = factory.Faker('email')
    senha_hash = factory.LazyFunction(lambda: gerar_hash_senha("senha123"))
    nome = factory.Faker('name', locale='pt_BR')
    is_admin = False
    ativo = True

class OperadorFactory(factory.Factory):
    class Meta:
        model = Operador

    id = factory.Faker('uuid4')
    nome_completo = factory.Faker('name', locale='pt_BR')
    data_nascimento = factory.Faker('date_of_birth', minimum_age=18, maximum_age=60)
    # Gera um CPF numérico aleatório para testes (simplificado)
    cpf = factory.Sequence(lambda n: f"123456789{n:02d}"[-11:])
    telefone1 = factory.Faker('numerify', text='119########')
    ativo = True